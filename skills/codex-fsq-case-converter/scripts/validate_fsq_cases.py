#!/usr/bin/env python3
"""Validate FSQ AI Test DSL Codex YAML files against the JSON Schema.

Raw testcase files are YAML multi-documents:
  doc 1: config
  doc 2: command list

The schema validates the normalized model:
  {"config": doc1, "commands": doc2}
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator


def iter_case_files(root: Path) -> list[Path]:
    if root.is_file():
        return [root]
    return sorted(root.glob("**/*.codex.yaml"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate FSQ Codex YAML testcases")
    parser.add_argument("--schema", required=True, type=Path, help="Path to codex-fsq-ai-test-dsl-v1.schema.json")
    parser.add_argument("--cases", required=True, type=Path, help="Case file or directory containing *.codex.yaml")
    parser.add_argument("--strict-naming", action="store_true", help="Require every case filename to end with .codex.yaml")
    args = parser.parse_args()

    schema = json.loads(args.schema.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    paths = iter_case_files(args.cases)
    failures: list[tuple[Path, list[str]]] = []

    for path in paths:
        messages: list[str] = []
        if args.strict_naming and not path.name.endswith(".codex.yaml"):
            messages.append("filename must end with .codex.yaml")
        try:
            docs = list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
        except Exception as exc:  # noqa: BLE001 - CLI should report all parse errors plainly.
            failures.append((path, [f"YAML parse error: {exc}"]))
            continue

        if len(docs) != 2:
            messages.append(f"expected exactly 2 YAML documents, got {len(docs)}")
        else:
            model = {"config": docs[0], "commands": docs[1]}
            for error in sorted(validator.iter_errors(model), key=lambda e: list(e.path)):
                location = "/".join(map(str, error.path)) or "<root>"
                messages.append(f"{location}: {error.message}")

        text = path.read_text(encoding="utf-8")
        if "&id" in text or "*id" in text:
            messages.append("YAML contains generated anchors/aliases; rewrite without aliases for reviewability")
        if "optional: true" in text:
            messages.append("contains optional: true; confirm the source explicitly makes this check optional")
        if "point:" in text or "\n  x:" in text or "\n  y:" in text:
            messages.append("contains coordinate-like fields; confirm this is intentional and not screenshot guessing")

        if messages:
            failures.append((path, messages))

    print(f"total={len(paths)} failed={len(failures)}")
    for path, messages in failures:
        print(path)
        for message in messages[:10]:
            print(f"  - {message}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
