#!/usr/bin/env python3
"""Consolide des observations ; ne transforme pas des essais manquants en résultats."""
import json
from datetime import datetime
from pathlib import Path

root = Path(__file__).resolve().parent
protocol = json.loads((root / "protocole.json").read_text())
events = [json.loads(line) for line in (root / "execution.jsonl").read_text().splitlines()]
metrics = json.loads((root / "lecture-mesuree.json").read_text()) if (root / "lecture-mesuree.json").exists() else {}
state = json.loads((root / "etat-execution.json").read_text())
interruptions = json.loads((root / "interruptions.json").read_text()) if (root / "interruptions.json").exists() else {}
starts, ends = {}, {}
for event in events:
    name = event.get("name", event.get("run"))
    if event["event"] in {"start", "user_selected_separate_agents_and_blind_judges"}:
        starts[name] = event["time"]
    elif event["event"] == "complete":
        ends[name] = event["time"]
cases = []
for case in protocol["cases"]:
    run = case["run"]
    folder = root / "runs" / run
    result = {"run": run, "condition": case["condition"], "brief": case["brief_id"],
              "repeat": case["repeat"], "label": case["anonymous_label"],
              "status": "completed" if run in ends else "running" if run in starts else "prepared"}
    result["wall_measurement_status"] = "observed"
    if run in interruptions:
        result["interruption"] = interruptions[run]
        result["wall_measurement_status"] = interruptions[run]["wall_measurement_status"]
    if run in starts and run in ends:
        seconds = (datetime.fromisoformat(ends[run]) - datetime.fromisoformat(starts[run])).total_seconds()
        result["wall_seconds"] = seconds
        result["over_20_minutes"] = seconds > 1200
    if run in metrics:
        result["reading"] = metrics[run]
    functional = folder / "parcours-coordinateur.json"
    if functional.exists():
        report = json.loads(functional.read_text())
        result["functional"] = {k: report[k] for k in ["passed", "failed", "source_unchanged"]}
    audit = folder / "audit-final" / "observations.json"
    if audit.exists():
        report = json.loads(audit.read_text())
        result["automatic_observations"] = {
            "source_unchanged": report["source_unchanged"],
            "overflow_widths": [v["width"] for v in report["viewports"] if v["horizontal_overflow"]],
            "script_errors": sum(len(v["events"]["page_errors"]) for v in report["viewports"]),
            "external_requests": sum(len(v["events"]["external_requests"]) for v in report["viewports"]),
        }
    cases.append(result)
comparisons = []
for left, right in [("run-01", "run-02"), ("run-04", "run-03"), ("run-06", "run-05")]:
    a, b = next(c for c in cases if c["run"] == left), next(c for c in cases if c["run"] == right)
    compared = {"before": left, "after": right, "status": "pending"}
    if a["status"] == b["status"] == "completed" and "reading" in a and "reading" in b:
        compared["status"] = "measured"
        for name, av, bv in [
            ("wall_seconds", a["wall_seconds"], b["wall_seconds"]),
            ("unique_chars_per_request_key", a["reading"]["unique_chars_per_request_key"], b["reading"]["unique_chars_per_request_key"]),
            ("chars_served_with_repetitions", a["reading"]["chars_served_with_repetitions"], b["reading"]["chars_served_with_repetitions"]),
        ]:
            compared[name] = {"before": av, "after": bv, "change_percent": round((bv / av - 1) * 100, 2) if av else None}
            if name == "wall_seconds" and (a["wall_measurement_status"] != "observed" or b["wall_measurement_status"] != "observed"):
                compared[name]["change_percent"] = None
                compared[name]["status"] = "NOT-COMPARABLE: interruption d’usage et pause du coordinateur incluses"
    comparisons.append(compared)
bilan = {
    "cases": cases, "comparisons": comparisons,
    "api_tokens": "NOT-MEASURED",
    "owner_judgement": state["owner_judgement"],
    "general_effect": "NOT-VERIFIED",
    "limitations": [
        "Six pages et deux briefs : comparaison descriptive, sans significativité ni effet général établi.",
        "Même modèle hérité ; service exact et graines internes non attestés.",
        "Caractères servis par le lecteur seulement, en-têtes compris, pas tout le contexte du modèle.",
        "Union par clé de requête, pas déduplication sémantique de textes issus de routes différentes.",
        "Avant premier index.html ne signifie pas avant toute préparation ou production.",
        "Durée mesurée à réception de la fin, outils et attente de service compris ; contrôles parent exclus.",
        "Critères de goût R1 à R4 et R9 réservés au propriétaire.",
    ],
}
(root / "bilan-observe.json").write_text(json.dumps(bilan, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"completed": sum(c["status"] == "completed" for c in cases), "measured_pairs": sum(c["status"] == "measured" for c in comparisons), "api_tokens": "NOT-MEASURED"}))
