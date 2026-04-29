#!/usr/bin/env python3
"""Create an FSQ Codex run manifest."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from fsq_case_runner_lib import build_manifest, discover_cases, make_run_id, write_json


def main() -> int:
    parser = argparse.ArgumentParser(description="Create FSQ Codex run manifest")
    parser.add_argument("--cases", default="fsq-testcases", help="Case file or root directory")
    parser.add_argument("--platform", help="Filter by platform")
    parser.add_argument("--area", help="Filter by area directory")
    parser.add_argument("--tag", action="append", default=[], help="Require tag; repeatable")
    parser.add_argument("--limit", type=int, help="Maximum number of cases")
    parser.add_argument("--schema", default="docs/codex-fsq-ai-test-dsl-v1.schema.json", help="FSQ schema path")
    parser.add_argument("--output-root", default="runs", help="Run output root")
    parser.add_argument("--run-id", help="Run id; defaults to codex timestamp")
    args = parser.parse_args()

    cases = discover_cases(args.cases, args.platform, args.area, args.tag, args.limit)
    if not cases:
        print("No cases matched selection.", file=sys.stderr)
        return 1

    run_id = args.run_id or make_run_id()
    run_dir = Path(args.output_root) / run_id
    manifest = build_manifest(cases, args.schema, args.output_root, run_id)
    write_json(run_dir / "manifest.json", manifest)
    print(run_dir / "manifest.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
