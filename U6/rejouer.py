#!/usr/bin/env python3
"""Parcours rejoués par le coordinateur, séparés de ceux du producteur."""
import argparse
import hashlib
import json
import threading
from datetime import datetime, timezone
from functools import partial
from http.server import ThreadingHTTPServer
from pathlib import Path

from playwright.sync_api import expect, sync_playwright
from capturer import QuietHandler, manifest


def check(checks, name, test):
    try:
        observation = test()
        checks.append({"name": name, "status": "PASS", "observation": observation})
    except Exception as exc:
        checks.append({"name": name, "status": "FAIL", "observation": str(exc)[:1600]})


def sillage(page, checks):
    def entry():
        page.locator(".nav-action[data-start]").click()
        expect(page.locator("#client")).to_be_focused()
        return "Le CTA de navigation place le focus dans le champ client de l'exemple."
    check(checks, "CTA principal", entry)

    def total():
        page.locator("#quantity").fill("3")
        page.locator("#rate").fill("120")
        page.locator("#tax").select_option("20")
        expect(page.locator("#total")).to_have_text("432,00 €")
        return "3 × 120 € HT, TVA illustrative 20 %, total 432 € TTC."
    check(checks, "Calcul interactif", total)

    def invalid():
        page.locator("#client").fill("")
        page.locator("#prepare").click()
        expect(page.locator("#client")).to_be_focused()
        expect(page.locator("#client")).to_have_attribute("aria-invalid", "true")
        expect(page.locator("#client-error")).to_be_visible()
        assert not page.locator("#preview-dialog").evaluate("el=>el.open")
        return "Client vide : erreur visible associée au champ, focus rendu, aucun aperçu."
    check(checks, "Erreur puis récupération", invalid)

    def preview():
        page.locator("#client").fill("Test du coordinateur")
        page.locator("#service").fill("Révision de page")
        page.locator("#prepare").click()
        expect(page.locator("#preview-dialog")).to_be_visible()
        expect(page.locator("#preview-client")).to_have_text("Test du coordinateur")
        expect(page.locator("#preview-total")).to_contain_text("432,00 €")
        expect(page.locator("#close-preview")).to_be_focused()
        return "Récupération et aperçu : nom et total transmis ; focus dans le dialogue."
    check(checks, "Aperçu après récupération", preview)

    def focus():
        for key in ["Tab"] * 7 + ["Shift+Tab"] * 7:
            page.keyboard.press(key)
            assert page.evaluate("document.getElementById('preview-dialog').contains(document.activeElement)")
        return "Quatorze déplacements Tab/Maj+Tab restent dans le dialogue modal."
    check(checks, "Clavier du dialogue", focus)

    def download():
        with page.expect_download() as pending:
            page.locator("#download").click()
        downloaded = pending.value
        content = Path(downloaded.path()).read_text()
        assert downloaded.suggested_filename.endswith(".txt")
        assert "Test du coordinateur" in content and "432,00 €" in content
        assert "PAS UNE FACTURE FISCALE" in content
        return "Fichier texte réellement téléchargé, nom/total exacts, statut de démonstration explicite."
    check(checks, "Téléchargement local", download)

    def close():
        page.keyboard.press("Escape")
        expect(page.locator("#preview-dialog")).not_to_be_visible()
        expect(page.locator("#prepare")).to_be_focused()
        return "Échap ferme l'aperçu et rend le focus au bouton de préparation."
    check(checks, "Fermeture et retour du focus", close)


def folio(page, checks):
    def entry():
        page.locator("#primary-action").click()
        expect(page.locator("#demo")).to_be_visible()
        expect(page.locator("#client")).to_be_focused()
        return "Le CTA ouvre la démonstration et place le focus dans le champ client."
    check(checks, "CTA principal", entry)

    def invalid():
        page.locator("#client").fill("")
        page.locator(".form-submit").click()
        expect(page.locator("#client")).to_be_focused()
        expect(page.locator("#client")).to_have_attribute("aria-invalid", "true")
        expect(page.locator("#client-error")).to_be_visible()
        expect(page.locator("#invoice-form")).to_be_visible()
        return "Client vide : erreur visible, focus rendu, saisie conservée."
    check(checks, "Erreur client", invalid)

    def amount_error():
        page.locator("#client").fill("Test du coordinateur")
        page.locator("#amount").fill("abc")
        page.locator(".form-submit").click()
        expect(page.locator("#amount")).to_be_focused()
        expect(page.locator("#amount")).to_have_attribute("aria-invalid", "true")
        return "Montant non numérique : erreur liée au champ, focus et valeurs conservés."
    check(checks, "Erreur montant", amount_error)

    def calculate():
        page.locator("#service").fill("Révision de page")
        page.locator("#amount").fill("360,00")
        page.locator("#tax").select_option("20")
        page.locator(".form-submit").click()
        expect(page.locator("#success")).to_be_visible()
        expect(page.locator("#success-total")).to_have_text("432,00 €")
        expect(page.locator("#invoice-client")).to_have_text("Test du coordinateur")
        expect(page.locator("#invoice-total")).to_have_text("432,00 €")
        return "Montant 360 € HT saisi avec virgule : total 432 € transmis au document et à l'aperçu."
    check(checks, "Récupération, calcul et transmission", calculate)

    def focus():
        for key in ["Tab"] * 7 + ["Shift+Tab"] * 7:
            page.keyboard.press(key)
            assert page.evaluate("document.getElementById('demo').contains(document.activeElement)")
        return "Quatorze déplacements Tab/Maj+Tab restent dans le dialogue modal."
    check(checks, "Clavier du dialogue", focus)

    def download():
        with page.expect_download() as pending:
            page.locator("#download").click()
        downloaded = pending.value
        content = Path(downloaded.path()).read_text()
        assert "Test du coordinateur" in content and "432,00 €" in content
        assert "SANS VALEUR COMPTABLE" in content and "AUCUN ENVOI" in content
        return "Téléchargement local réel, valeurs exactes et exemple sans valeur comptable explicite."
    check(checks, "Téléchargement local", download)

    def edit():
        page.locator("#edit").click()
        expect(page.locator("#client")).to_be_focused()
        expect(page.locator("#client")).to_have_value("Test du coordinateur")
        return "Retour à la saisie avec valeurs préservées et focus sur le client."
    check(checks, "Retour à la saisie", edit)

    def close():
        page.keyboard.press("Escape")
        expect(page.locator("#demo")).not_to_be_visible()
        expect(page.locator("#primary-action")).to_be_focused()
        return "Échap ferme la démo et rend le focus au CTA d'origine."
    check(checks, "Fermeture et focus", close)

    def steps():
        page.locator('[data-step="2"]').click()
        expect(page.locator('[data-step="2"]')).to_have_attribute("aria-pressed", "true")
        expect(page.locator("#status-pill")).to_have_text("Réglée")
        expect(page.locator("#step-copy")).to_contain_text("aucun paiement réel")
        page.locator('[data-step="0"]').click()
        expect(page.locator("#status-pill")).to_have_text("Brouillon")
        return "Sélection d'étapes fonctionnelle, état réglé signalé comme illustration sans paiement réel."
    check(checks, "Sélecteur de parcours illustratif", steps)


def trait(page, checks):
    trigger = page.locator("[data-open-demo]").nth(1)

    def entry():
        trigger.click()
        expect(page.locator("#demo-dialog")).to_be_visible()
        expect(page.locator("#client")).to_be_focused()
        return "CTA de la première scène : ouverture de la démo, focus sur le client."
    check(checks, "CTA principal", entry)

    def invalid():
        page.locator("#client").fill("")
        page.locator(".form-button").click()
        expect(page.locator("#client")).to_be_focused()
        expect(page.locator("#client")).to_have_attribute("aria-invalid", "true")
        expect(page.locator("#client-error")).to_be_visible()
        return "Client vide : erreur associée au champ et focus rendu."
    check(checks, "Erreur client", invalid)

    def amount_error():
        page.locator("#client").fill("Test du coordinateur")
        page.locator("#amount").fill("-1")
        page.locator(".form-button").click()
        expect(page.locator("#amount")).to_be_focused()
        expect(page.locator("#amount")).to_have_attribute("aria-invalid", "true")
        return "Montant négatif refusé, erreur liée au champ et données conservées."
    check(checks, "Erreur montant", amount_error)

    def calculate():
        page.locator("#service").fill("Révision de page")
        page.locator("#amount").fill("360")
        page.locator("#vat").select_option("20")
        page.locator(".form-button").click()
        expect(page.locator("#result-view")).to_be_visible()
        expect(page.locator("#result-sheet [data-doc-client]")).to_have_text("Test du coordinateur")
        expect(page.locator("#result-sheet [data-doc-total]")).to_have_text("432,00 €")
        return "360 € HT, TVA illustrative 20 %, nom et total 432 € transmis au document."
    check(checks, "Récupération, calcul et transmission", calculate)

    def focus():
        for key in ["Tab"] * 7 + ["Shift+Tab"] * 7:
            page.keyboard.press(key)
            active = page.evaluate("document.activeElement.tagName + '#' + document.activeElement.id")
            assert page.evaluate("document.getElementById('demo-dialog').contains(document.activeElement)"), f"Focus hors dialogue après {key} : {active}"
        return "Quatorze déplacements Tab/Maj+Tab restent dans le dialogue modal."
    check(checks, "Clavier du dialogue", focus)

    def download():
        with page.expect_download() as pending:
            page.locator("#download-example").click()
        content = Path(pending.value.path()).read_text()
        assert "Test du coordinateur" in content and "432,00 €" in content
        assert "sans valeur comptable" in content and "Aucun document envoyé" in content
        return "Fichier texte téléchargé avec les données saisies et le statut d'exemple."
    check(checks, "Téléchargement local", download)

    def edit():
        page.locator("#edit-example").click()
        expect(page.locator("#client")).to_be_focused()
        expect(page.locator("#client")).to_have_value("Test du coordinateur")
        return "Retour à la saisie avec valeurs et focus préservés."
    check(checks, "Retour à la saisie", edit)

    def close():
        page.keyboard.press("Escape")
        expect(page.locator("#demo-dialog")).not_to_be_visible()
        expect(trigger).to_be_focused()
        return "Échap ferme la démo et rend le focus au CTA d'origine."
    check(checks, "Fermeture et focus", close)


def pli(page, checks):
    trigger = page.locator("#primary-cta")

    def entry():
        trigger.click()
        expect(page.locator("#editor")).to_be_visible()
        expect(page.locator("#client")).to_be_focused()
        return "CTA de la première scène : ouverture de l'éditeur et focus sur le client."
    check(checks, "CTA principal", entry)

    def invalid():
        page.locator("#client").fill("")
        page.locator("#submit-invoice").click()
        expect(page.locator("#client")).to_be_focused()
        expect(page.locator("#client")).to_have_attribute("aria-invalid", "true")
        expect(page.locator("#client-error")).to_be_visible()
        return "Client vide refusé ; erreur locale associée et focus rendu au champ."
    check(checks, "Erreur client", invalid)

    def amount_error():
        page.locator("#client").fill("Test du coordinateur")
        page.locator("#hours").fill("-1")
        page.locator("#submit-invoice").click()
        expect(page.locator("#hours")).to_be_focused()
        expect(page.locator("#hours")).to_have_attribute("aria-invalid", "true")
        expect(page.locator("#client")).to_have_value("Test du coordinateur")
        return "Heures négatives refusées, nom conservé et erreur liée au champ."
    check(checks, "Erreur quantité", amount_error)

    def focus():
        for key in ["Tab"] * 7 + ["Shift+Tab"] * 7:
            page.keyboard.press(key)
            active = page.evaluate("document.activeElement.tagName + '#' + document.activeElement.id")
            assert page.evaluate("document.getElementById('editor').contains(document.activeElement)"), f"Focus hors dialogue après {key} : {active}"
        return "Quatorze déplacements Tab/Maj+Tab restent dans l'éditeur modal."
    check(checks, "Clavier du dialogue", focus)

    def calculate():
        page.locator("#service").fill("Révision de page")
        page.locator("#hours").fill("3")
        page.locator("#rate").fill("120")
        page.locator("#tax").select_option("20")
        expect(page.locator("#form-total")).to_have_text("432,00 €")
        page.locator("#submit-invoice").click()
        expect(page.locator("#editor")).not_to_be_visible()
        expect(page.locator("#client-output")).to_have_text("Test du coordinateur")
        expect(page.locator("#grand-total")).to_have_text("432,00 €")
        expect(page.locator("#success")).to_be_visible()
        expect(page.locator("#success")).to_be_focused()
        return "3 h × 120 € HT + 20 % = 432 € ; valeurs transmises au brouillon, fermeture de l'éditeur et focus sur le résultat."
    check(checks, "Récupération, calcul et transmission", calculate)

    def download():
        with page.expect_download() as pending:
            page.locator("#download").click()
        content = Path(pending.value.path()).read_text()
        assert "Test du coordinateur" in content and "432,00 €" in content
        assert "SANS VALEUR DE FACTURE LÉGALE" in content and "Aucun envoi" in content
        return "Brouillon texte réellement téléchargé, avec données saisies et statut d'exemple."
    check(checks, "Téléchargement local", download)

    def edit():
        page.locator("#edit-example").click()
        expect(page.locator("#client")).to_be_focused()
        expect(page.locator("#client")).to_have_value("Test du coordinateur")
        expect(page.locator("#hours")).to_have_value("3")
        return "Réouverture avec valeurs conservées et focus dans l'éditeur."
    check(checks, "Retour à la saisie", edit)

    def close():
        page.keyboard.press("Escape")
        expect(page.locator("#editor")).not_to_be_visible()
        expect(page.locator("#edit-example")).to_be_focused()
        return "Échap ferme l'éditeur et rend le focus au bouton utilisé pour le rouvrir."
    check(checks, "Fermeture et focus", close)


def rayon(page, checks):
    def entry():
        page.locator("#primary-cta").click()
        expect(page.locator("#booking-title")).to_be_focused()
        expect(page.locator("#stage-one")).to_be_visible()
        return "Action principale : arrivée sur le formulaire de créneau et focus sur son titre."
    check(checks, "CTA principal", entry)

    def missing_time():
        page.locator("#continue").click()
        expect(page.locator("#time-error")).to_be_visible()
        expect(page.locator("#time-0900")).to_be_focused()
        expect(page.locator("#time-0900")).to_have_attribute("aria-invalid", "true")
        return "Heure manquante refusée ; message associé et focus sur une heure disponible."
    check(checks, "Erreur de créneau", missing_time)

    def radios():
        page.locator('label[for="service-check"]').click()
        page.locator('label[for="day-wed"]').click()
        page.locator('label[for="time-0900"]').click()
        expect(page.locator("#time-1400")).to_be_disabled()
        page.keyboard.press("ArrowRight")
        expect(page.locator("#time-1130")).to_be_checked()
        page.keyboard.press("ArrowRight")
        expect(page.locator("#time-1630")).to_be_checked()
        page.keyboard.press("ArrowLeft")
        expect(page.locator("#time-1130")).to_be_checked()
        return "Radios natifs utilisables au clavier ; le créneau désactivé de 14 h est sauté."
    check(checks, "Choix et clavier des créneaux", radios)

    def step_two():
        page.locator("#continue").click()
        expect(page.locator("#stage-two")).to_be_visible()
        expect(page.locator("#customer-name")).to_be_focused()
        for value in ["Une révision", "Mercredi 14 octobre 2026", "11:30"]:
            expect(page.locator("#selection-summary")).to_contain_text(value)
        return "Service, jour et heure transmis à la seconde étape ; focus sur le nom."
    check(checks, "Transmission du choix", step_two)

    def empty_contact():
        page.locator("#prepare").click()
        expect(page.locator("#customer-name")).to_be_focused()
        expect(page.locator("#customer-name")).to_have_attribute("aria-invalid", "true")
        expect(page.locator("#name-error")).to_be_visible()
        expect(page.locator("#email-error")).to_be_visible()
        return "Coordonnées vides refusées ; erreurs locales et focus sur le premier champ."
    check(checks, "Erreur coordonnées vides", empty_contact)

    def invalid_email():
        page.locator("#customer-name").fill("Test du coordinateur")
        page.locator("#customer-email").fill("adresse-invalide")
        page.locator("#prepare").click()
        expect(page.locator("#customer-email")).to_be_focused()
        expect(page.locator("#customer-email")).to_have_attribute("aria-invalid", "true")
        expect(page.locator("#customer-name")).to_have_value("Test du coordinateur")
        return "E-mail invalide refusé ; nom et choix conservés."
    check(checks, "Erreur e-mail et conservation", invalid_email)

    def back():
        page.locator("#customer-email").fill("coord@example.com")
        page.locator("#bike-notes").fill("Frein avant à régler")
        page.locator("#back").click()
        expect(page.locator("#stage-one")).to_be_visible()
        expect(page.locator("#time-1130")).to_be_checked()
        page.locator("#continue").click()
        expect(page.locator("#customer-name")).to_have_value("Test du coordinateur")
        expect(page.locator("#customer-email")).to_have_value("coord@example.com")
        return "Aller-retour entre étapes sans perdre le créneau ou les coordonnées."
    check(checks, "Retour et reprise", back)

    def success():
        page.locator("#prepare").click()
        expect(page.locator("#success")).to_be_visible()
        expect(page.locator("#success-title")).to_be_focused()
        for value in ["Test du coordinateur", "Mercredi 14 octobre 2026", "11:30", "Une révision", "Frein avant à régler"]:
            expect(page.locator("#success-data")).to_contain_text(value)
        expect(page.locator(".success-copy")).to_contain_text("Aucune réservation")
        expect(page.locator(".success-copy")).to_contain_text("aucun e-mail")
        return "Récapitulatif exact avec focus et statut de démonstration sans réservation ou envoi."
    check(checks, "Préparation locale et résultat", success)

    def restart():
        page.locator("#restart").click()
        expect(page.locator("#stage-one")).to_be_visible()
        expect(page.locator("#success")).not_to_be_visible()
        expect(page.locator("#service-repair")).to_be_checked()
        expect(page.locator('input[name="time"]:checked')).to_have_count(0)
        expect(page.locator("#service-repair")).to_be_focused()
        return "Nouvel essai : formulaire réinitialisé et focus rendu au premier choix."
    check(checks, "Recommencer", restart)


def rayon_libre(page, checks):
    def entry():
        page.get_by_role("link", name="Prendre rendez-vous").click()
        expect(page.locator('input[name="service"]:checked')).to_be_focused()
        page.locator('label.service-choice').filter(has=page.locator('input[value="Freins ou vitesses"]')).click()
        page.locator("#to-slots").click()
        expect(page.locator("#step-2")).to_be_visible()
        expect(page.locator("#slots-title")).to_be_focused()
        return "Action de rendez-vous, choix du besoin et arrivée sur les créneaux avec focus."
    check(checks, "CTA principal et besoin", entry)

    def missing_time():
        page.locator("#to-contact").click()
        expect(page.locator("#slot-error")).to_contain_text("Sélectionnez une heure")
        expect(page.locator('input[name="time"][value="09:00"]')).to_be_focused()
        return "Heure manquante refusée, message local et focus sur une heure disponible."
    check(checks, "Erreur de créneau", missing_time)

    def unavailable():
        page.locator("label.date-choice").filter(has=page.locator('input[value="Jeudi 15 octobre"]')).click()
        expect(page.locator(".unavailable")).to_contain_text("Aucun créneau")
        page.locator("#to-contact").click()
        expect(page.locator("#slot-error")).to_contain_text("Choisissez un autre jour")
        expect(page.locator('input[name="date"]:checked')).to_be_focused()
        return "Jour sans créneau : arrêt explicite, aucun passage à la suite, focus pour changer de jour."
    check(checks, "Jour indisponible", unavailable)

    def radios():
        page.locator("label.date-choice").filter(has=page.locator('input[value="Mardi 13 octobre"]')).click()
        page.locator("label.time-choice").filter(has=page.locator('input[value="09:00"]')).click()
        expect(page.locator('input[name="time"][value="14:00"]')).to_be_disabled()
        page.keyboard.press("ArrowRight")
        expect(page.locator('input[name="time"][value="11:00"]')).to_be_checked()
        page.keyboard.press("ArrowRight")
        expect(page.locator('input[name="time"][value="09:00"]')).to_be_checked()
        page.locator("label.date-choice").filter(has=page.locator('input[value="Mercredi 14 octobre"]')).click()
        expect(page.locator('input[name="time"]:checked')).to_have_count(0)
        page.locator("label.time-choice").filter(has=page.locator('input[value="15:00"]')).click()
        return "Flèches natives sautent le créneau désactivé ; changement de jour efface l'ancienne heure."
    check(checks, "Clavier et changement de jour", radios)

    def contact():
        page.locator("#to-contact").click()
        expect(page.locator("#step-3")).to_be_visible()
        expect(page.locator("#contact-title")).to_be_focused()
        for value in ["Freins ou vitesses", "Mercredi 14 octobre", "15:00"]:
            expect(page.locator("#mini-summary")).to_contain_text(value)
        return "Besoin, jour et heure transmis à la saisie de coordonnées."
    check(checks, "Transmission du choix", contact)

    def empty_contact():
        page.locator('#step-3 button[type="submit"]').click()
        expect(page.locator("#name")).to_be_focused()
        expect(page.locator("#name")).to_have_attribute("aria-invalid", "true")
        expect(page.locator("#name-error")).not_to_be_empty()
        expect(page.locator("#email-error")).not_to_be_empty()
        return "Coordonnées vides refusées, erreurs nommées et focus sur le premier champ."
    check(checks, "Erreur coordonnées vides", empty_contact)

    def invalid_email():
        page.locator("#name").fill("Test du coordinateur")
        page.locator("#email").fill("adresse-invalide")
        page.locator('#step-3 button[type="submit"]').click()
        expect(page.locator("#email")).to_be_focused()
        expect(page.locator("#email")).to_have_attribute("aria-invalid", "true")
        expect(page.locator("#name")).to_have_value("Test du coordinateur")
        return "E-mail invalide refusé sans perte du nom ou des choix."
    check(checks, "Erreur e-mail et conservation", invalid_email)

    def back():
        page.locator("#email").fill("coord@example.com")
        page.locator("#note").fill("Frein avant à régler")
        page.locator('[data-back="2"]').click()
        expect(page.locator('input[name="time"][value="15:00"]')).to_be_checked()
        page.locator("#to-contact").click()
        expect(page.locator("#name")).to_have_value("Test du coordinateur")
        expect(page.locator("#email")).to_have_value("coord@example.com")
        return "Aller-retour entre étapes avec conservation de l'heure et des coordonnées."
    check(checks, "Retour et reprise", back)

    def success():
        page.locator('#step-3 button[type="submit"]').click()
        expect(page.locator("#step-4")).to_be_visible()
        expect(page.locator("#success-title")).to_be_focused()
        for value in ["Test du coordinateur", "coord@example.com", "Mercredi 14 octobre", "15:00", "Freins ou vitesses", "Frein avant à régler"]:
            expect(page.locator("#final-summary")).to_contain_text(value)
        expect(page.locator(".success-note")).to_contain_text("Aucun rendez-vous")
        expect(page.locator(".success-note")).to_contain_text("aucun message")
        return "Récapitulatif exact, focus sur le résultat et statut d'exemple sans réservation ni envoi."
    check(checks, "Préparation locale et résultat", success)

    def restart():
        page.locator("#restart").click()
        expect(page.locator("#step-1")).to_be_visible()
        expect(page.locator("#name")).to_have_value("")
        expect(page.locator("#email")).to_have_value("")
        expect(page.locator('input[name="time"]:checked')).to_have_count(0)
        expect(page.locator('input[name="service"]:checked')).to_be_focused()
        return "Nouvelle simulation : coordonnées et choix de créneau effacés, focus sur le besoin."
    check(checks, "Recommencer", restart)

    def service_picker():
        page.locator('[data-service="Roue ou crevaison"]').click()
        expect(page.locator('input[name="service"][value="Roue ou crevaison"]')).to_be_checked()
        expect(page.locator('input[name="service"][value="Roue ou crevaison"]')).to_be_focused()
        return "Le choix dans la liste des réparations renseigne réellement le formulaire."
    check(checks, "Choix depuis les prestations", service_picker)

    def privacy():
        page.locator("#privacy-toggle").click()
        expect(page.locator("#privacy")).to_be_visible()
        expect(page.locator("#privacy-toggle")).to_have_attribute("aria-expanded", "true")
        page.locator("#privacy-toggle").click()
        expect(page.locator("#privacy")).not_to_be_visible()
        return "Explication des données ouvrable et refermable, état accessible renseigné."
    check(checks, "Explication des données", privacy)


TESTS = {"run-01": sillage, "run-02": folio, "run-03": trait, "run-04": pli, "run-05": rayon, "run-06": rayon_libre}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run", choices=sorted(TESTS))
    parser.add_argument("--output", type=Path, help="Copie corrigée séparée ; le livrable original reste figé.")
    parser.add_argument("--report", type=Path, help="Nouveau fichier de rapport, sans écraser une preuve.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    case = root / "runs" / args.run
    output = args.output.resolve() if args.output else case / "livrable"
    destination = args.report.resolve() if args.report else case / "parcours-coordinateur.json"
    if destination.exists():
        parser.error("Le rapport existe déjà ; conserver les résultats avant une nouvelle révision.")
    before = manifest(output)
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(output)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    report = {"started_at": datetime.now(timezone.utc).isoformat(), "run": args.run, "viewports": []}
    origin = f"http://127.0.0.1:{server.server_port}"
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(executable_path="/usr/bin/chromium", args=["--no-sandbox", "--disable-dev-shm-usage"])
            report["browser_version"] = browser.version
            for width, height in [(1440, 1000), (390, 844), (320, 844)]:
                context = browser.new_context(viewport={"width": width, "height": height}, reduced_motion="reduce", accept_downloads=True)
                page = context.new_page()
                external = []
                def restrict(route):
                    if route.request.url.startswith(origin + "/"):
                        route.continue_()
                    else:
                        external.append(route.request.url)
                        route.abort()
                context.route("**/*", restrict)
                page.goto(origin + "/index.html", wait_until="networkidle")
                checks = []
                TESTS[args.run](page, checks)
                checks.append({"name": "Aucun envoi externe pendant le parcours", "status": "PASS" if not external else "FAIL", "observation": external})
                report["viewports"].append({"width": width, "checks": checks})
                context.close()
            browser.close()
        report["source_unchanged"] = before == manifest(output)
        report["finished_at"] = datetime.now(timezone.utc).isoformat()
        report["passed"] = sum(c["status"] == "PASS" for v in report["viewports"] for c in v["checks"])
        report["failed"] = sum(c["status"] == "FAIL" for v in report["viewports"] for c in v["checks"])
        destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({k: report[k] for k in ["run", "passed", "failed", "source_unchanged"]}))
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


if __name__ == "__main__":
    main()
