#!/usr/bin/env python3
"""Valide la carte de lecture et les façades, sans créer d’autorité.

Deux contrôles :
1. carte : table des locators (unicité, propriétaire, correspondance, résolution),
   couverture de tout locator cité, unicité des titres porteurs d’un locator ;
   la résolution est celle de read_route.py (un seul résolveur) ;
2. façades : liste close des conditions de façade (LCF). Chaque entrée nomme une
   façade, la condition du propriétaire qu’elle doit conserver et sa source. Une
   entrée n’entre que par une décision écrite, avec sa mutation rouge.
Limite déclarée : une contradiction nouvelle hors de la LCF n’est pas détectée ;
la revue bornée des façades avant release la complète.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # l’import du résolveur ne doit rien écrire dans le package
sys.path.insert(0, str(Path(__file__).resolve().parent))
import read_route as rr  # noqa: E402

ROOT = rr.ROOT
OFFICIAL = rr.OFFICIAL
MAP = OFFICIAL / "READING_MAP.md"
SKILL_DIR = ROOT / "skills" / "design-governance-practice" if (ROOT / "skills").is_dir() else ROOT / "skill"
REQUIRED = (
    "Statut :** guide dérivé non normatif",
    "## Chemin canonique de démarrage",
    "## Routage minimal par décision",
    "## Activation multi-perspective",
    "## Handoff minimal commun",
    "## Résolution des routes",
    "## Locators principaux",
    "DIRECTION/START",
    "ACTION/RUN-LITE",
    "ACTION/CLOSE-EXIT-CHECK",
    "SAVOIR/ROUTING",
    "BIBLIOTHEQUE/SELECT",
    "## Condition d’arrêt",
    "N/A-JUSTIFIED",
    "NOT-VERIFIED",
)
OWNER_MAP = {f"{prefix}/*": OFFICIAL / f"{prefix}.md" for prefix in rr.PREFIXES}
CITED = re.compile(rf"`((?:{'|'.join(rr.PREFIXES)})/[A-Z0-9_\-]+(?:/[A-Z0-9_\-]+)?)`")


def fail(message: str) -> None:
    raise SystemExit(f"READING MAP VALIDATION FAILED — {message}")


# ---------- 1. Carte ----------
def check_map(text: str, errors: list[str]) -> None:
    try:
        rows = rr.parse_route_rows(text)
    except rr.RouteError as exc:
        errors.append(str(exc))
        return
    routes = {locator: (owner, chain) for locator, owner, chain in rows}
    seen: set[str] = set()
    for locator, owner, chain in rows:
        if locator in seen:
            errors.append(f"locator en double : {locator}")
            continue
        seen.add(locator)
        prefix = locator.split("/", 1)[0]
        if owner != f"{prefix}.md":
            errors.append(f"propriétaire incohérent : {locator} → {owner}")
            continue
        root_locator = "/".join(locator.split("/")[:2])
        if rr.heading_locator(chain[0]) != root_locator:
            errors.append(f"destination ne correspond pas au locator : {locator} → {chain[0]}")
            continue
        try:
            rr.resolve(locator, routes)
        except rr.RouteError as exc:
            errors.append(f"titre de locator introuvable : {locator} ({exc})")
    # unicité des titres porteurs d’un locator, dans tous les propriétaires
    carriers: dict[str, list[str]] = {}
    for prefix in rr.PREFIXES:
        path = OFFICIAL / f"{prefix}.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        for index, _, heading in rr.headings(lines):
            own = rr.heading_locator(heading)
            if own:
                carriers.setdefault(own, []).append(f"{path.name}:{index + 1}")
    for locator, places in sorted(carriers.items()):
        if len(places) > 1:
            errors.append(f"locator ambigu : {locator} porté par {', '.join(places)}")
    # couverture : tout locator cité dans les fichiers officiels et la skill est servi
    cited: set[str] = set()
    sources = sorted(OFFICIAL.glob("*.md")) + [SKILL_DIR / "SKILL.md"]
    for source in sources:
        if source.is_file():
            cited.update(CITED.findall(source.read_text(encoding="utf-8")))
    for locator in sorted(cited):
        try:
            rr.resolve(locator, routes)
        except rr.RouteError as exc:
            errors.append(f"locator cité non résolu : {locator} ({exc})")


def check_connections(text: str, errors: list[str]) -> None:
    """Provenance et forme de l’index ; pertinence et qualité restent hors contrôle."""
    try:
        rr.connections(text)
    except (rr.RouteError, OSError) as exc:
        errors.append(f"connexions situées : {exc}")


def check_reader_witness(text: str, errors: list[str]) -> None:
    """Le lecteur autonome refait les contrôles de la carte (témoins synthétiques)."""
    rows = [line for line in text.splitlines() if line.startswith("| `DIRECTION/START` |")]
    if not rows:
        errors.append("témoin du lecteur impossible : ligne DIRECTION/START absente de la table")
        return
    try:
        rr.parse_routes(text.replace(rows[0], rows[0] + "\n" + rows[0], 1))
        errors.append("témoin du lecteur : un locator répété dans la table est accepté")
    except rr.RouteError:
        pass
    owner, chain = rr.parse_routes(text)["DIRECTION/START"]
    try:
        rr.resolve("DIRECTION/START", {"DIRECTION/START": ("SAVOIR.md", chain)})
        errors.append("témoin du lecteur : un propriétaire incohérent est accepté")
    except rr.RouteError as exc:
        if "propriétaire incohérent" not in str(exc):
            errors.append(f"témoin du lecteur : propriétaire incohérent non diagnostiqué ({exc})")


# ---------- 2. Façades : liste close des conditions (LCF) ----------
HANDOFF_TOKENS = re.compile(r"\b(MODE|DECISION-CHANGE|DECISION|RISK|SCOPE|ARTIFACT|OBSERVATION|METHOD|TRACE-LOCATOR|NOT-VERIFIED|"
                            r"NEXT-ACTION|OWNER|NEXT-PROOF|EXIT-CONDITION)\b")
VISIBLE = "MODE — DECISION — CHANGE — PROOF — LIMIT — NEXT-ACTION — OWNER"
OUTCOME = r"(CHANGED|CONFIRMED|ABANDONED|N/A-JUSTIFIED|NOT-OBSERVED)"
USER_EFFECT = re.compile(r"(?i)mémorable|mémoris|tâche|usage|utilisabilit")
PROTOCOL = re.compile(r"(?i)protocole|participant")
UNBOUNDED = re.compile(r"(?<!vise à )(?<!visent à )augmente la (probabilité|qualité)")
STATUS_TOKEN = re.compile(r"`(SEED|PILOT|ADOPTED|DEPRECATED|ABANDONED)`")


def cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


VISIBLE_RUBRIQUES = ("Ce que j’ai fait :", "Pourquoi :", "Ce qui manque pour la vraie version :", "La suite :")


def charge_row(t: dict[str, str], mode: str) -> list[str] | None:
    sec = t["D"][t["D"].find("## DIRECTION/CHARGE"):]
    sec = sec[:sec.find("\n## ", 5)]
    return row(sec, f"**{mode}**")


def row(text: str, key: str, col: int = 0) -> list[str] | None:
    for line in text.splitlines():
        if line.startswith("|") and not line.startswith("|---"):
            found = cells(line)
            if len(found) > col and key in found[col]:
                return found
    return None


def before(text: str, first: str, second: str) -> bool:
    return first in text and second in text and text.index(first) < text.index(second)


def after(text: str, marker: str, length: int) -> str:
    index = text.find(marker)
    return text[index:index + length] if index >= 0 else ""


def fenced_after(text: str, marker: str) -> str:
    index = text.find(marker)
    if index < 0:
        return ""
    match = re.search(r"```(?:text)?\n(.*?)```", text[index:], re.S)
    return match.group(1) if match else ""


def rows_between(text: str, start: str, stop: str) -> list[list[str]]:
    index = text.find(start)
    if index < 0:
        return []
    segment = text[index:]
    end = segment.find(stop, len(start))
    segment = segment[: end if end > 0 else len(segment)]
    found = [cells(line) for line in segment.splitlines() if line.startswith("| ") and not line.startswith("|---")]
    return found[1:]


def plain(cell: str) -> str:
    return re.sub(r"[*`]", "", cell).strip()


def load_texts() -> dict[str, str]:
    files = {
        "D": OFFICIAL / "DIRECTION.md", "A": OFFICIAL / "ACTION.md", "S": OFFICIAL / "SAVOIR.md",
        "B": OFFICIAL / "BIBLIOTHEQUE.md", "C": OFFICIAL / "CHANGELOG.md", "G": OFFICIAL / "GLOSSAIRE.md",
        "Q": OFFICIAL / "QUICKSTART.md", "RM": MAP, "OM": OFFICIAL / "ORCHESTRATION_MAP.md",
        "README": ROOT / "README.md", "NOTES": ROOT / "RELEASE_NOTES.md",
        "SK": SKILL_DIR / "SKILL.md", "EX": SKILL_DIR / "references" / "examples.md",
        "MP": SKILL_DIR / "references" / "machine_projection.md",
    }
    return {key: path.read_text(encoding="utf-8") if path.is_file() else "" for key, path in files.items()}


def lcf_07(t: dict[str, str]) -> bool:
    chain = after(t["D"], "**Chaîne de lecture interne.**", 700)
    prio = fenced_after(t["D"], "```text\nRUN-PRIORITY")
    pointers = [row(t["RM"], "Direction identitaire"), row(t["RM"], "Direction forte et spécifique")]
    rows = [charge_row(t, "DIRECTION")]
    return (before(chain, "`VISUAL_TARGET`", "`FIRST-OBJECT`") and before(prio, "DIRECTION —", "FIRST-OBJECT —")
            and all(r and before(" ".join(r), "VISUAL_TARGET", "FIRST-OBJECT") for r in rows)
            and all(p and "`DIRECTION/CHARGE`" in " ".join(p) for p in pointers))


def lcf_03(t: dict[str, str]) -> bool:
    ui, proof, system = row(t["RM"], "UI/UX habitable"), row(t["RM"], "Preuve et décision fiables"), row(t["RM"], "Système maintenable")
    keys = ("migration", "rollback", "CHANGELOG")
    return (bool(ui) and "ACTION/GATE-A" in ui[1] and "ACTION/GATE-A" not in ui[2]
            and bool(proof) and re.search(r"(?i)gate", proof[1]) is not None and re.search(r"(?i)gate", proof[2]) is None
            and bool(system) and all(k in system[1] for k in keys) and not any(k in system[2] for k in keys))


def lcf_11(t: dict[str, str]) -> bool:
    lines = [l for b in re.findall(r"```text\n(.*?)```", t["EX"], re.S) for l in b.splitlines() if l.startswith("DECISION-CHANGE:")]
    glossary = next((l for l in t["G"].splitlines() if l.startswith("| **DECISION-CHANGE** |")), "")
    return (bool(lines) and all(re.match(rf"DECISION-CHANGE: {OUTCOME} — .+\(observation : .+\)", l) for l in lines)
            and re.search(OUTCOME, glossary) is not None and "observation" in glossary)


def lcf_12(t: dict[str, str]) -> bool:
    blocks = [b for b in re.findall(r"```text\n(.*?)```", t["EX"], re.S) if "ACCEPTED-WITH-RESERVATION" in b]
    glossary = [l for l in t["G"].splitlines() if l.startswith("|") and "ACCEPTED-WITH-RESERVATION" in l and "Exemple" not in l and "**Verdict" not in l]
    complete = lambda s: all(re.search(p, s, re.I) for p in (r"owner", r"prochaine preuve", r"revue", r"(condition de )?sortie"))
    return all(re.search(r"(?m)^RESERVATION: ", b) and complete(b) for b in blocks) and all(complete(l) for l in glossary)


def lcf_13(t: dict[str, str]) -> bool:
    blocks = re.findall(r"```text\n(.*?)```", t["EX"], re.S)
    return (all(not re.search(r"(?m)^NOT-OBSERVED:", b) for b in blocks)
            and all("STATE: CLOSED" not in b or re.search(r"(?m)^VERDICT: ", b) for b in blocks))


def lcf_14(t: dict[str, str]) -> bool:
    evidence = [l for b in re.findall(r"```text\n(.*?)```", t["EX"], re.S) for l in b.splitlines() if l.startswith("EVIDENCE:") and "capture" in l]
    return bool(evidence) and all(not USER_EFFECT.search(l) or PROTOCOL.search(l) for l in evidence)


def lcf_15_16_17(t: dict[str, str]) -> tuple[bool, bool, bool]:
    first = rows_between(t["D"], "### Contrat positif du premier objet", "\n#")
    dims = [plain(r[0]) for r in first]
    quick = [plain(r[0]) for r in rows_between(t["Q"], "## 6. Produire une qualité positive", "\n#")]
    cft = {plain(r[0]) for r in rows_between(t["S"], "## CFT-00", "### Creative Quality Review")}
    header = next((l for l in t["D"][t["D"].find("### Contrat positif du premier objet"):].splitlines() if l.startswith("| Dimension")), "")
    col = next((k for k, c in enumerate(cells(header)) if "CFT-00" in c), None)
    mapped = [v.strip() for r in first if col is not None and len(r) > col for v in re.split(r"[,+/]| et ", plain(r[col])) if v.strip()]
    triggers = {plain(r[0]): r[1] for r in rows_between(t["D"], "### Déclencheurs critiques", "\n#") if len(r) > 1}
    pick = lambda start: next((v for k, v in triggers.items() if k.startswith(start)), "")
    motif, scene, density = pick("Motif possiblement générique"), pick("Asset, motion, scène"), pick("Détail final")
    return (bool(dims) and quick == dims,
            col is not None and bool(mapped) and all(v in cft or v in {"—", "DIRECTION"} for v in mapped),
            "SAVOIR/CRAFT/CFT-01" in motif and "ACTION/ANTI-SLOP" in motif and "BIBLIOTHEQUE/" in scene and "SAVOIR/CRAFT" in density)


def lcf_20(t: dict[str, str]) -> bool:
    section = t["C"][t["C"].find("## Cycle de vie des routes"):t["C"].find("## Migration des anciens aliases")]
    table = {m.group(1) for m in (re.match(r"\| `([A-Z]+)` \|", l) for l in section.splitlines()) if m}
    listed = [l for l in t["B"].splitlines() if "`PILOT`" in l and "`DEPRECATED`" in l]
    return bool(table) and len(listed) >= 2 and all(set(STATUS_TOKEN.findall(l)) == table for l in listed)


def lcf_21(t: dict[str, str]) -> bool:
    present = [t[k] for k in ("README", "NOTES", "C") if t[k]]  # RELEASE_NOTES n’existe pas dans la distribution Local
    return all("NOT-VERIFIED" in text for text in present) and not UNBOUNDED.search(t["D"])


# ---------- LCF-22 à LCF-35 ----------
SCHEMA = ROOT / "schemas" / "run_card.schema.json"
NUM_WORDS = {3: "trois", 4: "quatre", 5: "cinq", 6: "six", 7: "sept"}
CHANGE_ENUM = re.compile(r"DECISION-CHANGE[^.\n]{0,120}N/A-JUSTIFIED|N/A-JUSTIFIED[^.\n]{0,120}DECISION-CHANGE")
BOOT_COUNT = re.compile(r"(?i)\b(une|deux|trois|\d+)\s+(anti-directions?|tensions?)\b")


def lcf_22(t: dict[str, str]) -> bool:
    lines = [l for k in ("A", "D", "G", "Q", "S", "SK", "EX", "MP") for l in t[k].splitlines()
             if not l.startswith("DECISION-CHANGE:") and (CHANGE_ENUM.search(l) or ("`CHANGE` vaut" in l and "N/A-JUSTIFIED" in l))]
    return bool(lines) and all("NOT-OBSERVED" in l for l in lines) and not any("obtenue ou attendue" in t[k] for k in ("A", "G"))


def lcf_23(t: dict[str, str]) -> bool:
    b1b = t["A"][t["A"].find("### B1b"):]
    scope = next((p for p in b1b.split("\n\n")[1:3] if "requis par module" in p), "")
    return all(k in scope for k in ("`DIRECTION`", "`ACCEPTED-WITH-RESERVATION`", "`PASS-WITH-RESERVATION`"))


def lcf_24(t: dict[str, str]) -> bool:
    boots = [[l for l in t[k].splitlines() if "Creative Boot" in l or "CREATIVE-BOOT" in l] for k in ("Q", "SK")]
    return all(boots) and not any(BOOT_COUNT.search(l) for group in boots for l in group)


def lcf_25(t: dict[str, str]) -> bool:
    carte = t["A"][t["A"].find("### Carte de lecture par mode"):t["A"].find("### ACTION/HANDOFF")]
    for mode in ("LITE", "ITER"):
        sk, ac = charge_row(t, mode), row(carte, f"`{mode}`")
        if not (sk and ac and len(sk) > 2 and "ACTION/GATE-B" in sk[1] and not re.search(r"(?i)gates? B", sk[2]) and "ACTION/GATE-B" in ac[1]):
            return False
    return True


def lcf_26(t: dict[str, str]) -> bool:
    try:
        props = json.loads(SCHEMA.read_text(encoding="utf-8"))["properties"]["run_card"]["properties"]
        axes = set(props["closure"]["properties"]["axes"]["properties"]["V"]["enum"])
        fields = props["profile_decision"]["required"]
    except (OSError, KeyError, ValueError):
        return False
    axis_line = next((l for l in t["MP"].splitlines() if "`closure.axes`" in l), "")
    listed = set(re.findall(r"`([A-Z/-]+)`", axis_line.split("`closure.axes`", 1)[-1].split(";")[0])) if axis_line else set()
    pd_line = next((l for l in t["MP"].splitlines() if "`profile_decision`" in l and "champs" in l), "")
    count = re.search(r"(\w+) champs sont obligatoires", pd_line)
    return (listed == axes and bool(count) and count.group(1) == NUM_WORDS.get(len(fields))
            and all(f"`{f}`" in pd_line for f in fields))


def lcf_27(t: dict[str, str]) -> bool:
    texts = [t[k] for k in ("C", "NOTES", "README") if t[k]]
    return all("alignés sur leurs propriétaires" not in x for x in texts) and "liste close des conditions de façade" in t["C"]


def lcf_28(t: dict[str, str]) -> bool:
    vt = t["D"][t["D"].find("## DIRECTION/VISUAL_TARGET"):t["D"].find("### Compilation de la première proposition")]
    fields = {plain(r[0]).lower() for r in rows_between(vt, "| Champ |", "\n\n")}
    claims = [c.strip().lower() for l in t["A"].splitlines() if l.startswith("| VISUAL_TARGET :")
              for c in re.split(r",| et ", cells(l)[0].split(":", 1)[1])]
    return bool(fields) and bool(claims) and all(c in fields for c in claims)


def lcf_29(t: dict[str, str]) -> bool:
    legend = t["D"][t["D"].find("### Légende"):]
    legend = legend[:legend.find("\n#", 5)]
    sentence = next((l for l in legend.splitlines() if "SAVOIR" in l and not l.startswith("|")), "")
    tags = re.findall(r"`(\[[^\]`]+\])`", sentence)
    return bool(tags) and all(tag[:-1] in t["S"] or f"`{tag}` n’y est pas employé" in sentence for tag in tags)


def retour_si(text: str, start: str) -> dict[str, str]:
    i = text.find(start)
    if i < 0:
        return {}
    seg = text[i:]
    j = seg.find("\n#", len(start))
    seg = seg[: j if j > 0 else len(seg)]
    header = next((cells(l) for l in seg.splitlines() if l.startswith("| Dimension")), [])
    k = next((n for n, c in enumerate(header) if c.startswith("Retour si")), None)
    if k is None:
        return {}
    return {plain(r[0]): plain(r[k]) for r in rows_between(seg, "| Dimension", "\n\n") if len(r) > k}


def lcf_30(t: dict[str, str]) -> bool:
    d = retour_si(t["D"], "### Contrat positif du premier objet")
    return bool(d) and retour_si(t["Q"], "## 6. Produire une qualité positive") == d


def lcf_31(t: dict[str, str]) -> bool:
    head = t["EX"][:t["EX"].find("\n## ")]
    return all(k in head for k in ("schemas/run_card.example.json", "machine_projection.md", "validate_run_card.py"))


def lcf_32(t: dict[str, str]) -> bool:
    l = next((x for x in t["A"].splitlines() if "Un droit inconnu" in x), "")
    return "interdit `ACCEPTED`" in l and "`ACCEPTED-WITH-RESERVATION`" in l and "avant diffusion" in l


def lcf_33(t: dict[str, str]) -> bool:
    sav = next((l for l in t["S"].splitlines() if l.startswith("Toute ressource de stack")), "")
    pol = t["A"][t["A"].find("Toute ressource technique maintenue indique"):].splitlines()[1:]
    items: list[str] = []
    for l in pol:
        if l.startswith("- "):
            items.append(l)
        elif items:
            break
    return (bool(sav) and "ACTION/POLICIES" in sav and "date de vérification" not in sav
            and len(items) == 7 and "sept champs" in t["A"])


def lcf_34(t: dict[str, str]) -> bool:
    outs = [l for l in t["A"].splitlines() if l.startswith("**Sortie.**")]
    return len(outs) == 5 and all(re.match(r"\*\*Sortie\.\*\* Paquet `[A-ZÈ]+` d’`ACTION/CLOSE-PACKAGE`\.", l) for l in outs)


def lcf_35(t: dict[str, str]) -> bool:
    closed = next((l for l in t["G"].splitlines() if l.startswith("| **CLOSED** |")), "")
    return bool(closed) and "n’est pas éligible" not in closed and "NOT-VERIFIED" in closed and "exclut `ACCEPTED`" in closed


# ---------- LCF-36 à LCF-42 ----------
NO_DECISION = re.compile(r"(?i)aucune décision (ne change|n’est changée|modifiée)")


def lcf_36(t: dict[str, str]) -> bool:
    l = next((x for x in t["A"].splitlines() if "Un droit inconnu" in x), "")
    return "que pour une `RUN_CARD` `DIRECTION`" in l and "contrôle seulement l’exclusion" not in l


def lcf_37(t: dict[str, str]) -> bool:
    seg = t["A"][t["A"].find("## ACTION/CLOSE-PACKAGE"):]
    rows = [l for l in seg[:seg.find("\n\n", seg.find("| Mode | Paquet minimal"))].splitlines() if l.startswith("| **")]
    return len(rows) == 5 and all("NOT-OBSERVED" in l for l in rows)


def lcf_38(t: dict[str, str]) -> bool:
    lines = [l for k in ("A", "D", "S", "B", "Q", "G", "SK", "EX") for l in t[k].splitlines()
             if NO_DECISION.search(l) and "N/A-JUSTIFIED" in l]
    sav = next((l for l in t["S"].splitlines() if l.startswith("La sortie de SAVOIR")), "")
    return (all("NOT-OBSERVED" in l or "non applicable" in l or "selon le contrat ACTION" in l for l in lines)
            and "À la clôture" in sav)


def lcf_39(t: dict[str, str]) -> bool:
    sec = t["Q"][t["Q"].find("## 5. Charger"):t["Q"].find("## 6.")]
    return ("`DIRECTION/CHARGE`" in sec and not row(sec, "`LITE`")
            and all((r := charge_row(t, m)) and "ACTION/GATE-A" in r[1] and "ACTION/GATE-B" in r[1] for m in ("LITE", "ITER")))


def lcf_40(t: dict[str, str]) -> bool:
    closed = next((l for l in t["G"].splitlines() if l.startswith("| **CLOSED** |")), "")
    exit_rows = [l for l in t["A"].splitlines() if l.startswith("| Réserves |") or l.startswith("7. La réserve")]
    return "date ou version" in closed and len(exit_rows) == 2 and all("date ou version" in l for l in exit_rows)


def lcf_41(t: dict[str, str]) -> bool:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    found: list[str] = []

    def walk(node: object, path: list[str]) -> None:
        if isinstance(node, dict):
            enum, typ = node.get("enum"), node.get("type")
            if (isinstance(enum, list) and None in enum) or typ == "null" or (isinstance(typ, list) and "null" in typ):
                found.append(".".join(p for p in path if p not in ("properties", "run_card")))
            for key, value in node.items():
                walk(value, path + [key])
        elif isinstance(node, list):
            for value in node:
                walk(value, path)

    walk(schema.get("properties", {}), [])
    line = next((l for l in t["A"].splitlines() if "`null` signifie" in l), "")
    return (bool(found) and all(f"`{f}`" in line for f in found) and "champ facultatif sans valeur est omis" in line
            and "schéma l’admet" in t["MP"] and "champ facultatif sans valeur est omis" in t["MP"])


def lcf_42(t: dict[str, str]) -> bool:
    ex = t["Q"][t["Q"].find("## 9. Exemple complet minimal"):t["Q"].find("## 10.")]
    after = ex.split("DECISION-CHANGE:\n", 1)
    return (bool(ex) and not re.search(r"(?m)^CHANGE:", ex) and len(after) == 2
            and re.match(OUTCOME + r" — ", after[1]) is not None and "reste à réobserver" in after[1].split("\n\n")[0]
            and not after[1].startswith("CHANGED"))


# ---------- LCF-43 à LCF-46 ----------
BRIEF_ORDER = re.compile(r"contenu réel.{0,80}?marque.{0,120}?asset principal.{0,120}?destination")
WAVE_MARKERS = re.compile(r"hero SaaS|gradient décoratif|\bviolet\b|\bInter\b|\bhalos?\b|\bbeige\b|\bcrème\b|serif italique|"
                          r"orange rouille|bandeau défilant|illustration peinte|\btramage\b|"
                          r"\bdithering\b|logos? pixel|\bASCII\b|hachures de plan|bleu Klein|paysage peint")


def boot_block(t: dict[str, str]) -> list[str]:
    return fenced_after(t["D"], "Le boot tient au maximum les décisions suivantes").splitlines()


def lcf_43(t: dict[str, str]) -> bool:
    entry = fenced_after(t["D"], "### Entrée minimale").splitlines()
    boot = boot_block(t)
    vt = t["D"][t["D"].find("### Décider la route de production"):t["D"].find("### Réserve `ANCHOR-GENERATED`")]
    return (any(l.startswith("CONSTRAINT —") and "destination" in l for l in entry) and any(l.startswith("FABRICATION:") for l in boot)
            and not any(l.startswith(("ANCHOR-BASIS:", "ANCHOR-LIMIT:")) for l in boot)
            and "jamais un faux asset" in vt and "bilan `FABRICATION`" in t["A"]
            and all("`FABRICATION`" in t[k] for k in ("Q", "SK")))


def lcf_44(t: dict[str, str]) -> bool:
    ext = t["D"][t["D"].find("## DIRECTION/EXTERNAL-START"):t["D"].find("### Traduction humaine minimale")]
    return all(BRIEF_ORDER.search(x) and "au plus trois" in x.lower() for x in (ext, t["Q"], t["SK"]))


def lcf_45(t: dict[str, str]) -> bool:
    boot = boot_block(t)
    return (any(l.startswith("MODAL:") for l in boot) and any(l.startswith("PARTI:") for l in boot)
            and not any(l.startswith("ANTI-DIRECTIONS:") for l in boot)
            and all("`MODAL`/`PARTI`" in t[k] for k in ("Q", "SK")) and "MODAL:" in t["EX"])


# Un halo de détourage ou de bord est un défaut de production, pas une affirmation de tendance :
# la ligne est exemptée seulement si « halo » est son unique marqueur, que ce contexte y est nommé
# et qu'aucune formulation décorative n'apparaît. « halos lumineux » non daté reste refusé.
HALO_PRODUCTION = re.compile(r"détour|\bbords?\b|\bcontours?\b", re.IGNORECASE)


def wave_hit(line: str) -> bool:
    hits = [m.group(0) for m in WAVE_MARKERS.finditer(line)]
    if not hits:
        return False
    only_halo = all(re.fullmatch(r"halos?", h, re.IGNORECASE) for h in hits)
    decorative = re.search(r"halos? (?:décoratifs?|lumineux|diffus)", line, re.IGNORECASE)
    return not (only_halo and HALO_PRODUCTION.search(line) and not decorative)


def lcf_46(t: dict[str, str]) -> bool:
    keys = ("D", "A", "S", "B", "G", "Q", "RM", "OM", "README", "SK", "EX")
    stray = [l for k in keys for l in t[k].splitlines() if wave_hit(l) and not l.startswith("[VEILLE 20")]
    dated = [l for l in t["S"].splitlines() if l.startswith("[VEILLE 20") and wave_hit(l)]
    return not stray and bool(dated)


# ---------- LCF-47 à LCF-50 ----------
def savoir_section(t: dict[str, str], start: str, stop: str) -> str:
    return t["S"][t["S"].find(start):t["S"].find(stop)]


def lcf_47(t: dict[str, str]) -> bool:
    fo = t["D"][t["D"].find("## DIRECTION/FIRST-OBJECT"):t["D"].find("### Contrat positif du premier objet")]
    return "de préférence **codé**" in fo and bool(re.search(r"de préférence (\*\*)?codé", t["SK"]))


def lcf_48(t: dict[str, str]) -> bool:
    vt = t["D"][t["D"].find("### Décider la route de production"):t["D"].find("### Réserve `ANCHOR-GENERATED`")]
    carte = [l for l in t["S"].splitlines() if l.startswith("[VEILLE 20") and "Carte des moyens par couche" in l]
    return bool(carte) and "jamais des styles" in carte[0] and "carte des moyens" in vt


def lcf_49(t: dict[str, str]) -> bool:
    atlas = savoir_section(t, "# SAVOIR/DESIGN-ATLAS", "# SAVOIR/STYLE")
    vt = t["D"][t["D"].find("### Décider la route de production"):t["D"].find("### Réserve `ANCHOR-GENERATED`")]
    return "**Traitement des assets moyens.**" in atlas and "jamais un dessin de remplacement" in vt


def lcf_50(t: dict[str, str]) -> bool:
    return any(l.startswith("[VEILLE 20") and "Vague 3 :" in l for l in t["S"].splitlines())


# Corrections de la révision de mobilisation ; chaque condition possède sa mutation rouge.
def lcf_51(t: dict[str, str]) -> bool:
    entry = next((l for l in t["B"].splitlines() if l.startswith("2. **Zéro route")), "")
    local = row(t["B"], "Local")
    return (all(word in entry for word in ("héritage", "source", "justification", "non-applicabilité réelle"))
            and "conserve-la et justifie `N/A-JUSTIFIED`" not in entry
            and "`N/A-JUSTIFIED` si aucune route ne change" not in t["B"]
            and bool(local) and "héritage" in local[1] and "réellement non applicable" in local[1])


def lcf_52(t: dict[str, str]) -> bool:
    definition = row(t["G"], "**RUN_CARD**")
    return bool(definition) and all(value in definition[1] for value in
                                   ("niveau de trace", "trace légère", "ne produit pas", "ACTION/RUN_CARD", "ACTION/CLOSE-PACKAGE"))


def lcf_53(t: dict[str, str]) -> bool:
    policy = next((l for l in t["D"].splitlines() if l.startswith("policy_profile:")), "")
    return all(f"`{key}`" in policy for key in
               ("risk_triggers", "required_controls", "risk_coverage", "depth_rules", "contraindications"))


def lcf_54(t: dict[str, str]) -> bool:
    snapshot = after(t["A"], "### Vue d’exécution dérivée", 5000)
    return (all("python3 scripts/read_route.py --connexions" in t[key] for key in ("D", "SK"))
            and all(value in snapshot for value in ("trace existante", "source pertinente change", "effet comme attendu",
                                                   "capacités d’observation attestées", "autorité d’action")))


def lcf_55(t: dict[str, str]) -> bool:
    tree = after(t['D'], '### Arbre de classification', 3000)
    iter_line = next((line for line in tree.splitlines() if line.startswith('3. ')), '')
    quick_iter = next((line for line in t['Q'].splitlines() if line.startswith('3. **`ITER`**')), '')
    return (all(term in iter_line for term in ('rappeler et réévaluer', 'au-delà d’un fix ou delta local qui la conserve'))
            and all(term in quick_iter for term in ('rappeler et réévaluer', 'au-delà d’un fix local qui la conserve')))


def lcf_56(t: dict[str, str]) -> bool:
    handoff = after(t['A'], '### ACTION/HANDOFF', 7500)
    definition = row(t['G'], '**Trace complète**')
    map_exception = 'sauf la forme courte LITE sans RUN_CARD définie'
    return ('sauf la forme courte LITE définie ci-dessus' in handoff
            and 'une demande de projection structurée requiert la `RUN_CARD` validée' in handoff
            and bool(definition) and 'est complète sans RUN_CARD' in definition[1]
            and map_exception in t['RM'] and 'forme courte LITE sans RUN_CARD est admise' in t['Q']
            and 'La forme courte LITE conserve une trace complète sans RUN_CARD' in t['SK'])


def check_facades(errors: list[str]) -> None:
    t = load_texts()
    rm33, rm49 = row(t["RM"], "Direction identitaire"), row(t["RM"], "Accessibilité")
    qs_dir, rd_dir, rd_iter = row(t["Q"], "`DIRECTION`", 1), row(t["README"], "`DIRECTION`", 1), row(t["README"], "`ITER`", 1)
    index = row(t["D"], "Nouvelle structure d’écran")
    entry = after(t["D"], "Ce gabarit est une vue d’activation", 600)
    fast = row(t["D"], "Quel est le risque dominant ?")
    prio = fenced_after(t["D"], "```text\nRUN-PRIORITY")
    canon = HANDOFF_TOKENS.findall(fenced_after(t["A"], "### ACTION/HANDOFF"))
    f15, f16, f17 = lcf_15_16_17(t)
    # (ID, façade, source propriétaire, condition tenue)
    table = [
        ("LCF-01", "READING_MAP, ligne « Direction identitaire »", "DIRECTION/START ; ACTION/RUN-DIRECTION [FORCÉ]",
         bool(rm33) and "`DIRECTION/CHARGE`" in rm33[1] and bool(charge_row(t, "DIRECTION"))
         and "ACTION/RUN-DIRECTION" in charge_row(t, "DIRECTION")[1] and "ACTION/RUN-DIRECTION" not in charge_row(t, "DIRECTION")[2]),
        ("LCF-02", "READING_MAP, ligne « Accessibilité »", "ACTION/GATE-A (contrôles applicables dus)",
         bool(rm49) and "N/A-JUSTIFIED" not in rm49[-1] and "ACTION/GATE-A" in rm49[-1]),
        ("LCF-03", "READING_MAP (combinaisons), noyau UI/UX, preuve, système", "ACTION/GATE-A ; gate du risque ; paquet SYSTÈME (B3)", lcf_03(t)),
        # La table des modes vit dans le guide opérateur (QUICKSTART) ; l'entrée
        # humaine (README) ne demande aucun mode. Les propriétés sont conservées sur la table qui subsiste.
        ("LCF-04", "QUICKSTART, ligne DIRECTION ; aucune table de mode dans le README", "DIRECTION/START (direction visuelle autonome)",
         bool(qs_dir) and "craft" not in qs_dir[0].lower() and "autonome" in qs_dir[0] and rd_dir is None),
        ("LCF-05", "QUICKSTART, ITER dans l'ordre canonique ; aucune ligne ITER dans le README",
         "DIRECTION/START (ITER : direction existante et retrouvable)",
         re.search(r"\*\*`ITER`\*\*[^\n]*(retrouvable|existante)", t["Q"]) is not None and rd_iter is None),
        ("LCF-06", "DIRECTION, index « Nouvelle structure d’écran »", "DIRECTION/START (classification)",
         bool(index) and "classification `ACTION/RUN-STANDARD`" not in index[1]),
        ("LCF-07", "DIRECTION 72, RUN-PRIORITY, READING_MAP (routage et combinaisons), skill", "DIRECTION 55 (cible avant premier objet)", lcf_07(t)),
        ("LCF-08", "DIRECTION, gabarit START et FAST-PATH", "DIRECTION/START (OWNER et SCOPE jamais omis)",
         re.search(r"`?OWNER`? et `?SCOPE`?[^.]*jamais omis", entry) is not None and bool(fast) and "si nécessaire" not in fast[1]),
        ("LCF-09", "DIRECTION, RUN-PRIORITY et récapitulatif de protection (point 4)", "BIBLIOTHEQUE/SELECT, SCENE",
         bool(re.search(r"FIRST-OBJECT —[\s\S]*?sauf si", prio))),
        ("LCF-10", "QUICKSTART, table de mode ; README sans table de mode", "D-FAC-1 (classement : voir DIRECTION/START)",
         re.search(r"(?i)classement\s*:\s*voir `DIRECTION/START`", t["Q"]) is not None and rd_dir is None and rd_iter is None),
        ("LCF-C1", "READING_MAP et skill, copies du handoff", "ACTION/HANDOFF",
         bool(canon) and HANDOFF_TOKENS.findall(fenced_after(t["RM"], "## Handoff minimal commun")) == canon
         and (not after(t["SK"], "## Carte de lecture et sortie", 10)
              or all(token in HANDOFF_TOKENS.findall(after(t["SK"], "## Carte de lecture et sortie", 2500)) for token in canon))),
        ("LCF-C2", "QUICKSTART et skill, réponse visible", "ACTION/HANDOFF",
         all(r in after(t["A"], "### ACTION/HANDOFF", 4000) for r in VISIBLE_RUBRIQUES)
         and "réponse visible en langage produit" in t["Q"] and "`ACTION/HANDOFF`" in t["Q"]
         and all(r in t["SK"] for r in VISIBLE_RUBRIQUES) and VISIBLE not in t["Q"] + t["SK"]),
        ("LCF-11", "exemples de la skill et GLOSSAIRE, DECISION-CHANGE", "ACTION/STATUS (triade) ; INV-C1-1", lcf_11(t)),
        ("LCF-12", "exemples et GLOSSAIRE, ACCEPTED-WITH-RESERVATION", "INV-B2-9 ; ACTION (réserve complète)", lcf_12(t)),
        ("LCF-13", "exemples de la skill, NOT-OBSERVED et VERDICT", "triade C1 ; INV-C1-4", lcf_13(t)),
        ("LCF-14", "exemples de la skill, EVIDENCE fondées sur des captures", "ACTION (claims et protocole)", lcf_14(t)),
        ("LCF-15", "QUICKSTART §6", "DIRECTION/FIRST-OBJECT (dimensions)", f15),
        ("LCF-16", "DIRECTION, contrat du premier objet, colonne CFT-00", "SAVOIR/CRAFT/CFT-00", f16),
        ("LCF-17", "DIRECTION, déclencheurs critiques", "SAVOIR/CRAFT ; BIBLIOTHEQUE ; ACTION/ANTI-SLOP", f17),
        ("LCF-20", "BIBLIOTHEQUE, listes des statuts de route", "CHANGELOG, cycle de vie", lcf_20(t)),
        ("LCF-21", "DIRECTION, README, RELEASE_NOTES, CHANGELOG", "CHANGELOG (efficacité NOT-VERIFIED)", lcf_21(t)),
        ("LCF-22", "ACTION (table RUN_CARD, réponse visible, paquets), GLOSSAIRE et façades : DECISION-CHANGE", "ACTION/STATUS (triade) ; RET-1", lcf_22(t)),
        ("LCF-23", "ACTION/GATE-B — B1b, portée", "validate_run_card (check_b1b) ; INV-B3-3 ; RET-2", lcf_23(t)),
        ("LCF-24", "QUICKSTART et skill, Creative Boot", "DIRECTION/CREATIVE-BOOT ; BIBLIOTHEQUE/TENSION ; RET-3", lcf_24(t)),
        ("LCF-25", "skill et carte d'ACTION, chargement LITE et ITER", "ACTION/PRECONDITION (Gate B du risque) ; RET-4", lcf_25(t)),
        ("LCF-26", "machine_projection : axes et profile_decision", "schemas/run_card.schema.json ; RET-5", lcf_26(t)),
        ("LCF-27", "CHANGELOG, RELEASE_NOTES, README : portée de la cohérence des façades", "liste close des conditions de façade ; RET-6", lcf_27(t)),
        ("LCF-28", "ACTION, table de correspondance RUN_CARD : lignes VISUAL_TARGET", "DIRECTION/VISUAL_TARGET (table canonique)", lcf_28(t)),
        ("LCF-29", "DIRECTION, légende des tags", "SAVOIR (Niveaux d’autorité) ; F-DIR-005", lcf_29(t)),
        ("LCF-30", "QUICKSTART §6, colonne « Retour si… »", "DIRECTION/FIRST-OBJECT", lcf_30(t)),
        ("LCF-31", "exemples de la skill : renvoi à la sérialisation", "ACTION/RUN_CARD ; schemas/run_card.example.json ; C6", lcf_31(t)),
        ("LCF-32", "ACTION, droits inconnus", "validate_run_card (rights_status) ; INV-B2-10", lcf_32(t)),
        ("LCF-33", "SAVOIR, ressource de stack", "ACTION/POLICIES (sept champs)", lcf_33(t)),
        ("LCF-34", "ACTION, sorties des blocs RUN-*", "ACTION/CLOSE-PACKAGE", lcf_34(t)),
        ("LCF-35", "GLOSSAIRE, exemple CLOSED", "ACTION (protection critique) ; B1", lcf_35(t)),
        ("LCF-36", "ACTION, droits inconnus : portée du contrôle machine", "validate_run_card (rights_status, DIRECTION)", lcf_36(t)),
        ("LCF-37", "ACTION/CLOSE-PACKAGE, cinq paquets", "ACTION/STATUS (triade) ; validate_run_card (decision_change)", lcf_37(t)),
        ("LCF-38", "sources et façades : « aucune décision » et N/A-JUSTIFIED", "ACTION/STATUS (triade)", lcf_38(t)),
        ("LCF-39", "QUICKSTART §5, chargement LITE et ITER", "ACTION/PRECONDITION (Gate B du risque)", lcf_39(t)),
        ("LCF-40", "GLOSSAIRE, exemple CLOSED : réserve à sept attributs", "ACTION (réserve) ; RESERVATION_FIELDS", lcf_40(t)),
        ("LCF-41", "ACTION et machine_projection : champs admettant null", "schemas/run_card.schema.json ; O-1", lcf_41(t)),
        ("LCF-42", "QUICKSTART §9 : DECISION-CHANGE selon la triade", "ACTION/STATUS ; ACTION/HANDOFF", lcf_42(t)),
        ("LCF-43", "DIRECTION (entrée, boot, route de production), ACTION, QUICKSTART, skill : bilan de fabrication", "DIRECTION/CREATIVE-BOOT (FABRICATION)", lcf_43(t)),
        ("LCF-44", "EXTERNAL-START, QUICKSTART, skill : prise de brief, même ordre", "DIRECTION/EXTERNAL-START (prise de brief)", lcf_44(t)),
        ("LCF-45", "boot, QUICKSTART, skill, exemples : MODAL / PARTI", "DIRECTION/CREATIVE-BOOT (MODAL, PARTI)", lcf_45(t)),
        ("LCF-46", "textes et façades : marqueurs de vague seulement en [VEILLE] daté", "SAVOIR ([VEILLE] daté)", lcf_46(t)),
        ("LCF-47", "FIRST-OBJECT et skill : objet de preuve codé, de préférence", "DIRECTION/FIRST-OBJECT", lcf_47(t)),
        ("LCF-48", "SAVOIR ([VEILLE] daté) et route de production : carte des moyens", "SAVOIR ([VEILLE])", lcf_48(t)),
        ("LCF-49", "SAVOIR (DESIGN-ATLAS) et route de production : traitement des assets moyens", "SAVOIR (DESIGN-ATLAS)", lcf_49(t)),
        ("LCF-50", "SAVOIR, [VEILLE] daté : vague 3", "SAVOIR ([VEILLE])", lcf_50(t)),
        ("LCF-51", "BIBLIOTHEQUE, entrée et résumés locaux", "BIBLIOTHEQUE/FAST-PATH ; ACTION/STATUS (héritage distinct de non-applicabilité)", lcf_51(t)),
        ("LCF-52", "GLOSSAIRE, RUN_CARD", "ACTION/HANDOFF ; ACTION/RUN_CARD (niveau de trace et mode)", lcf_52(t)),
        ("LCF-53", "DIRECTION, gabarit DOMAIN-FRAME", "schemas/domain_frame.schema.json (risk_coverage)", lcf_53(t)),
        ("LCF-54", "DIRECTION, noyau et snapshot", "DIRECTION/CHARGE ; ACTION/RUN_CARD (mobilisation, limites et fraîcheur)", lcf_54(t)),
        ('LCF-55', 'START et QUICKSTART : frontière LITE / ITER', 'DIRECTION/START (fix conservé ou direction réévaluée)', lcf_55(t)),
        ('LCF-56', 'HANDOFF, guides et noyau : exception de trace complète LITE', 'ACTION/HANDOFF ; ACTION/CLOSE-PACKAGE', lcf_56(t)),
    ]
    for lcf_id, facade, source, held in table:
        if not held:
            errors.append(f"{lcf_id} : condition de façade non tenue — {facade} (propriétaire : {source})")


def main() -> int:
    bad = rr.non_utf8(rr.ROOT)  # encodage nommé avant toute lecture
    if bad:
        fail(f"Markdown non UTF-8 : {', '.join(bad)}")
    if not MAP.is_file():
        fail("READING_MAP.md absent")
    text = MAP.read_text(encoding="utf-8")
    for item in REQUIRED:
        if item not in text:
            fail(f"élément obligatoire absent : {item}")
    for route, owner in OWNER_MAP.items():
        if route not in text:
            fail(f"propriétaire de route absent : {route}")
        if not owner.is_file():
            fail(f"fichier propriétaire absent : {owner}")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        target = target.split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (MAP.parent / target).exists():
            fail(f"lien relatif non résolu : {target}")
    # The map must remain derived and cannot introduce a competing classifier.
    if "source" not in text or "normative" not in text or "ne reclassifie pas" not in text:
        fail("frontière de non-autorité ou de non-reclassification absente")
    errors: list[str] = []
    check_map(text, errors)
    check_connections(text, errors)
    check_reader_witness(text, errors)
    check_facades(errors)
    if errors:
        print("READING MAP VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("READING MAP VALIDATION PASSED — carte dérivée, propriétaires, locators, liens et conditions de façade contrôlés")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
