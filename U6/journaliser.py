#!/usr/bin/env python3
"""Journal du coordinateur, distinct du protocole figé et des traces de lecture."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("event", choices=["start", "complete", "audit", "judge_start", "judge_complete", "intervention", "owner_judgement"])
parser.add_argument("name")
parser.add_argument("--agent")
parser.add_argument("--note", default="")
args = parser.parse_args()
record = {"time": datetime.now(timezone.utc).isoformat(), "event": args.event,
          "name": args.name, "agent": args.agent, "note": args.note}
path = Path(__file__).resolve().parent / "execution.jsonl"
with path.open("a") as stream:
    stream.write(json.dumps(record, ensure_ascii=False) + "\n")
records = [json.loads(line) for line in path.read_text().splitlines()]
started, completed, audited, judges = set(), set(), set(), {}
owner = "pending"
for item in records:
    event, name = item["event"], item.get("name", item.get("run"))
    if event in {"start", "user_selected_separate_agents_and_blind_judges"}:
        started.add(name)
    elif event == "complete":
        completed.add(name)
    elif event == "audit":
        audited.add(name)
    elif event in {"judge_start", "judge_complete"}:
        judges[name] = event
    elif event == "owner_judgement":
        owner = {"status": "received", "time": item["time"], "answer": item.get("note", "")}
state = {"updated_at": record["time"], "selection": "separate_agents_and_blind_judges",
         "generation_started": True, "running": sorted(started - completed),
         "productions_completed": sorted(completed), "audits_completed": sorted(audited),
         "judges": judges, "owner_judgement": owner}
(path.parent / "etat-execution.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(record, ensure_ascii=False))
