#!/usr/bin/env python3
"""Run FSQ Codex cases through a command-template wrapper."""

from __future__ import annotations

import argparse
from pathlib import Path
import shlex
import subprocess
import sys
import time

from fsq_case_runner_lib import (
    append_jsonl,
    build_manifest,
    discover_cases,
    make_run_id,
    slug_path,
    write_json,
)

VALIDATOR = Path("skills/codex-fsq-case-converter/scripts/validate_fsq_cases.py")


def validate_case(schema: str, case_path: str) -> tuple[bool, str]:
    cmd = [sys.executable, str(VALIDATOR), "--schema", schema, "--cases", case_path]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    output = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode == 0, output.strip()


def render_command(template: str, case: dict, output_dir: Path, manifest_path: Path) -> str:
    return template.format(
        case=shlex.quote(case["path"]),
        backend=shlex.quote(case["backend"]),
        output=shlex.quote(str(output_dir)),
        manifest=shlex.quote(str(manifest_path)),
    )


def write_log(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text or "", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run FSQ Codex cases")
    parser.add_argument("--cases", default="fsq-testcases", help="Case file or root directory")
    parser.add_argument("--platform", help="Filter by platform")
    parser.add_argument("--area", help="Filter by area directory")
    parser.add_argument("--tag", action="append", default=[], help="Require tag; repeatable")
    parser.add_argument("--exclude-tag", action="append", default=[], help="Exclude tag; repeatable")
    parser.add_argument("--limit", type=int, help="Maximum number of cases")
    parser.add_argument("--schema", default="docs/codex-fsq-ai-test-dsl-v1.schema.json", help="FSQ schema path")
    parser.add_argument("--output-root", default="runs", help="Run output root")
    parser.add_argument("--run-id", help="Run id; defaults to codex timestamp")
    parser.add_argument("--runner-command", help="Command template using {case}, {backend}, {output}, {manifest}")
    args = parser.parse_args()

    cases = discover_cases(args.cases, args.platform, args.area, args.tag, args.exclude_tag, args.limit)
    if not cases:
        print("No cases matched selection.", file=sys.stderr)
        return 1

    run_id = args.run_id or make_run_id()
    run_dir = Path(args.output_root) / run_id
    logs_dir = run_dir / "logs"
    evidence_dir = run_dir / "evidence"
    logs_dir.mkdir(parents=True, exist_ok=True)
    evidence_dir.mkdir(parents=True, exist_ok=True)

    manifest = build_manifest(cases, args.schema, args.output_root, run_id)
    manifest_path = run_dir / "manifest.json"
    write_json(manifest_path, manifest)
    results_path = run_dir / "results.jsonl"

    final_code = 0
    for case in cases:
        case_slug = slug_path(case["path"])
        case_output = evidence_dir / case_slug
        case_output.mkdir(parents=True, exist_ok=True)
        start = time.monotonic()

        valid, validation_output = validate_case(args.schema, case["path"])
        write_log(logs_dir / f"{case_slug}.validation.log", validation_output + "\n")
        if not valid:
            duration_ms = int((time.monotonic() - start) * 1000)
            result = {
                "case": case["path"],
                "platform": case["platform"],
                "backend": case["backend"],
                "status": "failed",
                "exitCode": 1,
                "durationMs": duration_ms,
                "outputDir": str(case_output),
                "message": "schema validation failed",
            }
            append_jsonl(results_path, result)
            final_code = 1
            continue

        if not args.runner_command:
            duration_ms = int((time.monotonic() - start) * 1000)
            message = f"runner command missing for backend {case['backend']}"
            result = {
                "case": case["path"],
                "platform": case["platform"],
                "backend": case["backend"],
                "status": "skipped",
                "exitCode": None,
                "durationMs": duration_ms,
                "outputDir": str(case_output),
                "message": message,
            }
            append_jsonl(results_path, result)
            write_log(logs_dir / f"{case_slug}.stdout.log", "")
            write_log(logs_dir / f"{case_slug}.stderr.log", message + "\n")
            final_code = max(final_code, 2)
            continue

        rendered = render_command(args.runner_command, case, case_output, manifest_path)
        write_log(logs_dir / f"{case_slug}.command.txt", rendered + "\n")
        proc = subprocess.run(rendered, shell=True, capture_output=True, text=True, check=False)
        duration_ms = int((time.monotonic() - start) * 1000)
        write_log(logs_dir / f"{case_slug}.stdout.log", proc.stdout)
        write_log(logs_dir / f"{case_slug}.stderr.log", proc.stderr)
        status = "passed" if proc.returncode == 0 else "failed"
        result = {
            "case": case["path"],
            "platform": case["platform"],
            "backend": case["backend"],
            "status": status,
            "exitCode": proc.returncode,
            "durationMs": duration_ms,
            "outputDir": str(case_output),
        }
        append_jsonl(results_path, result)
        if proc.returncode != 0:
            final_code = 1

    print(f"runDir={run_dir}")
    print(f"manifest={manifest_path}")
    print(f"results={results_path}")
    return final_code


if __name__ == "__main__":
    sys.exit(main())
