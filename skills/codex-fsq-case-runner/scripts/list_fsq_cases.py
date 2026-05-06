#!/usr/bin/env python3
"""List FSQ Codex testcase files."""

from __future__ import annotations

import argparse
import json
import sys

from fsq_case_runner_lib import discover_cases


def main() -> int:
    parser = argparse.ArgumentParser(description="List FSQ Codex cases")
    parser.add_argument("--cases", default="fsq-testcases", help="Case file or root directory")
    parser.add_argument("--platform", help="Filter by platform")
    parser.add_argument("--area", help="Filter by area directory")
    parser.add_argument("--tag", action="append", default=[], help="Require tag; repeatable")
    parser.add_argument("--exclude-tag", action="append", default=[], help="Exclude tag; repeatable")
    parser.add_argument("--limit", type=int, help="Maximum number of cases")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    cases = discover_cases(args.cases, args.platform, args.area, args.tag, args.exclude_tag, args.limit)
    if args.json:
        print(json.dumps(cases, indent=2, sort_keys=True))
        return 0

    if not cases:
        print("No cases matched selection.", file=sys.stderr)
        return 1

    for item in cases:
        tags = ",".join(item.get("tags", []))
        print(f"{item['platform']}\t{item.get('area') or '-'}\t{tags}\t{item['path']}\t{item['name']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
