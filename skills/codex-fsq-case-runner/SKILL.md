---
name: codex-fsq-case-runner
description: Use when running, smoke-testing, selecting, validating, manifesting, or collecting evidence for FSQ AI Test DSL Codex YAML cases across Windows, macOS, iOS, or Android.
---

# Codex FSQ Case Runner

## Overview

Run converted FSQ AI Test DSL cases through platform-default MCP backends, while preserving manifests, logs, and evidence for manual analysis. Prefer small smoke runs first, then expand to platform or area batches.

## Backend Defaults

Use platform to choose backend automatically:

| Platform | Backend |
| --- | --- |
| windows | `pywinauto-mcp` |
| macos | `appium-mcp` |
| ios | `appium-mcp` |
| android | `appium-mcp` |

## Daily Workflow

1. List candidate cases.
2. Validate selected case YAML against `docs/codex-fsq-ai-test-dsl-v1.schema.json`.
3. Generate a run manifest under `runs/codex-<timestamp>/manifest.json`.
4. Run one or more cases through `run_fsq_cases.py`.
5. Inspect `runs/codex-<timestamp>/results.jsonl`, `logs/`, and `evidence/`.
6. Do not edit case YAML automatically after a failure.

## Commands

List cases:

```bash
python3 skills/codex-fsq-case-runner/scripts/list_fsq_cases.py \
  --cases fsq-testcases \
  --platform windows \
  --area settings
```

Create a manifest only:

```bash
python3 skills/codex-fsq-case-runner/scripts/make_run_manifest.py \
  --cases fsq-testcases \
  --platform windows \
  --area settings \
  --limit 3
```

Run a single case with a concrete runner command:

```bash
python3 skills/codex-fsq-case-runner/scripts/run_fsq_cases.py \
  --cases fsq-testcases/windows/settings/open_settings_page.codex.yaml \
  --runner-command "<runner> --case {case} --backend {backend} --output {output} --manifest {manifest}"
```

Run a small batch:

```bash
python3 skills/codex-fsq-case-runner/scripts/run_fsq_cases.py \
  --cases fsq-testcases \
  --platform windows \
  --area settings \
  --limit 3 \
  --runner-command "<runner> --case {case} --backend {backend} --output {output} --manifest {manifest}"
```

Run one Android case with the repository-owned simple Appium runner and per-step accessibility evidence:

```bash
ANDROID_UDID=<device-id> \
python3 skills/codex-fsq-case-runner/scripts/run_fsq_cases.py \
  --cases fsq-testcases/android/bottom_bar/access_settings_through_overflow_menu.codex.yaml \
  --run-id codex-android-simple-smoke \
  --runner-command 'ANDROID_UDID=<device-id> python3 skills/codex-fsq-case-runner/scripts/codex_android_simple_runner.py --case {case} --backend {backend} --output {output} --manifest {manifest}'
```

The simple Android runner is not an MCP adapter. It uses Appium Python client against an Appium server, captures `before` and `after` accessibility XML for every step, and captures `failed` XML plus a `failureClass` when a step fails. Screenshots are optional and disabled by default.

If no `--runner-command` is provided, the script still validates cases and creates a run bundle, then records each selected case as `skipped` with a missing runner message.

## References

Read these only when needed:

- `references/environment.md`: platform environment setup checks.
- `references/runner-adapters.md`: backend defaults and command-template variables.
- `references/evidence-and-repair.md`: failure evidence and repair discipline.

## Rules

- Do not hardcode secrets, device IDs, or private runner endpoints.
- Do not screenshot-guess coordinates under a non-vision model.
- Do not convert runner failures into case edits automatically.
- Treat cases as isolated: each case should start with `launchApp` and end with `killApp`.
- Keep run outputs under `runs/`, which should be treated as generated evidence.
