#!/usr/bin/env python3
"""Validation autonome de la projection JSON RUN_CARD de Design Governance V1.

Le schéma JSON est la source des règles de structure et de vocabulaire. Le code
ci-dessous ne recopie pas ses enums : il implémente uniquement le petit sous-
ensemble de JSON Schema utilisé par le fichier livré.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "run_card.schema.json"
EXAMPLE = ROOT / "schemas" / "run_card.example.json"
FIXTURES = ROOT / "schemas" / "fixtures"


class ValidationError(Exception):
    """Erreur de validation avec un chemin lisible dans le document."""


def format_path(path: str) -> str:
    return path or "$"


def type_matches(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "null":
        return value is None
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    raise ValidationError(f"type de schéma non pris en charge : {expected}")


def validate_node(value: Any, schema: dict[str, Any], path: str = "") -> None:
    """Valide la projection JSON de RUN_CARD et ses invariants sémantiques V1."""
    if "allOf" in schema:
        for condition in schema["allOf"]:
            if_schema = condition.get("if", {})
            if_matches = True
            if "required" in if_schema and isinstance(value, dict):
                if_matches = all(key in value for key in if_schema["required"])
            if if_matches and isinstance(value, dict):
                for key, child in if_schema.get("properties", {}).items():
                    if key in value:
                        try:
                            validate_node(value[key], child, f"{path}.{key}" if path else key)
                        except ValidationError:
                            if_matches = False
                            break
                    else:
                        if_matches = False
                        break
            if if_matches:
                validate_node(value, condition.get("then", {}), path)

    if "anyOf" in schema:
        branch_errors: list[str] = []
        for branch in schema["anyOf"]:
            try:
                validate_node(value, branch, path)
                break
            except ValidationError as exc:
                branch_errors.append(str(exc))
        else:
            details = " ; ".join(branch_errors)
            raise ValidationError(f"{format_path(path)} : aucune branche anyOf satisfaite ({details})")

    if "const" in schema and value != schema["const"]:
        raise ValidationError(f"{format_path(path)} : valeur non canonique : {value}")

    if "enum" in schema and value not in schema["enum"]:
        raise ValidationError(f"{format_path(path)} : valeur non canonique : {value}")

    if "type" in schema:
        expected = schema["type"]
        expected_types = expected if isinstance(expected, list) else [expected]
        if not any(type_matches(value, item) for item in expected_types):
            names = ", ".join(expected_types)
            raise ValidationError(f"{format_path(path)} : type attendu {names}")

    if isinstance(value, str) and "minLength" in schema:
        if len(value.strip()) < schema["minLength"]:
            raise ValidationError(f"{format_path(path)} : chaîne vide ou composée uniquement d’espaces")

    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            raise ValidationError(f"{format_path(path)} : nombre minimal d’éléments non atteint")
        if "items" in schema:
            for index, item in enumerate(value):
                validate_node(item, schema["items"], f"{path}[{index}]")

    if isinstance(value, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                raise ValidationError(f"{format_path(path)} : champ obligatoire absent : {key}")

        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            unknown = sorted(set(value) - set(properties))
            if unknown:
                raise ValidationError(f"{format_path(path)} : champs inconnus : {', '.join(unknown)}")

        for key, child_schema in properties.items():
            if key in value:
                child_path = f"{path}.{key}" if path else key
                validate_node(value[key], child_schema, child_path)


def json_type(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, (int, float)):
        return "number"
    return {str: "string", list: "array", dict: "object"}.get(type(value), type(value).__name__)


class DuplicateKeyError(ValueError):
    """Clé JSON répétée dans un même objet."""


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"clé répétée : {key}")
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    try:
        display_path = path.relative_to(ROOT)
    except ValueError:
        display_path = path
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_keys)
    except DuplicateKeyError as exc:
        raise ValidationError(f"{exc} dans {display_path}") from exc
    except (OSError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ValidationError(f"lecture JSON impossible pour {display_path} : {exc}") from exc


def check_types(value: Any, schema: dict[str, Any], path: str = "") -> None:
    """Pré-passe de types : seuls les mots-clés `type`, `properties` et `items` sont suivis,
    pour que l’interprétation métier ne reçoive jamais une valeur d’un type illégal."""
    if not isinstance(schema, dict):
        return
    if "type" in schema:
        expected = schema["type"]
        expected_types = expected if isinstance(expected, list) else [expected]
        if not any(type_matches(value, item) for item in expected_types):
            raise ValidationError(f"{format_path(path)} : type attendu {', '.join(expected_types)}")
    elif isinstance(schema.get("enum"), list):
        # Un champ à enum sans type (ex. closure.issue) reçoit le type de ses valeurs, pour que
        # les contrôles métier ne lisent jamais une liste ou un objet à sa place.
        expected_types = sorted({json_type(item) for item in schema["enum"]})
        if json_type(value) not in expected_types:
            raise ValidationError(f"{format_path(path)} : type attendu {', '.join(expected_types)} (valeurs de l’enum)")
    if isinstance(value, dict):
        for key, child in schema.get("properties", {}).items():
            if key in value:
                check_types(value[key], child, f"{path}.{key}" if path else key)
    if isinstance(value, list) and isinstance(schema.get("items"), dict):
        for index, item in enumerate(value):
            check_types(item, schema["items"], f"{path}[{index}]")


def check_held_message(document: Any) -> None:
    """Expose le diagnostic métier historique avant le rejet d’enum générique."""
    if not isinstance(document, dict):
        return
    card = document.get("run_card")
    if not isinstance(card, dict):
        return
    closure = card.get("closure")
    if isinstance(closure, dict) and closure.get("state") == "HELD":
        raise ValidationError("HELD est un statut de direction, pas une valeur de state")


ACCEPTED = {"ACCEPTED", "ACCEPTED-WITH-RESERVATION"}
PRE_OBSERVATION = {"INTAKE", "CLASSIFIED", "SPECCED", "BUILDING"}
PLACEHOLDERS = {"todo", "tbd", "à définir", "a definir", "à déterminer", "a determiner", "à compléter", "a completer",
                "placeholder", "n/a", "?", "inconnu", "lorem ipsum"}
RESERVATION_FIELDS = ("owner", "scope", "date_version", "impact", "next_proof", "review_date", "exit_condition")
# L’exception FAIL-ASSUMED étend la réserve commune ; sa date est celle de la carte (date_version non exigée).
EXCEPTION_FIELDS = ("owner", "scope", "impact", "next_proof", "review_date", "exit_condition", "gate_axis", "failure_evidence", "requested_by")
SYSTEM_FIELDS = ("impact", "owner", "migration", "rollback", "changelog_ref")
ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}(?:[T ](\d{2}):(\d{2})(?::(\d{2})(?:\.\d+)?)?(?:Z|[+-](\d{2}):(\d{2}))?)?")


def filled(value: Any) -> bool:
    """Chaîne non vide et non placeholder."""
    return isinstance(value, str) and bool(value.strip()) and value.strip().lower() not in PLACEHOLDERS


def iso_date(value: Any) -> bool:
    match = ISO_DATE.fullmatch(value.strip()) if isinstance(value, str) else None
    if not match:
        return False
    try:
        date.fromisoformat(value.strip()[:10])
    except ValueError:
        return False
    # Heure, minute, seconde et fuseau réels (ni 25:61, ni +25:00).
    hour, minute, second, tz_hour, tz_minute = (int(part) if part else 0 for part in match.groups())
    return hour <= 23 and minute <= 59 and second <= 59 and tz_hour <= 23 and tz_minute <= 59


def check_critical_protection(card: dict[str, Any], mode: Any) -> dict[str, Any] | None:
    risk = card.get("risk")
    if not isinstance(risk, dict):
        return None
    if not filled(risk.get("statement")):
        raise ValidationError("risk.statement requis : énoncé du risque principal, non vide et sans placeholder")
    if risk.get("level") != "critical":
        return None
    if mode in {"LITE", "ITER"}:
        raise ValidationError("un risque critical interdit le mode LITE ou ITER (DIRECTION/START, Protection de niveau)")
    protection = risk.get("critical_protection")
    if not isinstance(protection, dict):
        raise ValidationError("un risque critical exige une critical_protection structurée")
    for field in ("control", "owner", "scope", "failure_action", "evidence_locator"):
        value = protection.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValidationError(f"critical_protection exige le champ {field}")
        if not filled(value):
            raise ValidationError(f"critical_protection.{field} ne peut pas être un placeholder")
    if protection.get("failure_action") not in {"RETURNED", "BLOCKED", "ESCALATED"}:
        raise ValidationError("critical_protection.failure_action doit retourner, bloquer ou escalader")
    if protection.get("result") not in {"PASS", "FAIL", "NOT-VERIFIED"}:
        raise ValidationError("critical_protection exige result (PASS, FAIL ou NOT-VERIFIED)")
    return protection


def check_protection_outcome(protection: dict[str, Any] | None, verdict: Any, issue: Any) -> None:
    if protection is None:
        return
    if protection["result"] == "NOT-VERIFIED" and verdict == "ACCEPTED":
        raise ValidationError("protection critique NOT-VERIFIED : verdict ACCEPTED interdit (la réserve reste possible)")
    if protection["result"] == "FAIL":
        if verdict in ACCEPTED:
            raise ValidationError("protection critique en échec : aucun verdict accepté")
        if issue != protection["failure_action"]:
            raise ValidationError("protection critique en échec : l’issue doit suivre critical_protection.failure_action")


def check_exception(card: dict[str, Any], closure: dict[str, Any]) -> None:
    if closure.get("issue") != "FAIL-ASSUMED":
        return
    exception = closure.get("exception")
    if not isinstance(exception, dict):
        raise ValidationError("FAIL-ASSUMED exige closure.exception (réserve commune, gate_axis, failure_evidence, requested_by, disposition)")
    missing = [field for field in EXCEPTION_FIELDS if not filled(exception.get(field))]
    if missing:
        raise ValidationError(f"closure.exception incomplète ou placeholder : {', '.join(missing)}")
    if not iso_date(exception.get("review_date")):
        raise ValidationError("closure.exception.review_date doit être une date ISO")
    proof = card.get("proof") if isinstance(card.get("proof"), dict) else {}
    if exception["failure_evidence"] not in (proof.get("observed") or []):
        raise ValidationError("exception : failure_evidence doit figurer dans proof.observed (un échec connu, pas un NOT-VERIFIED)")
    if exception.get("disposition") not in {"NON-DIFFUSÉ", "DIFFUSÉ-LIMITÉ", "RETIRÉ", "ESCALADÉ"}:
        raise ValidationError("exception exige disposition (NON-DIFFUSÉ, DIFFUSÉ-LIMITÉ, RETIRÉ ou ESCALADÉ)")


def check_time(card: dict[str, Any], closure: dict[str, Any]) -> None:
    state, verdict = closure.get("state"), closure.get("verdict")
    if state in PRE_OBSERVATION:
        if verdict is not None:
            raise ValidationError(f"state {state} : le verdict doit rester null avant CHECKING")
        if card.get("decision_change") is not None or card.get("creative_close") is not None:
            raise ValidationError(f"state {state} : decision_change et creative_close sont des champs après observation, interdits avant observation")
    if state in {"DECIDED", "CLOSED"} and verdict is None:
        raise ValidationError(f"state {state} exige un verdict")


def check_accepted(card: dict[str, Any], closure: dict[str, Any], mode: Any) -> None:
    verdict = closure.get("verdict")
    if verdict not in ACCEPTED:
        return
    axes = closure.get("axes")
    if not isinstance(axes, dict):
        raise ValidationError("un verdict accepté exige closure.axes (V, U, A, T)")
    values = [axes.get(axis) for axis in ("V", "U", "A", "T")]
    if "RETURN" in values:
        raise ValidationError("un axe RETURN interdit un verdict accepté")
    if verdict == "ACCEPTED" and "NOT-VERIFIED" in values:
        raise ValidationError("un axe NOT-VERIFIED interdit ACCEPTED (la réserve reste possible)")
    if verdict == "ACCEPTED" and "PASS-WITH-RESERVATION" in values:
        raise ValidationError("une réserve d'axe interdit ACCEPTED (PASS-WITH-RESERVATION)")
    profile = card.get("capability_profile")
    if not isinstance(profile, dict):
        raise ValidationError("un verdict accepté exige capability_profile")
    proof = card.get("proof") if isinstance(card.get("proof"), dict) else {}
    provenance = proof.get("provenance") if isinstance(proof.get("provenance"), dict) else {}
    capability = provenance.get("capability")
    available = profile.get("available") if isinstance(profile.get("available"), list) else []
    unavailable = profile.get("unavailable") if isinstance(profile.get("unavailable"), list) else []
    if provenance and (capability not in available or capability in unavailable):
        raise ValidationError("proof.provenance.capability doit être disponible (dans available, hors unavailable)")
    basis = [item for item in (profile.get("basis") or []) if isinstance(item, dict) and item.get("capability") == capability]
    if provenance and (not basis or any(item.get("kind") == "unattested_declaration" for item in basis)):
        raise ValidationError("proof.provenance.capability exige une basis attestée (basis déclarative ou absente)")
    if provenance:
        artifact = card.get("artifact") if isinstance(card.get("artifact"), dict) else {}
        if artifact.get("version") != provenance.get("artifact_version"):
            raise ValidationError("version de preuve différente de la version d'artefact (artifact.version = provenance.artifact_version)")
        if not iso_date(provenance.get("observed_at")):
            raise ValidationError("proof.provenance.observed_at doit être une date ISO")
    if verdict == "ACCEPTED-WITH-RESERVATION":
        reservations = closure.get("reservations")
        if not isinstance(reservations, list) or not reservations:
            raise ValidationError("ACCEPTED-WITH-RESERVATION exige closure.reservations")
        for reservation in reservations:
            missing = [field for field in RESERVATION_FIELDS if not isinstance(reservation, dict) or not filled(reservation.get(field))]
            if missing or not iso_date(reservation.get("review_date")):
                raise ValidationError(f"réserve incomplète ou placeholder : {', '.join(missing) or 'review_date ISO'}")
    if mode == "DIRECTION" and verdict == "ACCEPTED" and (card.get("artifact") or {}).get("rights_status") == "unknown":
        raise ValidationError("droits inconnus interdisent ACCEPTED (rights_status unknown)")
    decision_change = card.get("decision_change")
    if closure.get("state") == "CLOSED" and mode in {"ITER", "STANDARD", "DIRECTION", "SYSTÈME"} and not decision_change:
        raise ValidationError(f"{mode} clos et accepté exige decision_change (LITE : facultatif)")
    if isinstance(decision_change, dict) and decision_change.get("outcome") == "NOT-OBSERVED" and verdict == "ACCEPTED":
        raise ValidationError("decision_change NOT-OBSERVED interdit ACCEPTED")
    profile_decision = card.get("profile_decision")
    if isinstance(profile_decision, dict) and profile_decision.get("phase") != "observed":
        raise ValidationError("profil non observé : un verdict accepté exige profile_decision.phase observed")


def check_consequence(card: dict[str, Any], closure: dict[str, Any], mode: Any) -> None:
    decision_change = card.get("decision_change")
    if decision_change is not None:
        if not isinstance(decision_change, dict) or decision_change.get("outcome") not in {"CHANGED", "CONFIRMED", "ABANDONED", "N/A-JUSTIFIED", "NOT-OBSERVED"}:
            raise ValidationError("decision_change exige outcome (CHANGED, CONFIRMED, ABANDONED, N/A-JUSTIFIED ou NOT-OBSERVED)")
        if decision_change["outcome"] == "N/A-JUSTIFIED" and not filled(decision_change.get("reason")):
            raise ValidationError("decision_change N/A-JUSTIFIED exige une raison")
    if closure.get("issue") == "RECLASSIFIED":
        transition = closure.get("reclassification")
        if not isinstance(transition, dict) or not filled(transition.get("successor_run_ref")):
            raise ValidationError("RECLASSIFIED exige closure.reclassification (to_mode, successor_run_ref)")
        if transition.get("to_mode") == mode:
            raise ValidationError("reclassification : mode cible identique au mode du run")
    profile_decision = card.get("profile_decision")
    if isinstance(profile_decision, dict) and profile_decision.get("phase") not in {"intended", "observed"}:
        raise ValidationError("profile_decision exige phase (intended ou observed)")


def check_system_package(closure: dict[str, Any], mode: Any) -> None:
    if mode != "SYSTÈME" or closure.get("verdict") not in ACCEPTED:
        return
    package = closure.get("system_package")
    if not isinstance(package, dict):
        raise ValidationError("SYSTÈME accepté exige closure.system_package")
    consumers = package.get("consumers")
    if not isinstance(consumers, list) or not any(filled(item) for item in consumers):
        raise ValidationError("system_package exige au moins un consumer")
    missing = [field for field in SYSTEM_FIELDS if not filled(package.get(field))]
    non_regression = package.get("non_regression") if isinstance(package.get("non_regression"), dict) else {}
    if not filled(non_regression.get("claim")):
        missing.append("non_regression.claim")
    if missing:
        raise ValidationError(f"system_package incomplet ou placeholder : {', '.join(missing)}")
    baseline = non_regression.get("baseline") if isinstance(non_regression.get("baseline"), dict) else {}
    if not all(filled(baseline.get(field)) for field in ("locator", "version", "state")):
        raise ValidationError("non_regression.baseline exige locator, version et état")


def check_b1b(closure: dict[str, Any], mode: Any) -> None:
    axes = closure.get("axes") if isinstance(closure.get("axes"), dict) else {}
    if mode != "DIRECTION" or closure.get("verdict") not in ACCEPTED or axes.get("V") not in {"PASS", "PASS-WITH-RESERVATION"}:
        return
    b1b = closure.get("b1b")
    if not isinstance(b1b, dict):
        raise ValidationError("DIRECTION acceptée avec V PASS exige closure.b1b")
    if b1b.get("status") == "DONE":
        pair = b1b.get("pair") if isinstance(b1b.get("pair"), dict) else {}
        if not all(filled(pair.get(field)) for field in ("before_locator", "after_locator", "decision")) or pair.get("outcome") not in {"confirmed", "modified", "abandoned"}:
            raise ValidationError("paire B1b incomplète : before_locator, after_locator, decision, outcome")
        if pair["before_locator"].strip() == pair["after_locator"].strip():
            raise ValidationError("paire B1b : captures distinctes exigées (before_locator ≠ after_locator)")
        return
    if b1b.get("status") == "N/A-JUSTIFIED":
        if b1b.get("reason") not in {"no_editable_decision", "equivalent_pair_valid"}:
            raise ValidationError("motif N/A B1b non recevable (no_editable_decision ou equivalent_pair_valid)")
        if not all(filled(b1b.get(field)) for field in ("covered_decision", "owner", "next_proof")):
            raise ValidationError("N/A B1b exige covered_decision, owner et next_proof")
        if b1b["reason"] == "equivalent_pair_valid" and not filled(b1b.get("pair_ref")):
            raise ValidationError("N/A B1b par paire équivalente exige pair_ref")
        return
    raise ValidationError("closure.b1b.status doit être DONE ou N/A-JUSTIFIED")


def check_direction(card: dict[str, Any], closure: dict[str, Any]) -> None:
    verdict = closure.get("verdict")
    direction = card.get("direction")
    if not isinstance(direction, dict):
        raise ValidationError("DIRECTION exige un objet direction avec thèse, anti-direction et premier objet")
    for field in ("thesis", "anti_direction", "first_object"):
        value = direction.get(field)
        if field == "anti_direction":
            if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
                raise ValidationError("DIRECTION exige une anti_direction non vide")
        elif not isinstance(value, str) or not value.strip():
            raise ValidationError(f"DIRECTION exige le champ direction.{field}")
    if not card.get("trace_locator"):
        raise ValidationError("DIRECTION exige trace_locator pour une RUN_CARD persistante")
    if closure.get("state") in {"DECIDED", "CLOSED"} and not closure.get("direction_status"):
        raise ValidationError("DIRECTION décidée ou clôturée exige direction_status")
    artifact = card.get("artifact") if isinstance(card.get("artifact"), dict) else {}
    if artifact.get("rights_status") not in {"not_applicable", "cleared", "unknown", "restricted"}:
        raise ValidationError("DIRECTION exige artifact.rights_status (not_applicable, cleared, unknown ou restricted)")
    if direction.get("identity_stake") not in {"high", "normal"}:
        raise ValidationError("DIRECTION exige direction.identity_stake (high ou normal)")
    anchors = card.get("anchors")
    if not isinstance(anchors, list):
        raise ValidationError("DIRECTION exige anchors (liste, éventuellement vide)")
    if not anchors:
        if verdict in ACCEPTED:
            raise ValidationError("DIRECTION sans ancrage : verdict accepté interdit")
        if closure.get("issue") is None:
            raise ValidationError("DIRECTION sans ancrage exige une issue (sérialisation honnête, ACTION/PIPELINE-DIRECTION)")
    for anchor in anchors:
        if not isinstance(anchor, dict):
            raise ValidationError("chaque ancrage DIRECTION doit être structuré")
        if "type" not in anchor:
            raise ValidationError("ancrage exige type (generated, observed ou provided)")
        if verdict in ACCEPTED and anchor.get("transformation_status") != "transformed":
            raise ValidationError("un verdict accepté exige transformation_status transformed")
    calibration = direction.get("calibration")
    if calibration is not None:
        if not isinstance(calibration, dict) or calibration.get("basis") not in {"observed_anchor", "provided_anchor", "real_constraint", "generated_only_reserved"}:
            raise ValidationError("base de calibration non recevable (une revue indépendante n’est pas une calibration)")
        if calibration["basis"] == "generated_only_reserved" and verdict == "ACCEPTED":
            raise ValidationError("calibration générée seule interdit ACCEPTED")
    generated_only = bool(anchors) and all(isinstance(a, dict) and a.get("type") == "generated" for a in anchors)
    if (direction.get("identity_stake") == "high" and generated_only
            and closure.get("direction_status") in {"HELD", "HELD-WITH-ACCEPTED-DIFFERENCE"}):
        if not isinstance(calibration, dict) or calibration.get("basis") not in {"real_constraint", "generated_only_reserved"}:
            raise ValidationError("enjeu d’identité élevé : ancrage généré seul exige calibration (real_constraint ou generated_only_reserved)")
    profile_decision = card.get("profile_decision")
    if profile_decision is not None:
        if not isinstance(profile_decision, dict):
            raise ValidationError("profile_decision doit être un objet")
        for field in ("decision", "dials", "counterindication", "evidence"):
            value = profile_decision.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValidationError(f"profile_decision : champ obligatoire absent : {field}")
    creative_close = card.get("creative_close")
    if closure.get("state") == "CLOSED":
        if not isinstance(creative_close, dict):
            raise ValidationError("DIRECTION clôturée exige creative_close")
        for field in ("presence", "signature", "craft_detail", "dominant_defect", "next_polish_action"):
            value = creative_close.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValidationError(f"creative_close exige le champ {field}")
    for anchor in anchors:
        if not iso_date(anchor.get("date")):
            raise ValidationError("date d'ancrage ISO exigée (AAAA-MM-JJ)")
        for field in ("role", "source", "date", "scope", "transformation", "transformation_status", "limitation"):
            if not isinstance(anchor.get(field), str) or not anchor[field].strip():
                raise ValidationError(f"ancrage DIRECTION incomplet : {field}")
        for field in ("retained", "rejected"):
            value = anchor.get(field)
            if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
                raise ValidationError(f"ancrage DIRECTION exige {field} non vide")


def check_semantic_contract(document: Any) -> None:
    """Contrôle les invariants de la liste close (D-ACT-1) documentés par ACTION et DIRECTION."""
    if not isinstance(document, dict):
        return
    card = document.get("run_card")
    if not isinstance(card, dict):
        return

    mode = card.get("mode")
    capability_profile = card.get("capability_profile")
    if isinstance(capability_profile, dict):
        groups = {key: {value.strip() for value in capability_profile.get(key, []) if isinstance(value, str)}
                  for key in ("available", "unavailable", "not_required")}
        conflicts = (groups["available"] & groups["unavailable"]
                     | groups["available"] & groups["not_required"]
                     | groups["unavailable"] & groups["not_required"])
        if conflicts:
            raise ValidationError("capability_profile : capacité dans plusieurs catégories : " + ", ".join(sorted(conflicts)))
        available = capability_profile.get("available")
        basis = capability_profile.get("basis")
        if isinstance(available, list) and available and (not isinstance(basis, list) or not basis):
            raise ValidationError("capability_profile exige basis non vide lorsque available contient un élément")
    protection = check_critical_protection(card, mode)
    closure = card.get("closure")
    if not isinstance(closure, dict):
        return
    verdict = closure.get("verdict")
    issue = closure.get("issue")
    check_time(card, closure)
    check_protection_outcome(protection, verdict, issue)
    check_exception(card, closure)

    if mode == "DIRECTION":
        check_direction(card, closure)
    if mode in {"ITER", "STANDARD", "SYSTÈME"} and not card.get("trace_locator"):
        raise ValidationError(f"{mode} exige trace_locator pour une RUN_CARD persistante")
    if mode == "ITER":
        direction = card.get("direction")
        if not isinstance(direction, dict) or not filled(direction.get("thesis")):
            raise ValidationError("ITER exige un rappel de direction (direction.thesis) ; sinon reclasser (DIRECTION, ITER se souvient)")

    if closure.get("direction_status") == "LOST-IN-BUILD" and verdict in ACCEPTED:
        raise ValidationError("LOST-IN-BUILD ne peut pas produire un verdict accepté")
    if issue is not None and verdict in ACCEPTED:
        detail = " (une issue bloquante ou FAIL-ASSUMED ne peut pas produire un verdict accepté)" if issue in {"BLOCKED", "FAIL-ASSUMED"} else ""
        raise ValidationError(f"issue non nulle interdit un verdict accepté : {issue}{detail}")
    if closure.get("direction_status") == "PARTIALLY-HELD" and verdict == "ACCEPTED":
        raise ValidationError("PARTIALLY-HELD interdit ACCEPTED (HELD-WITH-ACCEPTED-DIFFERENCE pour une différence acceptée)")
    proof = card.get("proof")
    if isinstance(proof, dict):
        observed = proof.get("observed")
        not_verified = proof.get("not_verified")
        if isinstance(observed, list) and isinstance(not_verified, list):
            overlap = sorted(set(observed) & set(not_verified))
            if overlap:
                raise ValidationError("proof.observed et proof.not_verified ne peuvent pas contenir le même claim")
    if verdict in ACCEPTED:
        if closure.get("state") not in {"DECIDED", "CLOSED"}:
            raise ValidationError("un verdict accepté exige state DECIDED ou CLOSED")
        if not isinstance(proof, dict) or not isinstance(proof.get("observed"), list) or not proof["observed"]:
            raise ValidationError("un verdict accepté exige au moins une preuve observed")
        provenance = proof.get("provenance") if isinstance(proof, dict) else None
        if not isinstance(provenance, dict):
            raise ValidationError("un verdict accepté exige proof.provenance")
        for field in ("artifact_locator", "artifact_version", "method", "observed_at"):
            value = provenance.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValidationError(f"proof.provenance exige le champ {field}")
        artifact = card.get("artifact")
        if isinstance(artifact, dict) and provenance.get("artifact_locator") != artifact.get("locator"):
            raise ValidationError("proof.provenance.artifact_locator doit correspondre à artifact.locator")
        limitations = closure.get("limitations")
        if not isinstance(limitations, list) or not limitations:
            raise ValidationError("un verdict accepté exige une limitation non vide")
    check_consequence(card, closure, mode)
    check_accepted(card, closure, mode)
    check_system_package(closure, mode)
    check_b1b(closure, mode)


# Un nom de fichier nu (sans dossier) est local s'il porte une extension de fichier de cette liste
# fermée ; un ticket, un commit, une version ou un identifiant opaque n'est pas un chemin et reste hors du contrôle d'existence.
LOCAL_FILE_EXTENSIONS = {
    "html", "htm", "css", "js", "mjs", "json", "md", "txt", "csv", "pdf", "xml",
    "png", "jpg", "jpeg", "gif", "webp", "avif", "svg", "ico", "mp4", "webm", "mov",
    "zip", "fig", "sketch", "psd", "ai", "pptx", "docx", "xlsx", "woff", "woff2", "ttf", "otf",
}
BARE_FILE = re.compile(r"^[^\s/\\:]+\.([A-Za-z0-9]+)$")


def is_local_locator(locator: str) -> bool:
    if locator.startswith("file://"):
        return True
    if re.match(r"^[a-z][a-z0-9+.-]*://", locator, re.I):
        return False
    if locator.startswith(("/", "./", "../")) or "/" in locator:
        return True
    bare = BARE_FILE.match(locator)
    return bool(bare and bare.group(1).lower() in LOCAL_FILE_EXTENSIONS)


def check_strict_contract(document: Any, source_path: Path) -> None:
    """Profil strict (INV-C4-2) : mêmes exigences par mode que le profil normal, plus trois contrôles :
    placeholders exacts, familles d'hôtes de démonstration, existence des locators locaux résolus depuis le dossier de la carte
    (artefact, trace et, si la paire B1b est faite, ses deux captures)."""
    exact_placeholders = {
        "lorem ipsum",
        "chemin-ou-url-local",
        "ticket-ou-chemin-de-run",
        "à définir",
        "a definir",
        "todo",
        "tbd",
        "placeholder",
    }
    placeholder_hosts = {"invalid", "example.com", "example.org", "example.net"}

    def walk(value: Any, path: str = "") -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                walk(child, f"{path}.{key}" if path else key)
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{path}[{index}]")
        elif isinstance(value, str):
            lowered = value.strip().lower()
            if lowered in exact_placeholders:
                raise ValidationError(f"strict : placeholder ou texte générique dans {path}")

    walk(document)
    card = document.get("run_card") if isinstance(document, dict) else None
    card = card if isinstance(card, dict) else {}
    artifact = card.get("artifact") if isinstance(card.get("artifact"), dict) else {}
    locators = [("artifact.locator", artifact.get("locator")), ("trace_locator", card.get("trace_locator"))]
    closure = card.get("closure") if isinstance(card.get("closure"), dict) else {}
    b1b = closure.get("b1b") if isinstance(closure.get("b1b"), dict) else {}
    pair = b1b.get("pair") if b1b.get("status") == "DONE" and isinstance(b1b.get("pair"), dict) else {}
    locators += [(f"closure.b1b.pair.{side}", pair.get(side)) for side in ("before_locator", "after_locator") if side in pair]
    kinds = {"artifact.locator": "artefact", "trace_locator": "trace",
             "closure.b1b.pair.before_locator": "capture B1b avant", "closure.b1b.pair.after_locator": "capture B1b après"}
    if not isinstance(artifact.get("locator"), str) or not artifact["locator"].strip():
        raise ValidationError("strict : artifact.locator doit être renseigné")
    base = source_path.resolve().parent  # dossier de la carte, quel que soit le dossier de lancement
    for label, locator in locators:
        if not isinstance(locator, str) or not locator.strip():
            continue  # l’exigence de trace suit le mode, comme en profil normal
        locator = locator.strip()
        try:
            parsed = urlparse(locator)
            host = (parsed.hostname or '').lower().rstrip('.')
        except ValueError as exc:
            raise ValidationError(f"strict : {label} illisible : {locator}") from exc
        if parsed.scheme.lower() in {"http", "https"} and any(host == domain or host.endswith('.' + domain) for domain in placeholder_hosts):
            raise ValidationError(f"strict : {label} URL de démonstration interdite : {locator}")
        if is_local_locator(locator):
            candidate = Path(locator.removeprefix("file://"))
            if not candidate.is_absolute():
                candidate = base / candidate
            if not candidate.exists():
                raise ValidationError(f"strict : {kinds[label]} local absent : {locator}")


def validate_card(document: Any, schema: dict[str, Any], strict: bool = False, source_path: Path | None = None) -> None:
    check_types(document, schema)
    check_held_message(document)
    # Donner priorité aux diagnostics métier lisibles avant les exigences
    # conditionnelles du schéma, sans relâcher la validation structurelle.
    check_semantic_contract(document)
    if strict:
        check_strict_contract(document, source_path or EXAMPLE)
    validate_node(document, schema)


def check_fixture(
    path: Path,
    schema: dict[str, Any],
    should_pass: bool,
    errors: list[str],
    expected_message: str | None = None,
) -> None:
    if not should_pass and not expected_message:
        errors.append(f"oracle sans motif — {path.relative_to(ROOT)} : un négatif doit déclarer son message attendu")
        return
    try:
        validate_card(load_json(path), schema)
    except ValidationError as exc:
        if should_pass:
            errors.append(f"fixture valide rejetée — {path.relative_to(ROOT)} : {exc}")
        elif expected_message not in str(exc):
            errors.append(
                f"diagnostic inattendu — {path.relative_to(ROOT)} : attendu {expected_message!r}, obtenu {str(exc)!r}"
            )
        return
    if not should_pass:
        errors.append(f"fixture invalide acceptée — {path.relative_to(ROOT)}")


# Table déclarative des fixtures (A2) : nom → None (valide) ou motif attendu, sous-chaîne
# stable du diagnostic existant. Tout fichier de schemas/fixtures/ doit y figurer, et
# toute entrée doit exister. Les négatifs restent des scénarios composites nommés.
FIXTURE_TABLE: dict[str, str | None] = {
    "valid_closed_return.json": None,
    "valid_direction_with_profile_decision.json": None,
    "valid_direction_exploratory_untransformed.json": None,
    "invalid_state_held.json": "HELD est un statut de direction, pas une valeur de state",
    "invalid_missing_proof.json": "un verdict accepté exige au moins une preuve observed",
    "invalid_empty_proof.json": "un verdict accepté exige au moins une preuve observed",
    "invalid_global_axis_verdict.json": "closure.verdict : valeur non canonique : PASS",
    "invalid_direction_missing_object.json": "DIRECTION exige un objet direction",
    "invalid_direction_missing_trace_locator.json": "DIRECTION exige trace_locator",
    "invalid_direction_missing_creative_close.json": "DIRECTION clôturée exige creative_close",
    "invalid_direction_missing_status.json": "DIRECTION décidée ou clôturée exige direction_status",
    "invalid_creative_close_missing_field.json": "creative_close exige le champ craft_detail",
    "invalid_profile_decision_missing_evidence.json": "profile_decision : champ obligatoire absent : evidence",
    "invalid_accepted_before_decision.json": "un verdict accepté exige state DECIDED ou CLOSED",
    "invalid_accepted_without_provenance.json": "un verdict accepté exige proof.provenance",
    "invalid_accepted_without_limitations.json": "verdict accepté exige une limitation non vide",
    "invalid_accepted_without_observed.json": "verdict accepté exige au moins une preuve observed",
    "invalid_fail_assumed_accepted.json": "issue bloquante ou FAIL-ASSUMED",
    "invalid_capability_available_without_basis.json": "capability_profile exige basis non vide",
    "invalid_capability_profile_missing_basis.json": "capability_profile exige basis non vide",
    "invalid_critical_without_protection.json": "un risque critical exige une critical_protection structurée",
    "invalid_critical_placeholder_protection.json": "critical_protection.control ne peut pas être un placeholder",
    "invalid_accepted_lost_in_build.json": "LOST-IN-BUILD ne peut pas produire un verdict accepté",
    "invalid_lite_missing_minimum.json": "run_card : champ obligatoire absent : risk",
    "invalid_direction_untransformed_anchor.json": "un verdict accepté exige transformation_status transformed",
}

DELETE = object()
RC = "run_card"
PROTECTION = {"control": "Contrôle nommé", "owner": "owner-nommé", "scope": "Scope nommé", "failure_action": "RETURNED", "evidence_locator": "preuve-nommée", "result": "PASS"}
CRITICAL = {"level": "critical", "statement": "Risque critique nommé", "critical_protection": PROTECTION}
FAIL_OBS = "Échec observé : contraste insuffisant sur la note secondaire (Gate A)."
OBSERVED = ["Hiérarchie et premier geste observés dans le viewport inspecté.", FAIL_OBS]
EXCEPTION = {"owner": "Owner produit", "scope": "Pilote interne", "impact": "Note secondaire moins lisible", "next_proof": "Mesure après correction",
             "review_date": "2026-10-09", "exit_condition": "Contraste conforme mesuré", "gate_axis": "Gate A / contraste",
             "failure_evidence": FAIL_OBS, "requested_by": "Owner produit (demande écrite)", "disposition": "DIFFUSÉ-LIMITÉ"}
SYSTEM_PACKAGE = {"impact": "Token utilisé par trois surfaces", "consumers": ["web/app", "mobile/ios"], "owner": "Owner système",
                  "migration": "Alias temporaire pendant deux versions", "rollback": "Restaurer la valeur précédente du token",
                  "non_regression": {"claim": "Aucun écart hors intention", "baseline": {"locator": "baselines/token/", "version": "V1.4.0", "state": "défaut, focus"}},
                  "changelog_ref": "CHANGELOG — token action"}
CL = (RC, "closure")
ACC = [(CL + ("verdict",), "ACCEPTED"), (CL + ("axes",), {"V": "PASS", "U": "PASS", "A": "PASS", "T": "PASS"})]
FA = [((RC, "proof", "observed"), OBSERVED), (CL + ("issue",), "FAIL-ASSUMED"), (CL + ("verdict",), "RETURN"), (CL + ("exception",), EXCEPTION)]
FAILED = [((RC, "risk"), {**CRITICAL, "critical_protection": {**PROTECTION, "result": "FAIL"}}), (CL + ("issue",), "RETURNED"), (CL + ("verdict",), "RETURN")]
SYSTEM = [((RC, "mode"), "SYSTÈME"), (CL + ("system_package",), SYSTEM_PACKAGE)]
HIGH_GEN = [((RC, "direction", "identity_stake"), "high"), ((RC, "anchors", 0, "type"), "generated"),
            ((RC, "direction", "calibration"), {"basis": "generated_only_reserved", "detail": "Calibration sur hypothèse générée seule, réservée."})]
NO_ANCHOR = [((RC, "anchors"), []), (CL + ("issue",), "EXPLORATORY"), (CL + ("verdict",), "EXPLORATORY"), (CL + ("direction_status",), "PARTIALLY-HELD")]
INTAKE = [(CL + ("state",), "INTAKE"), (CL + ("verdict",), None), ((RC, "creative_close"), DELETE), ((RC, "decision_change"), DELETE)]
RECLASSIFIED = [(CL + ("issue",), "RECLASSIFIED"), (CL + ("verdict",), "RETURN"), (CL + ("reclassification",), {"to_mode": "STANDARD", "successor_run_ref": "run-043"})]
NORMAL = ((RC, "risk"), {"level": "normal", "statement": "Troncature du libellé sur mobile", "critical_protection": None})
ITER = [NORMAL, ((RC, "mode"), "ITER"), ((RC, "direction"), {"thesis": "La hiérarchie existante est conservée."})]
BUILDING = [NORMAL, (CL + ("state",), "BUILDING"), (CL + ("verdict",), None), (CL + ("issue",), None), ((RC, "decision_change"), DELETE)]
STRICT_LITE = [NORMAL, ((RC, "mode"), "LITE"), ((RC, "trace_locator"), DELETE), ((RC, "artifact", "locator"), str(EXAMPLE))]
RETURNED = FIXTURES / "valid_closed_return.json"
PROFILE = FIXTURES / "valid_direction_with_profile_decision.json"
# Cas unitaires à faute unique (A2) : base valide (vérifiée d'abord), éventuelles retouches
# qui gardent la base valide, UNE faute, motif attendu. Tout invariant ajouté arrive ici.
UNIT_CASES: list[tuple[Any, ...]] = [
    ("U-01", EXAMPLE, [], ((RC, "closure", "state"), "HELD"), "HELD est un statut de direction"),
    ("U-02", EXAMPLE, [], ((RC, "proof"), DELETE), "un verdict accepté exige au moins une preuve observed"),
    ("U-03", FIXTURES / "valid_closed_return.json", [], ((RC, "proof"), DELETE), "run_card : champ obligatoire absent : proof"),
    ("U-04", EXAMPLE, [], ((RC, "proof", "observed"), []), "un verdict accepté exige au moins une preuve observed"),
    ("U-05", EXAMPLE, [], ((RC, "closure", "verdict"), "PASS"), "closure.verdict : valeur non canonique : PASS"),
    ("U-06", EXAMPLE, [], ((RC, "direction"), DELETE), "DIRECTION exige un objet direction"),
    ("U-07", EXAMPLE, [], ((RC, "trace_locator"), DELETE), "DIRECTION exige trace_locator"),
    ("U-08", EXAMPLE, [], ((RC, "creative_close"), DELETE), "DIRECTION clôturée exige creative_close"),
    ("U-09", EXAMPLE, [], ((RC, "closure", "direction_status"), DELETE), "DIRECTION décidée ou clôturée exige direction_status"),
    ("U-10", EXAMPLE, [], ((RC, "creative_close", "craft_detail"), DELETE), "creative_close exige le champ craft_detail"),
    ("U-11", FIXTURES / "valid_direction_with_profile_decision.json", [], ((RC, "profile_decision", "evidence"), DELETE), "profile_decision : champ obligatoire absent : evidence"),
    ("U-12", EXAMPLE, [], ((RC, "closure", "state"), "CHECKING"), "un verdict accepté exige state DECIDED ou CLOSED"),
    ("U-13", EXAMPLE, [], ((RC, "proof", "provenance"), DELETE), "un verdict accepté exige proof.provenance"),
    ("U-14", EXAMPLE, [], ((RC, "closure", "limitations"), []), "verdict accepté exige une limitation non vide"),
    ("U-15", EXAMPLE, [((RC, "proof", "observed"), OBSERVED), (CL + ("exception",), EXCEPTION)], ((RC, "closure", "issue"), "FAIL-ASSUMED"), "issue bloquante ou FAIL-ASSUMED"),
    ("U-16", EXAMPLE, [], ((RC, "closure", "issue"), "BLOCKED"), "issue bloquante ou FAIL-ASSUMED"),
    ("U-17", EXAMPLE, [], ((RC, "capability_profile", "basis"), []), "capability_profile exige basis non vide"),
    ("U-18", EXAMPLE, [], ((RC, "capability_profile", "basis"), DELETE), "capability_profile exige basis non vide"),
    ("U-19", EXAMPLE, [], ((RC, "risk", "level"), "critical"), "un risque critical exige une critical_protection structurée"),
    ("U-20", EXAMPLE, [((RC, "risk"), CRITICAL)], ((RC, "risk", "critical_protection", "control"), "TODO"), "critical_protection.control ne peut pas être un placeholder"),
    ("U-21", EXAMPLE, [], ((RC, "closure", "direction_status"), "LOST-IN-BUILD"), "LOST-IN-BUILD ne peut pas produire un verdict accepté"),
    ("U-22", FIXTURES / "valid_closed_return.json", [], ((RC, "risk"), DELETE), "run_card : champ obligatoire absent : risk"),
    ("U-23", EXAMPLE, [], ((RC, "anchors", 0, "transformation_status"), "not_transformed"), "un verdict accepté exige transformation_status transformed"),
    # Invariants nouveaux de la migration (12.04), un cas chacun (règle A2)
    ("B1-1", EXAMPLE, [((RC, "risk"), CRITICAL)], ((RC, "mode"), "LITE"), "risque critical interdit le mode LITE ou ITER"),
    ("B1-2", EXAMPLE, [((RC, "risk"), CRITICAL)], ((RC, "risk", "critical_protection", "result"), DELETE), "critical_protection exige result"),
    ("B1-3a", EXAMPLE, [((RC, "risk"), {**CRITICAL, "critical_protection": {**PROTECTION, "result": "NOT-VERIFIED"}})], (CL + ("verdict",), "ACCEPTED"), "verdict ACCEPTED interdit"),
    ("B1-3b", EXAMPLE, FAILED, (CL + ("verdict",), "ACCEPTED-WITH-RESERVATION"), "protection critique en échec"),
    ("B1-3c", EXAMPLE, FAILED, (CL + ("issue",), "BLOCKED"), "issue doit suivre critical_protection.failure_action"),
    ("B1-4", EXAMPLE, FA, (CL + ("exception",), DELETE), "FAIL-ASSUMED exige closure.exception"),
    ("B1-5", EXAMPLE, FA, (CL + ("exception", "failure_evidence"), "Échec non observé"), "failure_evidence doit figurer dans proof.observed"),
    ("B1-6", EXAMPLE, FA, (CL + ("exception", "disposition"), DELETE), "exception exige disposition"),
    ("B2-1", EXAMPLE, [], (CL + ("issue",), "RETURNED"), "issue non nulle interdit un verdict accepté"),
    ("B2-2", EXAMPLE, ACC, (CL + ("direction_status",), "PARTIALLY-HELD"), "PARTIALLY-HELD interdit ACCEPTED"),
    ("B2-3a", EXAMPLE, [], (CL + ("axes",), DELETE), "verdict accepté exige closure.axes"),
    ("B2-3b", EXAMPLE, [], (CL + ("axes", "U"), "RETURN"), "axe RETURN interdit un verdict accepté"),
    ("B2-3c", EXAMPLE, ACC, (CL + ("axes", "A"), "NOT-VERIFIED"), "axe NOT-VERIFIED interdit ACCEPTED"),
    ("B2-3d", EXAMPLE, ACC, (CL + ("axes", "V"), "PASS-WITH-RESERVATION"), "réserve d'axe interdit ACCEPTED"),
    ("B2-4", EXAMPLE, [], ((RC, "proof", "provenance", "capability"), "clavier/AT non exécuté"), "provenance.capability doit être disponible"),
    ("B2-5", EXAMPLE, [], ((RC, "capability_profile"), DELETE), "un verdict accepté exige capability_profile"),
    ("B2-6", EXAMPLE, [], ((RC, "capability_profile", "basis", 1, "kind"), "unattested_declaration"), "basis déclarative"),
    ("B2-7", EXAMPLE, [], ((RC, "artifact", "version"), "2026-09-25 / V2"), "version de preuve différente de la version d'artefact"),
    ("B2-8", EXAMPLE, [], ((RC, "proof", "provenance", "observed_at"), "hier"), "observed_at doit être une date ISO"),
    ("B2-9a", EXAMPLE, [], (CL + ("reservations",), DELETE), "ACCEPTED-WITH-RESERVATION exige closure.reservations"),
    ("B2-9b", EXAMPLE, [], (CL + ("reservations", 0, "impact"), "à compléter"), "réserve incomplète ou placeholder"),
    ("B2-10a", EXAMPLE, ACC, ((RC, "artifact", "rights_status"), "unknown"), "droits inconnus interdisent ACCEPTED"),
    ("B2-10b", EXAMPLE, [], ((RC, "artifact", "rights_status"), DELETE), "DIRECTION exige artifact.rights_status"),
    ("B3-1a", EXAMPLE, SYSTEM, (CL + ("system_package",), DELETE), "SYSTÈME accepté exige closure.system_package"),
    ("B3-1b", EXAMPLE, SYSTEM, (CL + ("system_package", "consumers"), []), "system_package exige au moins un consumer"),
    ("B3-1c", EXAMPLE, SYSTEM, (CL + ("system_package", "rollback"), "à déterminer"), "system_package incomplet ou placeholder"),
    ("B3-2", EXAMPLE, SYSTEM, (CL + ("system_package", "non_regression", "baseline", "version"), DELETE), "baseline exige locator, version et état"),
    ("B3-3a", EXAMPLE, [], (CL + ("b1b",), DELETE), "exige closure.b1b"),
    ("B3-3b", EXAMPLE, [], (CL + ("b1b", "pair", "after_locator"), "captures/premiere-scene-v1.png"), "paire B1b : captures distinctes"),
    ("B3-4a", EXAMPLE, [], (CL + ("b1b",), {"status": "N/A-JUSTIFIED", "reason": "comparaison inutile", "covered_decision": "d", "owner": "o", "next_proof": "p"}), "motif N/A B1b non recevable"),
    ("B3-4b", EXAMPLE, [], (CL + ("b1b",), {"status": "N/A-JUSTIFIED", "reason": "equivalent_pair_valid", "covered_decision": "Relief porteur", "owner": "Owner", "next_proof": "Capture V2"}), "exige pair_ref"),
    ("B4-1", EXAMPLE, [], ((RC, "anchors", 0, "type"), DELETE), "ancrage exige type"),
    ("B4-2", EXAMPLE, [], ((RC, "anchors", 0, "date"), "récemment"), "date d'ancrage ISO"),
    ("B4-3", EXAMPLE, [], ((RC, "direction", "identity_stake"), DELETE), "DIRECTION exige direction.identity_stake"),
    ("B4-4a", EXAMPLE, HIGH_GEN, ((RC, "direction", "calibration"), DELETE), "ancrage généré seul exige calibration"),
    ("B4-4b", EXAMPLE, HIGH_GEN, ((RC, "direction", "calibration", "basis"), "independent_review"), "base de calibration non recevable"),
    ("B4-5", EXAMPLE, HIGH_GEN + ACC[1:], (CL + ("verdict",), "ACCEPTED"), "calibration générée seule interdit ACCEPTED"),
    ("B4-6a", EXAMPLE, [], ((RC, "anchors"), []), "DIRECTION sans ancrage : verdict accepté interdit"),
    ("B4-6b", EXAMPLE, NO_ANCHOR, (CL + ("issue",), None), "DIRECTION sans ancrage exige une issue"),
    ("C1-1a", EXAMPLE, [], ((RC, "decision_change", "outcome"), DELETE), "decision_change exige outcome"),
    ("C1-1b", EXAMPLE, [], ((RC, "decision_change", "outcome"), "N/A-JUSTIFIED"), "N/A-JUSTIFIED exige une raison"),
    ("C1-2", EXAMPLE, ACC, ((RC, "decision_change", "outcome"), "NOT-OBSERVED"), "NOT-OBSERVED interdit ACCEPTED"),
    ("C1-3", EXAMPLE, [((RC, "mode"), "STANDARD")], ((RC, "decision_change"), DELETE), "exige decision_change"),
    ("C1-4a", EXAMPLE, INTAKE, (CL + ("verdict",), "RETURN"), "le verdict doit rester null avant CHECKING"),
    ("C1-4b", EXAMPLE, [], (CL + ("verdict",), None), "exige un verdict"),
    ("C1-5a", EXAMPLE, RECLASSIFIED, (CL + ("reclassification",), DELETE), "RECLASSIFIED exige closure.reclassification"),
    ("C1-5b", EXAMPLE, RECLASSIFIED, (CL + ("reclassification", "to_mode"), "DIRECTION"), "mode cible identique"),
    ("C1-6", PROFILE, [], ((RC, "profile_decision", "phase"), "intended"), "profil non observé"),
    ("C2-1", EXAMPLE, [], ((RC, "risk", "statement"), "TBD"), "risk.statement requis"),
    ("C4-1", RETURNED, ITER, ((RC, "trace_locator"), DELETE), "ITER exige trace_locator"),
    ("C4-2", RETURNED, STRICT_LITE, ((RC, "artifact", "locator"), "captures/absent.png"), "artefact local absent", True),
    ("D2-1", RETURNED, BUILDING, ((RC, "decision_change"), {"outcome": "CHANGED", "value": "Conséquence déclarée", "evidence": "Aucune"}), "avant observation"),
    ("D2-2", RETURNED, ITER, ((RC, "direction"), DELETE), "rappel de direction"),
    # Cas négatifs : une règle, un cas.
    ("N1", EXAMPLE, [], ((RC, "proof", "provenance", "artifact_locator"), "autre-chemin-local"), "artifact_locator doit correspondre à artifact.locator"),
    ("N2", EXAMPLE, [], ((RC, "proof", "not_verified"), ["Hiérarchie et premier geste observés dans le viewport inspecté."]), "ne peuvent pas contenir le même claim"),
    ("N3", EXAMPLE, [((RC, "risk"), CRITICAL)], ((RC, "risk", "critical_protection", "failure_action"), "CONTINUE"), "failure_action doit retourner, bloquer ou escalader"),
    ("N4a", EXAMPLE, [((RC, "risk"), CRITICAL)], ((RC, "risk", "critical_protection", "owner"), DELETE), "critical_protection exige le champ owner"),
    ("N4b", EXAMPLE, [((RC, "risk"), CRITICAL)], ((RC, "risk", "critical_protection", "evidence_locator"), DELETE), "critical_protection exige le champ evidence_locator"),
    ("N5", EXAMPLE, [], ((RC, "proof", "provenance", "method"), DELETE), "proof.provenance exige le champ method"),
    # Heure ou fuseau impossibles ; issue d'un autre type que ses valeurs d'enum.
    ("C19-1", EXAMPLE, [], ((RC, "proof", "provenance", "observed_at"), "2026-08-29T25:61"), "observed_at doit être une date ISO"),
    ("C19-2", EXAMPLE, [], ((RC, "proof", "provenance", "observed_at"), "2026-08-29T10:00+25:00"), "observed_at doit être une date ISO"),
    ("C20-1", EXAMPLE, [], (CL + ("issue",), []), "type attendu null, string (valeurs de l’enum)"),
    # Un nom de fichier nu absent est refusé en profil strict, pour l'artefact comme pour la trace.
    ("C02-1", RETURNED, STRICT_LITE, ((RC, "artifact", "locator"), "absent.html"), "artefact local absent", True),
    ("C02-2", RETURNED, STRICT_LITE + [((RC, "trace_locator"), str(EXAMPLE))], ((RC, "trace_locator"), "trace-absente.md"),
     "trace local absent", True),
]

# Locators que le profil strict admet (aucun refus involontaire). Chaque valeur remplace
# trace_locator d'une carte LITE stricte valide ; les chemins relatifs se résolvent depuis le dossier de la carte.
STRICT_ADMITTED = [
    ("fichier nu présent", "run_card.example.json"),
    ("chemin relatif présent", "./run_card.example.json"),
    ("URL", "https://atelier.exemple.cm/runs/42"),
    ("ticket", "JIRA-142"),
    ("numéro de ticket", "#128"),
    ("commit", "1a4bf2f664a17be95ab9c0303a9e2b5a6803b250"),
    ("commit court", "1a4bf2f"),
    ("version", "v1.0.0"),
    ("identifiant opaque", "run-2026-10-01.a"),
    ("domaine sans schéma", "atelier.exemple.cm"),
]


def apply_edit(document: Any, path: tuple[Any, ...], value: Any) -> None:
    node = document
    for key in path[:-1]:
        node = node[key]
    if value is DELETE:
        del node[path[-1]]
    else:
        node[path[-1]] = json.loads(json.dumps(value))


def check_unit_cases(schema: dict[str, Any], errors: list[str]) -> None:
    passed = 0
    for case_id, base, edits, (fault_path, fault_value), motif, *options in UNIT_CASES:
        strict = bool(options and options[0])
        try:
            document = load_json(base)
            for path, value in edits:
                apply_edit(document, path, value)
        except (KeyError, IndexError, TypeError, ValidationError) as exc:
            errors.append(f"cas unitaire {case_id} : base illisible ({exc})")
            continue
        try:
            validate_card(document, schema, strict=strict, source_path=EXAMPLE)
        except ValidationError as exc:
            errors.append(f"cas unitaire {case_id} : base invalide ({exc})")
            continue
        try:
            apply_edit(document, fault_path, fault_value)
        except (KeyError, IndexError, TypeError) as exc:
            errors.append(f"cas unitaire {case_id} : chemin de faute introuvable ({exc})")
            continue
        try:
            validate_card(document, schema, strict=strict, source_path=EXAMPLE)
        except ValidationError as exc:
            if motif in str(exc):
                passed += 1
            else:
                errors.append(f"cas unitaire {case_id} : attendu {motif!r}, obtenu {str(exc)!r}")
            continue
        errors.append(f"cas unitaire {case_id} : faute unique acceptée ({motif})")
    print(f"+ cas unitaires : {passed}/{len(UNIT_CASES)}")


def check_schema_keyword_witness(schema: dict[str, Any], errors: list[str]) -> None:
    """Un mot-clé non pris en charge (pattern ajouté à run_card.id) est refusé."""
    witness = json.loads(json.dumps(schema))
    witness["properties"]["run_card"]["properties"]["id"]["pattern"] = "^RUN-"
    try:
        check_schema_keywords(witness)
    except ValidationError:
        print("+ mot-clé de schéma non pris en charge refusé : 1/1")
        return
    errors.append("témoin C13 : un mot-clé de schéma non pris en charge est ignoré")


def check_strict_admitted(schema: dict[str, Any], errors: list[str]) -> None:
    passed = 0
    for label, locator in STRICT_ADMITTED:
        try:
            document = load_json(RETURNED)
            for path, value in STRICT_LITE + [((RC, "trace_locator"), locator)]:
                apply_edit(document, path, value)
            validate_card(document, schema, strict=True, source_path=EXAMPLE)
        except (KeyError, IndexError, TypeError, ValidationError) as exc:
            errors.append(f"locator strict admis refusé ({label}, « {locator} ») : {exc}")
            continue
        passed += 1
    print(f"+ locators admis en profil strict : {passed}/{len(STRICT_ADMITTED)}")


def check_fixture_table(schema: dict[str, Any], errors: list[str]) -> None:
    present = {path.name for path in FIXTURES.glob("*.json")}
    for name in sorted(present - set(FIXTURE_TABLE)):
        errors.append(f"fixture non déclarée : schemas/fixtures/{name}")
    for name in sorted(set(FIXTURE_TABLE) - present):
        errors.append(f"fixture déclarée absente : schemas/fixtures/{name}")
    before = len(errors)
    for name, motif in FIXTURE_TABLE.items():
        if name in present:
            check_fixture(FIXTURES / name, schema, motif is None, errors, expected_message=motif)
    checked = len(present & set(FIXTURE_TABLE))
    print(f"+ fixtures déclarées : {checked - (len(errors) - before)}/{len(FIXTURE_TABLE)}")


def check_schema_authority(schema: dict[str, Any], errors: list[str]) -> None:
    """Régression : une modification d’enum dans le schéma doit modifier le résultat."""
    document = load_json(EXAMPLE)
    altered_schema = json.loads(json.dumps(schema))
    altered_schema["properties"]["run_card"]["properties"]["mode"]["enum"] = ["SCHEMA-DRIVEN-TEST"]
    document["run_card"]["mode"] = "SCHEMA-DRIVEN-TEST"
    try:
        validate_card(document, altered_schema)
    except ValidationError as exc:
        errors.append(f"le validateur n’utilise pas l’enum du schéma : {exc}")


SCHEMA_WITNESS_MODE = "SCHEMA-WITNESS-INVALID-MODE"


def load_schema() -> dict[str, Any]:
    """Chargement gouverné : aucun PASS n’est possible avec un schéma absent, vide ou incomplet."""
    if not SCHEMA.is_file():
        raise ValidationError("schéma absent : schemas/run_card.schema.json")
    schema = load_json(SCHEMA)
    if not isinstance(schema, dict) or not schema:
        raise ValidationError("schéma inopérant : la racine doit être un objet non vide")
    node: Any = schema
    for key in ("properties", "run_card", "properties", "mode", "enum"):
        node = node.get(key) if isinstance(node, dict) else None
    if not isinstance(node, list) or not node:
        raise ValidationError("schéma incomplet : properties.run_card.properties.mode.enum absent ou vide")
    check_schema_keywords(schema)
    return schema


# Le sous-ensemble de JSON Schema réellement interprété par validate_node. Un mot-clé hors de
# cette liste serait ignoré en silence ; il est donc refusé avant toute validation. Les annotations restent admises.
SCHEMA_KEYWORDS = {"type", "enum", "const", "required", "properties", "additionalProperties", "items", "minLength",
                   "minItems", "allOf", "anyOf", "if", "then"}
SCHEMA_ANNOTATIONS = {"$schema", "$id", "$comment", "title", "description", "default", "examples"}


def check_schema_keywords(schema: Any, path: str = "$") -> None:
    if not isinstance(schema, dict):
        raise ValidationError(f"schéma : sous-schéma non objet à {path}")
    unknown = sorted(set(schema) - SCHEMA_KEYWORDS - SCHEMA_ANNOTATIONS)
    if unknown:
        raise ValidationError(f"schéma : mot-clé non pris en charge à {path} : {', '.join(unknown)}")
    properties = schema.get("properties", {})
    if not isinstance(properties, dict):
        raise ValidationError(f"schéma : properties doit être un objet à {path}")
    for key, child in properties.items():
        check_schema_keywords(child, f"{path}.properties.{key}")
    for key in ("items", "if", "then"):
        if key in schema:
            check_schema_keywords(schema[key], f"{path}.{key}")
    for key in ("allOf", "anyOf"):
        if key in schema:
            if not isinstance(schema[key], list):
                raise ValidationError(f"schéma : {key} doit être une liste à {path}")
            for index, child in enumerate(schema[key]):
                check_schema_keywords(child, f"{path}.{key}[{index}]")


def check_schema_witness(schema: dict[str, Any]) -> None:
    """Témoin négatif avant tout PASS : un mode inventé doit être rejeté par le schéma seul."""
    document = load_json(EXAMPLE)
    if not isinstance(document, dict) or not isinstance(document.get("run_card"), dict):
        raise ValidationError("témoin de schéma impossible : exemple canonique sans objet run_card")
    document["run_card"]["mode"] = SCHEMA_WITNESS_MODE
    try:
        validate_node(document, schema)
    except ValidationError as exc:
        if "run_card.mode" in str(exc):
            return
        raise ValidationError(f"témoin de schéma non concluant : rejet pour un autre motif que le mode ({exc})") from exc
    raise ValidationError("le schéma n’impose pas l’enum de mode")


def validate_single_path(path: Path, schema: dict[str, Any], strict: bool = False) -> int:
    """Valide uniquement le fichier demandé par l’utilisateur ou un pipeline."""
    try:
        validate_card(load_json(path), schema, strict=strict, source_path=path)
    except (OSError, ValidationError) as exc:
        print("RUN_CARD VALIDATION FAILED")
        print(f"- {exc}")
        return 1
    print(f"RUN_CARD VALIDATION PASSED — fichier ciblé : {path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Valide la projection RUN_CARD ou la suite intégrée de fixtures."
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        help="fichier JSON à valider seul ; sans argument, exécute la suite complète",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="rejette les placeholders et vérifie les locators d’artefacts locaux ; nécessite un chemin JSON",
    )
    args = parser.parse_args(argv)
    errors: list[str] = []
    if args.strict and args.path is None:
        print("RUN_CARD VALIDATION FAILED")
        print("- --strict exige un fichier JSON ciblé")
        return 1
    # Avant toute branche, suite ou ciblée : schéma opérant et témoin négatif rejeté.
    try:
        schema = load_schema()
        check_schema_witness(schema)
    except ValidationError as exc:
        print("RUN_CARD VALIDATION FAILED")
        print(f"- {exc}")
        return 1
    # Une demande ciblée ne retombe jamais sur la suite.
    if args.path is not None:
        path = args.path.expanduser()
        if not path.is_absolute():
            path = Path.cwd() / path
        return validate_single_path(path.resolve(), schema, strict=args.strict)

    # Suite intégrée : le schéma est garanti opérant par le chargement gouverné.
    check_fixture(EXAMPLE, schema, True, errors)
    check_fixture_table(schema, errors)
    check_unit_cases(schema, errors)
    check_strict_admitted(schema, errors)
    check_schema_keyword_witness(schema, errors)
    check_schema_authority(schema, errors)

    if errors:
        print("RUN_CARD VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RUN_CARD VALIDATION PASSED — projection validée contre le schéma et fixtures contrôlés")
    return 0


if __name__ == "__main__":
    sys.exit(main())
