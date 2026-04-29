# Runner Adapters

## Backend Defaults

| Platform | Backend |
| --- | --- |
| windows | `pywinauto-mcp` |
| macos | `appium-mcp` |
| ios | `appium-mcp` |
| android | `appium-mcp` |

## Command Template Variables

`run_fsq_cases.py` can call a concrete runner command once per case. It substitutes:

- `{case}`: selected `.codex.yaml` path.
- `{backend}`: platform-default backend.
- `{output}`: per-case evidence directory.
- `{manifest}`: run manifest path.

Example shape:

```bash
--runner-command "<runner> --case {case} --backend {backend} --output {output} --manifest {manifest}"
```

## Windows Template

```bash
--runner-command "<runner> --case {case} --backend pywinauto-mcp --output {output} --manifest {manifest}"
```

The actual runner should use the accessibility tree first, then semantic locator reasoning and repair. It must not use screenshot coordinate guessing under a non-vision model.

## Appium MCP Template

```bash
--runner-command "<runner> --case {case} --backend appium-mcp --output {output} --manifest {manifest}"
```

The actual runner should map FSQ commands to Appium 3.x-compatible actions, including `performActions`, `releaseActions`, and driver execute methods when present in the case.

## Missing Runner Command

When no command template is provided, `run_fsq_cases.py` still validates selection and writes a run bundle. Results are `skipped` with a missing-runner message. This is intentional: it proves case selection and environment handoff without pretending execution occurred.
