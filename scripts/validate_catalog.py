#!/usr/bin/env python3
"""Validate data/dataset_catalog.csv against the controlled vocabularies.

Checks performed:
  * the CSV parses and has exactly the expected columns
  * dataset_id values are unique positive integers
  * controlled fields use only allowed vocabulary terms
  * publication_year and sample_size look sane
  * every non-example row has a matching dataset card in dataset_cards/

Exit code is 0 when everything passes, 1 otherwise. No third-party
dependencies — runs on a plain Python 3 install.

Usage:
    python scripts/validate_catalog.py
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CATALOG = REPO_ROOT / "data" / "dataset_catalog.csv"
VOCAB = REPO_ROOT / "data" / "controlled_vocabularies.csv"
CARDS_DIR = REPO_ROOT / "dataset_cards"

EXPECTED_COLUMNS = [
    "dataset_id", "accession", "title", "species", "common_name", "life_stage",
    "stressor", "stressor_level", "exposure_duration", "tissue", "omics_type",
    "platform", "sample_size", "location", "publication_year", "publication_doi",
    "data_repository", "has_raw_data", "notes", "curator", "status",
]

# Which catalog columns are constrained by controlled_vocabularies.csv.
CONTROLLED_FIELDS = [
    "stressor", "life_stage", "omics_type", "data_repository",
    "has_raw_data", "status",
]

NA_VALUES = {"", "na", "n/a", "none", "unknown"}


def load_vocabularies() -> dict[str, set[str]]:
    """Return {field: {allowed terms}} from controlled_vocabularies.csv."""
    vocab: dict[str, set[str]] = {}
    with VOCAB.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            field = (row.get("field") or "").strip()
            term = (row.get("term") or "").strip()
            if field and term:
                vocab.setdefault(field, set()).add(term)
    return vocab


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not CATALOG.exists():
        print(f"ERROR: {CATALOG} not found")
        return 1

    vocab = load_vocabularies()

    with CATALOG.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        header = reader.fieldnames or []
        if header != EXPECTED_COLUMNS:
            errors.append(
                "Header does not match expected columns.\n"
                f"  expected: {EXPECTED_COLUMNS}\n"
                f"  found:    {header}"
            )
            # Header mismatch makes row checks unreliable; report and stop.
            _report(errors, warnings)
            return 1

        rows = list(reader)

    seen_ids: dict[str, int] = {}
    for i, row in enumerate(rows, start=2):  # line 1 is the header
        rid = (row.get("dataset_id") or "").strip()
        status = (row.get("status") or "").strip().lower()

        # dataset_id: unique positive integer
        if not rid.isdigit() or int(rid) <= 0:
            errors.append(f"line {i}: dataset_id '{rid}' is not a positive integer")
        elif rid in seen_ids:
            errors.append(f"line {i}: duplicate dataset_id '{rid}' (also line {seen_ids[rid]})")
        else:
            seen_ids[rid] = i

        # controlled vocabulary fields
        for field in CONTROLLED_FIELDS:
            value = (row.get(field) or "").strip()
            allowed = vocab.get(field, set())
            if value and allowed and value not in allowed:
                errors.append(
                    f"line {i}: {field}='{value}' is not in the controlled vocabulary "
                    f"({', '.join(sorted(allowed))})"
                )

        # sample_size: integer if provided
        ss = (row.get("sample_size") or "").strip()
        if ss.lower() not in NA_VALUES and not ss.isdigit():
            warnings.append(f"line {i}: sample_size '{ss}' is not an integer")

        # publication_year: 4-digit year in a plausible range
        year = (row.get("publication_year") or "").strip()
        if year.lower() not in NA_VALUES:
            if not (year.isdigit() and 1990 <= int(year) <= 2100):
                warnings.append(f"line {i}: publication_year '{year}' looks off")

        # accession present
        if not (row.get("accession") or "").strip():
            errors.append(f"line {i}: missing accession")

        # every real (non-example) row should have a dataset card
        if status != "example":
            accession = (row.get("accession") or "").strip()
            if accession:
                card = CARDS_DIR / f"{accession}.md"
                if not card.exists():
                    warnings.append(
                        f"line {i}: no dataset card found at "
                        f"dataset_cards/{accession}.md"
                    )

    ok = _report(errors, warnings)
    print(f"\nChecked {len(rows)} rows.")
    return 0 if ok else 1


def _report(errors: list[str], warnings: list[str]) -> bool:
    for w in warnings:
        print(f"WARN:  {w}")
    for e in errors:
        print(f"ERROR: {e}")
    if not errors and not warnings:
        print("All checks passed. ✅")
    elif not errors:
        print(f"\n{len(warnings)} warning(s), no errors. ✅")
    else:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s). ❌")
    return not errors


if __name__ == "__main__":
    sys.exit(main())
