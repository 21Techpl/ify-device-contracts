"""Mechanical gate for the device-contract repo (required check: ci/test).

Checks, in order:
1. every tracked JSON file parses;
2. every schema under schemas/ is a valid Draft-07 JSON Schema;
3. VERSION exists, is semver, and its major matches every schema $id major
   (README rule: breaking changes bump the major version).

Run: python scripts/validate.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from jsonschema import Draft7Validator

SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    errors: list[str] = []

    vtext = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not SEMVER.match(vtext):
        errors.append(f"VERSION is not semver: {vtext!r}")
        v_major = None
    else:
        v_major = int(vtext.split(".")[0])

    json_files = sorted(p for p in ROOT.rglob("*.json") if ".git" not in p.parts)
    if not json_files:
        errors.append("no JSON files found; repository looks empty")

    for path in json_files:
        rel = path.relative_to(ROOT)
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{rel}: not valid JSON: {exc}")
            continue

        if path.parent.name == "schemas":
            try:
                Draft7Validator.check_schema(data)
            except Exception as exc:  # jsonschema.SchemaError or TypeError
                errors.append(f"{rel}: invalid Draft-07 schema: {exc}")
                continue
            if "$schema" in data and "draft-07" not in str(data["$schema"]):
                errors.append(f"{rel}: unexpected $schema (expected draft-07): {data['$schema']}")
            if "$id" in data:
                tail = str(data["$id"]).split("/")[-1]
                if not SEMVER.match(tail):
                    errors.append(f"{rel}: $id tail is not semver: {tail!r}")
                elif v_major is not None and int(tail.split(".")[0]) != v_major:
                    errors.append(
                        f"{rel}: $id major ({tail}) does not match VERSION major ({vtext})"
                    )

    if errors:
        print("BLOCKED: contract validation failed:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"OK: {len(json_files)} JSON file(s) parsed, schemas valid, VERSION {vtext} in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
