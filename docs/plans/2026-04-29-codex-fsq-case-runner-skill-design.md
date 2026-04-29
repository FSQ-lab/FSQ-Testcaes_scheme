# Codex FSQ Case Runner Skill Design

Codex-produced design note.

## Goal

Create a repository-local skill that helps team members run converted FSQ AI Test DSL cases directly, starting with platform-default MCP backends and preserving enough run evidence for manual failure analysis.

## Context

The repository already contains:

- FSQ DSL v1 specification and schema.
- `fsq-testcases/<platform>/.../*.codex.yaml` converted cases.
- `skills/codex-fsq-case-converter/` for converting source cases into FSQ DSL.

The next workflow is execution: team members need a repeatable way to select cases, validate them, choose the correct backend, start a run, and keep outputs organized.

## Decision

Create:

```text
skills/codex-fsq-case-runner/
  SKILL.md
  references/
    environment.md
    runner-adapters.md
    evidence-and-repair.md
  scripts/
    list_fsq_cases.py
    make_run_manifest.py
    run_fsq_cases.py
```

The skill should be committed as source files, not as a packaged `.skill` artifact.

## Backend Defaults

Use platform to choose backend automatically:

| Platform | Default backend |
| --- | --- |
| windows | `pywinauto-mcp` |
| macos | `appium-mcp` |
| ios | `appium-mcp` |
| android | `appium-mcp` |

The daily command should not require users to pass an adapter:

```bash
python3 skills/codex-fsq-case-runner/scripts/run_fsq_cases.py \
  --cases fsq-testcases/windows/settings/open_settings_page.codex.yaml
```

Batch selection should also work:

```bash
python3 skills/codex-fsq-case-runner/scripts/run_fsq_cases.py \
  --platform windows \
  --area settings \
  --limit 3
```

## Runner Command Handling

The wrapper should have a direct-run path with platform-default backend selection. Because the concrete executor CLI/MCP invocation may evolve, support a command-template override:

```bash
--runner-command "<command> --case {case} --backend {backend} --output {output} --manifest {manifest}"
```

Template variables:

- `{case}`: current `.codex.yaml` path.
- `{backend}`: platform-selected backend.
- `{output}`: per-case evidence directory.
- `{manifest}`: run manifest path.

When no concrete runner command is available, the script should fail clearly after validation and manifest creation, explaining which backend is required and where the run bundle was written. It should not pretend a case ran.

## Run Outputs

Create run bundles under:

```text
runs/codex-YYYYMMDD-HHMMSS/
  manifest.json
  results.jsonl
  logs/
  evidence/
```

Each result entry should include:

```json
{
  "case": "fsq-testcases/windows/settings/open_settings_page.codex.yaml",
  "platform": "windows",
  "backend": "pywinauto-mcp",
  "status": "passed|failed|skipped",
  "exitCode": 0,
  "durationMs": 12345,
  "outputDir": "runs/codex-.../evidence/..."
}
```

## Environment Guidance

`references/environment.md` should give practical setup checks:

- Python dependencies for local helper scripts.
- Appium 3.x MCP expectations for Android, iOS, and macOS.
- pywinauto MCP expectations for Windows.
- Edge app identity and accessibility permissions.
- Device/simulator/emulator availability.
- Credential/model/MCP environment variables as placeholders, without hardcoding secrets.

## Evidence And Repair Discipline

`references/evidence-and-repair.md` should state:

- Running should not modify case YAML automatically.
- Failures should preserve stdout, stderr, exit code, case path, backend, and evidence directory.
- Failure categories should include `element_not_found`, `wrong_state`, `page_not_ready`, `assertion_failed`, and `backend_error` when the executor can provide them.
- Non-vision models must not screenshot-guess coordinates.
- Locator failures should flow through accessibility-tree reasoning and repair rather than visual fallback.

## Scripts

### `list_fsq_cases.py`

List cases and metadata. Support:

- `--cases <path>` for root or file.
- `--platform <platform>`.
- `--area <area>`.
- `--tag <tag>` repeatable.
- `--json` for machine-readable output.

### `make_run_manifest.py`

Generate a manifest from selected cases. Include:

- `runId`.
- `createdAt`.
- selected cases.
- platform/backend mapping.
- schema path.
- output root.

### `run_fsq_cases.py`

Perform the execution wrapper workflow:

1. Resolve selected cases.
2. Validate selected cases through the converter skill validator.
3. Infer backend from platform.
4. Create run bundle and manifest.
5. If `--runner-command` is provided, run it once per case with template substitution.
6. If no runner command is available, write a skipped result that clearly says the concrete runner command is missing.
7. Save stdout/stderr logs and `results.jsonl`.
8. Return non-zero when any case fails or when no runner command is available for selected cases.

## Non-Goals

- Do not implement the full Appium or pywinauto executor inside the skill.
- Do not write repair logic that edits cases.
- Do not introduce packaged `.skill` files into the repository.
- Do not hardcode secrets, device IDs, or team-private runner endpoints.

## Acceptance Criteria

- The new skill validates with `quick_validate.py`.
- `list_fsq_cases.py` can list the existing 80 cases.
- `make_run_manifest.py` can create a manifest for a small Windows selection.
- `run_fsq_cases.py` can create a run bundle and skipped/missing-runner results without a real runner command.
- `run_fsq_cases.py` can execute a harmless command-template smoke test such as `python3 -c ...` against one case.
- The existing FSQ case validator still reports `total=80 failed=0`.
