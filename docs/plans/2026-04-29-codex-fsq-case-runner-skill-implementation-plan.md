# Codex FSQ Case Runner Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a repository-local `codex-fsq-case-runner` skill that can select, validate, manifest, and dispatch FSQ DSL cases through platform-default MCP backends.

**Architecture:** The skill is source-only under `skills/codex-fsq-case-runner/`. `SKILL.md` contains the daily workflow; `references/` contains environment, adapter, and evidence guidance; `scripts/` contains deterministic Python helpers for listing cases, creating manifests, and running command-template wrappers.

**Tech Stack:** Python 3, PyYAML, jsonschema, repository FSQ DSL schema, Markdown skills.

---

## File Structure

- Create `skills/codex-fsq-case-runner/SKILL.md`: skill trigger metadata and daily run workflow.
- Create `skills/codex-fsq-case-runner/references/environment.md`: environment checklist for Appium MCP and pywinauto MCP.
- Create `skills/codex-fsq-case-runner/references/runner-adapters.md`: platform-to-backend mapping and command-template variables.
- Create `skills/codex-fsq-case-runner/references/evidence-and-repair.md`: evidence layout and failure handling discipline.
- Create `skills/codex-fsq-case-runner/scripts/fsq_case_runner_lib.py`: shared Python helpers for case discovery, YAML metadata loading, backend inference, run IDs, and JSON writing.
- Create `skills/codex-fsq-case-runner/scripts/list_fsq_cases.py`: CLI for listing selected cases.
- Create `skills/codex-fsq-case-runner/scripts/make_run_manifest.py`: CLI for creating run manifests.
- Create `skills/codex-fsq-case-runner/scripts/run_fsq_cases.py`: CLI wrapper for validation, manifest creation, command-template execution, logs, and results.

### Task 1: Create Skill Documentation

**Files:**
- Create: `skills/codex-fsq-case-runner/SKILL.md`
- Create: `skills/codex-fsq-case-runner/references/environment.md`
- Create: `skills/codex-fsq-case-runner/references/runner-adapters.md`
- Create: `skills/codex-fsq-case-runner/references/evidence-and-repair.md`

- [ ] **Step 1: Create directories**

Run:

```bash
mkdir -p skills/codex-fsq-case-runner/references skills/codex-fsq-case-runner/scripts
```

Expected: directories exist.

- [ ] **Step 2: Write `SKILL.md`**

Create `skills/codex-fsq-case-runner/SKILL.md` with:

```markdown
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
- Keep run outputs under `runs/`, which should be treated as generated evidence.
```

- [ ] **Step 3: Write references**

Create the three reference files with concise sections matching `docs/plans/2026-04-29-codex-fsq-case-runner-skill-design.md`:

- `environment.md`: Python deps, Appium MCP, pywinauto MCP, Edge app/accessibility, device/simulator checks.
- `runner-adapters.md`: platform backend table, template variables, examples.
- `evidence-and-repair.md`: run bundle layout, result status, failure categories, no auto repair edits.

- [ ] **Step 4: Validate skill metadata**

Run:

```bash
python3 /Users/qunmi/.agents/skills/skill-creator/scripts/quick_validate.py skills/codex-fsq-case-runner
```

Expected: `Skill is valid!`

### Task 2: Implement Shared Runner Library

**Files:**
- Create: `skills/codex-fsq-case-runner/scripts/fsq_case_runner_lib.py`

- [ ] **Step 1: Write library**

Implement functions:

```python
def discover_cases(cases_root, platform=None, area=None, tags=None, limit=None): ...
def load_case_metadata(path): ...
def infer_backend(platform): ...
def make_run_id(now=None): ...
def slug_path(path): ...
def write_json(path, data): ...
def append_jsonl(path, item): ...
```

Use backend map:

```python
BACKENDS = {
    "windows": "pywinauto-mcp",
    "macos": "appium-mcp",
    "ios": "appium-mcp",
    "android": "appium-mcp",
}
```

- [ ] **Step 2: Run syntax check**

Run:

```bash
python3 -m py_compile skills/codex-fsq-case-runner/scripts/fsq_case_runner_lib.py
```

Expected: exit code `0`.

### Task 3: Implement Listing CLI

**Files:**
- Create: `skills/codex-fsq-case-runner/scripts/list_fsq_cases.py`

- [ ] **Step 1: Write CLI**

Implement arguments:

```text
--cases default fsq-testcases
--platform optional
--area optional
--tag repeatable
--limit optional int
--json optional flag
```

Text output columns: platform, area, tags, path, name.

- [ ] **Step 2: Verify text output**

Run:

```bash
python3 skills/codex-fsq-case-runner/scripts/list_fsq_cases.py --cases fsq-testcases --platform windows --area settings --limit 2
```

Expected: two Windows settings case rows.

- [ ] **Step 3: Verify JSON output**

Run:

```bash
python3 skills/codex-fsq-case-runner/scripts/list_fsq_cases.py --cases fsq-testcases --platform android --limit 1 --json
```

Expected: JSON array with one Android case object.

### Task 4: Implement Manifest CLI

**Files:**
- Create: `skills/codex-fsq-case-runner/scripts/make_run_manifest.py`

- [ ] **Step 1: Write CLI**

Implement arguments:

```text
--cases default fsq-testcases
--platform optional
--area optional
--tag repeatable
--limit optional int
--schema default docs/codex-fsq-ai-test-dsl-v1.schema.json
--output-root default runs
--run-id optional
```

Create `runs/<run-id>/manifest.json` with run metadata and selected cases.

- [ ] **Step 2: Verify manifest creation**

Run:

```bash
python3 skills/codex-fsq-case-runner/scripts/make_run_manifest.py --cases fsq-testcases --platform windows --area settings --limit 2 --run-id codex-test-manifest
```

Expected: `runs/codex-test-manifest/manifest.json` exists and contains two cases with backend `pywinauto-mcp`.

### Task 5: Implement Run Wrapper CLI

**Files:**
- Create: `skills/codex-fsq-case-runner/scripts/run_fsq_cases.py`

- [ ] **Step 1: Write CLI**

Implement arguments:

```text
--cases default fsq-testcases
--platform optional
--area optional
--tag repeatable
--limit optional int
--schema default docs/codex-fsq-ai-test-dsl-v1.schema.json
--output-root default runs
--run-id optional
--runner-command optional string
```

Workflow:

1. Discover selected cases.
2. Validate selected YAML by invoking `skills/codex-fsq-case-converter/scripts/validate_fsq_cases.py` once per file or against a temporary selected root/list.
3. Create run directories: `logs/`, `evidence/`.
4. Write manifest.
5. For each case, create per-case evidence dir.
6. If `--runner-command` is absent, append skipped result with `exitCode: null` and return `2`.
7. If present, substitute `{case}`, `{backend}`, `{output}`, `{manifest}` and run with `subprocess.run(shell=True, capture_output=True, text=True)`.
8. Save stdout/stderr to `logs/<case-slug>.stdout.log` and `.stderr.log`.
9. Append result JSONL.
10. Return `0` only when all executed cases exit `0`.

- [ ] **Step 2: Verify missing-runner behavior**

Run:

```bash
python3 skills/codex-fsq-case-runner/scripts/run_fsq_cases.py --cases fsq-testcases/windows/settings/open_settings_page.codex.yaml --run-id codex-test-missing-runner
```

Expected: exit code `2`, manifest created, result status `skipped`, message says runner command missing.

- [ ] **Step 3: Verify command-template smoke run**

Run:

```bash
python3 skills/codex-fsq-case-runner/scripts/run_fsq_cases.py --cases fsq-testcases/windows/settings/open_settings_page.codex.yaml --run-id codex-test-smoke-runner --runner-command "python3 -c 'import sys; print(\"case={case} backend={backend} output={output} manifest={manifest}\")'"
```

Expected: exit code `0`, result status `passed`, stdout log contains `backend=pywinauto-mcp`.

### Task 6: Final Verification And Commit

**Files:**
- Modify only generated runner skill files.

- [ ] **Step 1: Remove generated caches**

Run:

```bash
find skills/codex-fsq-case-runner -type d -name '__pycache__' -prune -exec rm -rf {} +
```

Expected: no `__pycache__` under the skill.

- [ ] **Step 2: Validate skill**

Run:

```bash
python3 /Users/qunmi/.agents/skills/skill-creator/scripts/quick_validate.py skills/codex-fsq-case-runner
```

Expected: `Skill is valid!`

- [ ] **Step 3: Validate all existing FSQ cases**

Run:

```bash
python3 skills/codex-fsq-case-converter/scripts/validate_fsq_cases.py --schema docs/codex-fsq-ai-test-dsl-v1.schema.json --cases fsq-testcases
```

Expected: `total=80 failed=0`.

- [ ] **Step 4: Run runner helper smoke checks**

Run:

```bash
python3 skills/codex-fsq-case-runner/scripts/list_fsq_cases.py --cases fsq-testcases --platform windows --area settings --limit 2
python3 skills/codex-fsq-case-runner/scripts/make_run_manifest.py --cases fsq-testcases --platform windows --area settings --limit 2 --run-id codex-test-manifest
python3 skills/codex-fsq-case-runner/scripts/run_fsq_cases.py --cases fsq-testcases/windows/settings/open_settings_page.codex.yaml --run-id codex-test-smoke-runner --runner-command "python3 -c 'print(\"ok {backend}\")'"
```

Expected: list output has two rows, manifest exists, smoke runner exits `0`.

- [ ] **Step 5: Commit**

Run:

```bash
git add skills/codex-fsq-case-runner docs/plans/2026-04-29-codex-fsq-case-runner-skill-implementation-plan.md
git commit -m "skills: add Codex FSQ case runner"
```

Expected: commit created.
