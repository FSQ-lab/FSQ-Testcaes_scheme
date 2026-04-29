# Evidence And Repair

## Run Bundle

Use this generated layout:

```text
runs/codex-YYYYMMDD-HHMMSS/
  manifest.json
  results.jsonl
  logs/
  evidence/
```

Each case gets a stable evidence directory under `evidence/` and stdout/stderr logs under `logs/`.

## Result Status

Use:

- `passed`: runner command exited `0`.
- `failed`: runner command ran and exited non-zero.
- `skipped`: runner command was missing or selection could not be executed.

Each result should include case path, platform, backend, status, exit code, duration, output directory, and message when useful.

## Failure Categories

When the downstream executor can provide a category, prefer:

- `element_not_found`
- `wrong_state`
- `page_not_ready`
- `assertion_failed`
- `backend_error`
- `environment_error`

## Repair Discipline

- Do not modify `.codex.yaml` files automatically during a run.
- Preserve stdout, stderr, exit code, manifest, and evidence path for manual analysis.
- Use accessibility-tree reasoning for semantic target failures.
- Do not fallback to screenshot coordinate guessing under a non-vision model.
- Treat `assertWithAI` as a blocking assertion unless the case explicitly marks it optional.
