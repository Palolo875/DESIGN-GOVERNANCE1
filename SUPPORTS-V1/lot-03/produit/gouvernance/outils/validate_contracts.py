#!/usr/bin/env python3
"""Validate DOMAIN_FRAME, RESEARCH_BRIEF and production contracts.

The validator implements the documented dependency-free schema subset and makes
its input explicit: a supplied JSON path is validated, while no argument runs
the complete built-in contract suite.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]  # gouvernance/outils/ → racine du package
CONTRACTS = {
    "domain_frame": (ROOT / "gouvernance/schemas/domain_frame.schema.json", ROOT / "gouvernance/schemas/examples/domain_frame.example.json"),
    "research_brief": (ROOT / "gouvernance/schemas/research_brief.schema.json", ROOT / "gouvernance/schemas/examples/research_brief.example.json"),
    "production_contracts": (ROOT / "gouvernance/schemas/production_contracts.schema.json", ROOT / "gouvernance/schemas/examples/production_contracts.example.json"),
}
METADATA_KEYS = {"$schema", "$id", "title", "description", "default", "examples"}
SUPPORTED_KEYS = {"type", "enum", "required", "properties", "additionalProperties", "items", "minLength", "minItems", "maxItems"} | METADATA_KEYS


class ValidationError(Exception):
    """Readable validation failure."""


def validate(value: Any, schema: dict[str, Any], path: str = "$") -> None:
    unknown_schema_keys = set(schema) - SUPPORTED_KEYS
    if unknown_schema_keys:
        raise ValidationError(f"{path}: mots-clés de schéma non supportés : {', '.join(sorted(unknown_schema_keys))}")
    if "enum" in schema and value not in schema["enum"]:
        raise ValidationError(f"{path}: valeur non canonique: {value}")
    if "type" in schema:
        expected = schema["type"]
        checks = {
            "object": isinstance(value, dict),
            "array": isinstance(value, list),
            "string": isinstance(value, str),
            "boolean": isinstance(value, bool),
            "null": value is None,
            "number": isinstance(value, (int, float)) and not isinstance(value, bool),
            "integer": isinstance(value, int) and not isinstance(value, bool),
        }
        if isinstance(expected, list):
            if not any(checks.get(item, False) for item in expected):
                raise ValidationError(f"{path}: type attendu {'/'.join(expected)}")
        elif not checks.get(expected, False):
            raise ValidationError(f"{path}: type attendu {expected}")
    if isinstance(value, str) and "minLength" in schema and len(value.strip()) < schema["minLength"]:
        raise ValidationError(f"{path}: chaîne vide ou composée uniquement d’espaces")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            raise ValidationError(f"{path}: nombre minimal d'éléments non atteint")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            raise ValidationError(f"{path}: nombre maximal d'éléments dépassé")
        if "items" in schema:
            for index, item in enumerate(value):
                validate(item, schema["items"], f"{path}[{index}]")
    if isinstance(value, dict):
        properties = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in value:
                raise ValidationError(f"{path}: champ obligatoire absent: {key}")
        if schema.get("additionalProperties") is False:
            unknown = sorted(set(value) - set(properties))
            if unknown:
                raise ValidationError(f"{path}: champs inconnus: {', '.join(unknown)}")
        for key, child in properties.items():
            if key in value:
                validate(value[key], child, f"{path}.{key}")


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    """Une clé répétée dans un même objet est refusée (la dernière valeur ne gagne plus)."""
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValidationError(f"clé répétée : {key}")
        result[key] = value
    return result


def loads(text: str) -> Any:
    return json.loads(text, object_pairs_hook=reject_duplicate_keys)


def load(path: Path) -> Any:
    try:
        return loads(path.read_text(encoding="utf-8"))
    except ValidationError as exc:
        raise ValidationError(f"{exc} dans {path}") from exc
    except (OSError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ValidationError(f"lecture impossible {path}: {exc}") from exc


def check_schema_keywords(schema: Any, path: str = "$") -> None:
    """Parcours statique : un mot-clé non supporté est refusé même dans une branche que l'exemple ne visite pas."""
    if not isinstance(schema, dict):
        raise ValidationError(f"{path}: sous-schéma non objet")
    unknown = set(schema) - SUPPORTED_KEYS
    if unknown:
        raise ValidationError(f"{path}: mots-clés de schéma non supportés : {', '.join(sorted(unknown))}")
    properties = schema.get("properties", {})
    if not isinstance(properties, dict):
        raise ValidationError(f"{path}.properties: doit être un objet")
    for key, child in properties.items():
        check_schema_keywords(child, f"{path}.properties.{key}")
    if "items" in schema:
        check_schema_keywords(schema["items"], f"{path}.items")


# Contrats dont la racine n'exige aucun objet précis mais « au moins un » (INV-C2-2, rectification R-6).
AT_LEAST_ONE = {"production_contracts": ("creative_direction_set", "ui_ux_reality_pack", "evaluation_case")}
PLACEHOLDERS = {"?", "tbd", "todo", "inconnu", "n/a", "à définir", "a definir", "à déterminer", "a determiner",
                "à compléter", "a completer", "placeholder", "lorem ipsum"}
SOURCE_DATE = re.compile(r"\d{4}(-\d{2}(-\d{2})?)?")


def source_date_ok(value: str) -> bool:
    """AAAA, AAAA-MM ou AAAA-MM-JJ, composants réels (ni mois 13, ni 30 février)."""
    if not SOURCE_DATE.fullmatch(value):
        return False
    parts = [int(part) for part in value.split("-")]
    try:
        date(parts[0], parts[1] if len(parts) > 1 else 1, parts[2] if len(parts) > 2 else 1)
    except ValueError:
        return False
    return True


def check_schema_witness(name: str, schema: dict[str, Any], example: Any) -> None:
    """Témoins négatifs au niveau schéma : rejetés par validate seul, pour leur motif."""
    if not isinstance(example, dict):
        raise ValidationError("témoin de schéma impossible : exemple canonique non objet")
    if schema["required"]:
        first = schema["required"][0]
        witnesses = [(
            {key: value for key, value in example.items() if key != first},
            f"champ obligatoire absent: {first}",
            f"le schéma n'impose pas la clé requise {first}",
        )]
    else:  # racine « au moins un » (R-6) : la première propriété reçoit une valeur de type incompatible
        first = next(key for key in schema["properties"] if key in example)
        witnesses = [({**example, first: 0}, f"$.{first}: type attendu", f"le schéma n'impose pas le type de {first}")]
    if name == "research_brief":  # F-VCT-003
        witnesses.append(({**example, "depth": "IMPOSSIBLE"}, "$.depth: valeur non canonique", "le schéma n'impose pas l'enum de depth"))
    for document, motif, failure in witnesses:
        try:
            validate(document, schema)
        except ValidationError as exc:
            if motif in str(exc):
                continue
            raise ValidationError(f"témoin de schéma non concluant : rejet pour un autre motif ({exc})") from exc
        raise ValidationError(failure)


def load_schema(name: str) -> dict[str, Any]:
    """Chargement gouverné : aucun document n'est jugé avec un schéma vide, incomplet ou hors sous-ensemble."""
    schema_path, example_path = CONTRACTS[name]
    schema = load(schema_path)
    if not isinstance(schema, dict) or not schema:
        raise ValidationError("schéma inopérant : la racine doit être un objet non vide")
    if schema.get("type") != "object":
        raise ValidationError("schéma inopérant : la racine doit déclarer type object")
    required = schema.get("required")
    if not isinstance(required, list):
        raise ValidationError("schéma incomplet : required racine absent ou vide")
    if not required:
        properties = schema.get("properties")
        declared = AT_LEAST_ONE.get(name, ())
        if not declared or schema.get("additionalProperties") is not False or not isinstance(properties, dict) \
                or set(properties) != set(declared):
            raise ValidationError("schéma incomplet : required racine absent ou vide")
    check_schema_keywords(schema)
    check_schema_witness(name, schema, load(example_path))
    return schema


def norm(value: str) -> str:
    return " ".join(value.split()).casefold()


def filled(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and value.strip().casefold() not in PLACEHOLDERS


def check_domain_frame(document: dict[str, Any]) -> None:
    policy = document["policy_profile"]
    if not {norm(item) for item in document["proof_requirements"]} & {norm(item) for item in policy["required_controls"]}:
        raise ValidationError("policy_profile.required_controls doit être relié au plan de preuve")
    risks = {norm(item) for item in document["domain_risks"]}
    controls = {norm(item) for item in policy["required_controls"]}
    covered: set[str] = set()
    for entry in policy["risk_coverage"]:
        risk = norm(entry["risk"])
        if risk not in risks:
            raise ValidationError(f"risk_coverage cite un risque non déclaré : {entry['risk']}")
        control, review = entry.get("control"), entry.get("review")
        if control is not None and norm(control) not in controls:
            raise ValidationError(f"risk_coverage : contrôle inconnu (absent de required_controls) : {control}")
        if not filled(control) and not filled(review):
            raise ValidationError(f"risque sans contrôle ni revue : {entry['risk']}")
        covered.add(risk)
    for risk in document["domain_risks"]:
        if norm(risk) not in covered:
            raise ValidationError(f"risque sans contrôle ni revue : {risk}")
    for index, item in enumerate(document["evidence_plan"]):
        for field in ("method", "scope", "artifact", "limit", "next_proof"):
            if not filled(item.get(field)):
                raise ValidationError(f"evidence_plan[{index}].{field} vide ou placeholder")


def check_research_brief(document: dict[str, Any]) -> None:
    for field in ("uncertainty_before", "uncertainty_after", "stop_condition"):
        if not filled(document[field]):
            raise ValidationError(f"{field} vide ou placeholder")
    entries = document["entries"]
    if document["depth"] in {"targeted", "deep"} and not entries:
        raise ValidationError("recherche activée (depth targeted ou deep) : au moins une entrée exigée")
    if not entries and document["uncertainty_after"] != document["uncertainty_before"]:
        raise ValidationError("sans entrée de recherche, l'incertitude ne peut pas changer (uncertainty_after = uncertainty_before)")
    for entry in entries:
        if not entry["decision_changed"].strip() or not entry["artifact_consequence"].strip():
            raise ValidationError("chaque entrée de recherche doit produire une décision et une conséquence d'artefact")
        if not filled(entry["source"]):
            raise ValidationError(f"source placeholder : {entry['source']!r}")
        date = entry["source_date"].strip()
        if date != "unknown" and not source_date_ok(date):
            raise ValidationError(f"source_date doit être ISO (AAAA, AAAA-MM ou AAAA-MM-JJ) ou unknown : {date}")
        if entry["source_status"] == "verified_in_run" and (not filled(entry.get("source_locator")) or date == "unknown"):
            raise ValidationError("source verified_in_run : exige un locator et une date connue")


def check_creative_direction_set(creative: dict[str, Any]) -> None:
    directions = creative["directions"]
    ids = [item["id"] for item in directions]
    if len(ids) != len(set(ids)):
        raise ValidationError("creative_direction_set.directions exige des ids uniques")
    if creative["selected_direction"] not in set(ids):
        raise ValidationError("creative_direction_set.selected_direction doit référencer une direction existante")
    seen = set()
    for item in directions:
        changes = [norm(change) for change in item["structural_changes"]]
        if len(changes) != len(set(changes)):
            raise ValidationError(f"changements structurels en double dans la direction {item['id']}")
        signature = (norm(item["tension"]), frozenset(changes))
        if signature in seen:
            raise ValidationError(f"directions non distinctes : {item['id']} reprend la tension et les changements d'une autre direction")
        seen.add(signature)


MATRICES = ("state_matrix", "responsive_matrix", "accessibility_basis", "robustness_basis")


def check_ui_ux_reality_pack(reality: dict[str, Any]) -> None:
    if not reality["coverage_map"]:
        raise ValidationError("ui_ux_reality_pack.coverage_map doit contenir au moins une exigence rattachée")
    if not any(item.strip() for name in MATRICES for item in reality[name]):
        raise ValidationError("UI_UX_REALITY_PACK doit déclarer au moins une exigence vérifiable")
    if not filled(reality["expected_scope"]):
        raise ValidationError("ui_ux_reality_pack.expected_scope vide ou placeholder")
    elements = {name: {norm(item) for item in reality[name]} for name in MATRICES}
    covered: dict[str, set[str]] = {name: set() for name in MATRICES}
    for entry in reality["coverage_map"]:
        matrix, _, element = entry["requirement"].partition(":")
        matrix, element = matrix.strip(), norm(element)
        if matrix not in elements or element not in elements[matrix]:
            raise ValidationError(f"coverage_map : exigence absente des matrices déclarées : {entry['requirement']}")
        covered[matrix].add(element)
        if entry["proof_status"] == "N/A-JUSTIFIED" and not filled(entry.get("reason")):
            raise ValidationError(f"coverage_map : N/A-JUSTIFIED exige une raison ({entry['requirement']})")
        if entry["proof_status"] == "OBSERVED" and not filled(reality.get("observed_scope")):
            raise ValidationError(f"coverage_map : une exigence OBSERVED exige observed_scope ({entry['requirement']})")
    for state in reality["state_matrix"]:
        if norm(state) not in covered["state_matrix"]:
            raise ValidationError(f"coverage_map : état non couvert : {state}")
    # « la couverture de chaque exigence » (ACTION/UI-UX-REALITY) vaut pour
    # toute exigence déclarée ; une exigence non vérifiée y figure en NOT-VERIFIED, jamais par omission.
    for name in MATRICES[1:]:
        for item in reality[name]:
            if item.strip() and norm(item) not in covered[name]:
                raise ValidationError(f"coverage_map : exigence déclarée non couverte : {name}: {item}")


def semantic_check(name: str, document: Any) -> None:
    if name == "domain_frame":
        check_domain_frame(document)
    if name == "research_brief":
        check_research_brief(document)
    if name == "production_contracts":
        present = [key for key in AT_LEAST_ONE[name] if key in document]
        if not present:
            raise ValidationError("production_contracts exige au moins un contrat (creative_direction_set, ui_ux_reality_pack ou evaluation_case)")
        if "creative_direction_set" in document:
            check_creative_direction_set(document["creative_direction_set"])
        if "ui_ux_reality_pack" in document:
            check_ui_ux_reality_pack(document["ui_ux_reality_pack"])


DELETE = object()
DF, RB, PC = "domain_frame", "research_brief", "production_contracts"
UI, CS = ("ui_ux_reality_pack",), ("creative_direction_set",)
# Cas unitaires à faute unique (règle A2) : contrat, UNE faute sur l'exemple canonique valide, motif.
UNIT_CASES: list[tuple[Any, ...]] = [
    ("K-02", DF, [(("policy_profile", "required_controls"), ["contrôle sans lien"])], "doit être relié au plan de preuve"),
    ("K-06", PC, [(CS + ("directions", 1, "id"), "A")], "exige des ids uniques"),
    ("K-07", PC, [(CS + ("selected_direction",), "Z")], "doit référencer une direction existante"),
    ("K-09", PC, [(UI + ("coverage_map",), [])], "nombre minimal d'éléments non atteint"),
    ("C2-2", PC, [(("creative_direction_set",), DELETE), (("ui_ux_reality_pack",), DELETE), (("evaluation_case",), DELETE)], "au moins un contrat"),
    ("C2-3", PC, [(UI + ("coverage_map", 0, "proof_status"), "N/A-JUSTIFIED")], "N/A-JUSTIFIED exige une raison"),
    ("C2-4", PC, [(UI + ("observed_scope",), None)], "exige observed_scope"),
    ("C3-1", PC, [(CS + ("directions", 1, "tension"), None), (CS + ("directions", 1, "structural_changes"), None)], "directions non distinctes"),
    ("C3-2", PC, [(CS + ("directions", 0, "structural_changes", 1), None)], "changements structurels en double"),
    ("MOB-ONE", PC, [(CS + ("directions",), None)], "nombre minimal d'éléments non atteint"),
    ("MOB-EMPTY", PC, [(CS + ("directions",), [])], "nombre minimal d'éléments non atteint"),
    ("C9-1", DF, [(("domain_risks",), None)], "risque sans contrôle ni revue"),
    ("C9-1b", DF, [(("policy_profile", "risk_coverage", 0, "control"), "contrôle inventé")], "contrôle inconnu"),
    ("C9-3", PC, [(UI + ("coverage_map", 0, "requirement"), "state_matrix: loading des données source")], "exigence absente des matrices"),
    ("C9-3b", PC, [(UI + ("coverage_map",), None)], "état non couvert"),
    ("C15-1", PC, [(UI + ("coverage_map",), None)], "exigence déclarée non couverte"),
    ("C9-4", RB, [(("entries", 0, "source"), "?")], "source placeholder"),
    ("C9-4b", RB, [(("entries", 0, "source_status"), "verified_in_run"), (("entries", 0, "source_locator"), DELETE)], "exige un locator"),
    ("C9-4c", RB, [(("entries", 0, "source_date"), "septembre")], "source_date doit être ISO"),
    # Une date de forme ISO mais impossible est refusée.
    ("C19-1", RB, [(("entries", 0, "source_date"), "2026-02-30")], "source_date doit être ISO"),
    ("C19-2", RB, [(("entries", 0, "source_date"), "2026-13")], "source_date doit être ISO"),
    ("E2-1", DF, [(("evidence_plan", 0, "method"), "à déterminer")], "evidence_plan[0].method vide ou placeholder"),
    ("E2-2", RB, [(("entries",), [])], "au moins une entrée exigée"),
    ("E2-2b", RB, [(("depth",), "none"), (("entries",), [])], "l'incertitude ne peut pas changer"),
    ("E2-2c", RB, [(("stop_condition",), "à déterminer")], "stop_condition vide ou placeholder"),
]
# Valeurs dépendantes de l'exemple, calculées au moment du cas (None ci-dessus).
DERIVED = {
    ("MOB-ONE", 0): lambda d: d["creative_direction_set"]["directions"][:1],
    ("C3-1", 0): lambda d: d["creative_direction_set"]["directions"][0]["tension"],
    ("C3-1", 1): lambda d: list(d["creative_direction_set"]["directions"][0]["structural_changes"]),
    ("C3-2", 0): lambda d: d["creative_direction_set"]["directions"][0]["structural_changes"][0].upper(),
    ("C9-1", 0): lambda d: d["domain_risks"] + ["exposition de données personnelles"],
    ("C9-3b", 0): lambda d: [e for e in d["ui_ux_reality_pack"]["coverage_map"] if not e["requirement"].startswith("state_matrix: loading")],
    ("C15-1", 0): lambda d: [e for e in d["ui_ux_reality_pack"]["coverage_map"] if not e["requirement"].startswith("robustness_basis: libellés longs")],
}


def apply_edit(document: Any, path: tuple[Any, ...], value: Any) -> None:
    node = document
    for key in path[:-1]:
        node = node[key]
    if value is DELETE:
        del node[path[-1]]
    else:
        node[path[-1]] = copy.deepcopy(value)


def check_unit_cases(schemas: dict[str, dict[str, Any]], documents: dict[str, Any]) -> list[str]:
    errors, passed = [], 0
    for case_id, name, faults, motif in UNIT_CASES:
        document = copy.deepcopy(documents[name])
        try:
            for index, (path, value) in enumerate(faults):
                apply_edit(document, path, DERIVED[(case_id, index)](document) if value is None and (case_id, index) in DERIVED else value)
        except (KeyError, IndexError, TypeError) as exc:
            errors.append(f"cas unitaire {case_id} : chemin de faute introuvable ({exc})")
            continue
        try:
            validate(document, schemas[name])
            semantic_check(name, document)
        except ValidationError as exc:
            if motif in str(exc):
                passed += 1
            else:
                errors.append(f"cas unitaire {case_id} : attendu {motif!r}, obtenu {str(exc)!r}")
            continue
        errors.append(f"cas unitaire {case_id} : faute unique acceptée ({motif})")
    print(f"+ cas unitaires : {passed}/{len(UNIT_CASES)}")
    return errors


def check_direction_cardinality(schema: dict[str, Any], original: dict[str, Any]) -> list[str]:
    """Une comparaison conditionnelle peut dépasser trois positions ; aucun contrat universel."""
    cases = []
    for count in (4, 8):
        document = copy.deepcopy(original)
        creative = document["creative_direction_set"]
        creative["directions"] = creative["directions"][:2]
        for index in range(2, count):
            item = copy.deepcopy(creative["directions"][0])
            item.update(id=f"fixture-{index}", tension=f"Tension distincte du cas synthétique {index}",
                        structural_changes=[f"Relation distincte du cas synthétique {index}"])
            creative["directions"].append(item)
        cases.append((f"{count} positions distinctes", document))
    without = copy.deepcopy(original)
    del without["creative_direction_set"]
    cases.append(("contrat créatif absent, autre contrat fourni", without))
    errors = []
    for label, document in cases:
        try:
            validate(document, schema)
            semantic_check("production_contracts", document)
        except ValidationError as exc:
            errors.append(f"cardinalité conditionnelle — {label} : {exc}")
    print(f"+ cardinalité conditionnelle : {len(cases) - len(errors)}/{len(cases)}")
    return errors


def detect_type(document: Any) -> str:
    """Famille de contrat reconnue par ses clés racines ; une seule doit correspondre."""
    if not isinstance(document, dict) or not document:
        raise ValidationError("type indéterminé : document vide ou non objet ; utiliser --type")
    matches = []
    for name, (schema_path, _) in CONTRACTS.items():
        schema = load(schema_path)
        if not isinstance(schema, dict) or not isinstance(schema.get("properties", {}), dict):
            raise ValidationError(f"schéma inopérant : {schema_path.name} doit être un objet à properties objet")  # C20
        properties = schema.get("properties", {})
        if set(document) <= set(properties):
            matches.append(name)
    if len(matches) != 1:
        raise ValidationError(f"type ambigu ou inconnu ({', '.join(matches) or 'aucun'}) : utiliser --type")
    return matches[0]


def validate_single_path(path: Path, name: str | None = None) -> int:
    try:
        document = load(path)
        name = name or detect_type(document)
        schema = load_schema(name)
        validate(document, schema)
        semantic_check(name, document)
    except (OSError, ValidationError) as exc:
        print("CONTRACT VALIDATION FAILED")
        print(f"- {exc}")
        return 1
    print(f"CONTRACT VALIDATION PASSED — fichier ciblé ({name}) : {path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Valide les contrats de production, ou un fichier de contrat ciblé.")
    parser.add_argument("path", nargs="?", type=Path, help="fichier JSON à valider seul (dans ou hors du package) ; sans argument, exécute la suite complète")
    parser.add_argument("--type", choices=sorted(CONTRACTS), help="famille du contrat ; sans --type, détectée par les clés racines")
    args = parser.parse_args(argv)
    if args.path is not None:
        return validate_single_path(args.path.expanduser().resolve(), args.type)
    if args.type is not None:
        print("CONTRACT VALIDATION FAILED")
        print("- --type exige un fichier JSON ciblé")
        return 1

    errors: list[str] = []
    schemas: dict[str, dict[str, Any]] = {}
    documents: dict[str, Any] = {}
    for name, (_, example_path) in CONTRACTS.items():
        try:
            schema = load_schema(name)
            document = load(example_path)
            schemas[name] = schema
            documents[name] = document
            validate(document, schema)
            semantic_check(name, document)
            print(f"+ {name}: valid")
        except ValidationError as exc:
            errors.append(f"{name}: {exc}")
    if not errors:
        errors.extend(check_unit_cases(schemas, documents))
        errors.extend(check_direction_cardinality(schemas["production_contracts"], documents["production_contracts"]))
    try:  # témoin de clé répétée
        loads('{"depth": "IMPOSSIBLE", "depth": "targeted"}')
        errors.append("témoin C12 : une clé répétée est acceptée")
    except ValidationError:
        print("+ clés répétées refusées : 1/1")
    if errors:
        print("CONTRACT VALIDATION FAILED")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("CONTRACT VALIDATION PASSED — domain, research, creative, UI/UX and evaluation contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
