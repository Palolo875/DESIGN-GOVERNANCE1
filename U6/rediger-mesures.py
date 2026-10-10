#!/usr/bin/env python3
"""Tableaux descriptifs à partir des relevés ; pas d'inférence ni de jetons estimés."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
bilan = json.loads((root / "bilan-observe.json").read_text())
if any(c["status"] != "completed" or "functional" not in c for c in bilan["cases"]):
    raise SystemExit("Les six productions et parcours sont nécessaires au tableau final.")
target = root / "mesures.md"
if target.exists():
    raise SystemExit("Tableau existant : ne pas écraser une preuve.")

def integer(value):
    return f"{value:,}".replace(",", " ")

lines = ["# Mesures U6", "", "Six productions distinctes ; chiffres descriptifs, sans significativité ni effet général établi.", "",
         "| Page | Version | Brief | Minutes observées | Caractères servis | Union par clé | Parcours du coordinateur |",
         "|---|---|---|---:|---:|---:|---|"]
for case in bilan["cases"]:
    r, f = case["reading"], case["functional"]
    duration = f"{case['wall_seconds']/60:.1f}".replace(".", ",")
    if case["wall_measurement_status"] != "observed":
        duration += " (interruption ; non comparable)"
    lines.append(f"| {case['label']} | {case['condition']} | {case['brief']}, répétition {case['repeat']} | {duration} | {integer(r['chars_served_with_repetitions'])} | {integer(r['unique_chars_per_request_key'])} | {f['passed']} PASS, {f['failed']} FAIL |")
lines.extend(["", "Le nombre de contrôles dépend du parcours implémenté ; il n'est pas une note comparative de qualité. Les échecs bruts restent comptés même si une copie est corrigée ensuite.", "",
              "| Paire avant → après | Variation du temps | Variation de l'union de caractères | Variation des caractères servis avec répétitions |",
              "|---|---:|---:|---:|"])
for pair in bilan["comparisons"]:
    labels = {c["run"]:c["label"] for c in bilan["cases"]}
    changes = [f"{pair[k]['change_percent']:+.1f} %".replace(".", ",") if pair[k]['change_percent'] is not None else "non comparable (interruption)" for k in ["wall_seconds", "unique_chars_per_request_key", "chars_served_with_repetitions"]]
    lines.append(f"| {labels[pair['before']]} → {labels[pair['after']]} | {' | '.join(changes)} |")
lines.extend(["", "Les caractères décrivent les textes servis par le lecteur DG, en-têtes inclus. L'union est calculée par clé de requête : elle ne supprime pas les recouvrements sémantiques entre des routes différentes. Les lectures techniques directes et les autres instructions ne sont pas comptées. Aucun compteur de jetons API n'est disponible.", "",
              "Le repère avant premier HTML utilise l'existence de `index.html` ; il ne date pas toute la préparation ou le début effectif de la production. Les cibles initiales de lecture restent non validées par cette mesure. La durée part du dernier marqueur valide du coordinateur et termine à réception de la livraison, outils et attente de service compris, contrôles du coordinateur exclus.", "",
              "Le défaut observé sur une page n'établit pas une disparition de règle ou une régression causée par la refonte. La validation stricte de RUN_CARD vérifie sa structure ; les parcours doivent être exécutés séparément.", ""])
target.write_text("\n".join(lines))
print(str(target))
