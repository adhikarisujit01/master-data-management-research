"""Small, auditable master-data integration demonstration.

The data is synthetic. An exact normalized email match is used as the
join key; this is NOT a general probabilistic entity-resolution system.
"""
from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path


def clean(value: str) -> str:
    return " ".join(value.strip().split())


def normalize_email(value: str) -> str:
    return clean(value).casefold()


def build_view(rows: list[dict[str, str]]) -> list[dict]:
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        email = normalize_email(row["email"])
        if not email:
            raise ValueError(f"Missing email in source record: {row['record_id']}")
        groups[email].append(row)

    results = []
    for email, records in sorted(groups.items()):
        # Prefer CRM's display name, if present, but preserve all provenance.
        ordered = sorted(records, key=lambda r: (r["source"] != "crm", r["record_id"]))
        names = [clean(r["name"]) for r in ordered if clean(r["name"])]
        cities = [clean(r["city"]) for r in ordered if clean(r["city"])]
        results.append({
            "email": email,
            "name": names[0] if names else None,
            "city": cities[0] if cities else None,
            "source_record_ids": [f"{r['source']}:{r['record_id']}" for r in ordered],
            "source_count": len(ordered),
            "conflicting_names": len({n.casefold() for n in names}) > 1,
            "conflicting_cities": len({c.casefold() for c in cities}) > 1,
        })
    return results


def evaluate(rows: list[dict[str, str]], canonical: list[dict]) -> dict:
    count = len(rows)
    duplicate_excess = count - len(canonical)
    return {
        "input_records": count,
        "canonical_entities": len(canonical),
        "duplicate_excess_under_exact_email_key": duplicate_excess,
        "exact_email_coverage": sum(bool(normalize_email(r["email"])) for r in rows) / count if count else 0,
        "canonical_city_completeness": sum(bool(r["city"]) for r in canonical) / len(canonical) if canonical else 0,
        "name_conflict_groups": sum(bool(r["conflicting_names"]) for r in canonical),
        "note": "Descriptive statistics on synthetic records, not an external benchmark.",
    }


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "data" / "synthetic_customers.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    view = build_view(rows)
    print(json.dumps({"metrics": evaluate(rows, view), "canonical_view": view}, indent=2))


if __name__ == "__main__":
    main()
