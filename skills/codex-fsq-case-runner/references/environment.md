# Environment Checks

## Common

- Run commands from the repository root.
- Ensure Python can import `yaml` and `jsonschema`.
- Validate cases before execution:

```bash
python3 skills/codex-fsq-case-converter/scripts/validate_fsq_cases.py \
  --schema docs/codex-fsq-ai-test-dsl-v1.schema.json \
  --cases fsq-testcases
```

- Keep credentials, device IDs, account names, and model keys outside committed files.
- Confirm the selected runner can read the two-document FSQ YAML shape.

## Windows

Default backend: `pywinauto-mcp`.

Check:

- Edge is installed at the configured path or discoverable by app name.
- pywinauto MCP server is installed and reachable by the runner.
- Windows accessibility tree can expose Edge controls.
- The runner can activate Edge and query elements by `name`, `automationId`, and `controlType`.

Useful case config pattern:

```yaml
platform: windows
app:
  name: edge
  exe: C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
  windowTitleRegex: .*Microsoft Edge.*
runner:
  backend: pywinauto-mcp
```

## Android, iOS, And macOS

Default backend: `appium-mcp`.

Check:

- Appium 3.x server and required drivers are installed.
- The Appium MCP bridge is reachable by the runner.
- Device, simulator, or emulator is booted and visible to Appium.
- The app id or bundle id in the case config matches the installed Edge build.
- Platform accessibility permissions are enabled where required.

## Failure Before Execution

If environment checks fail, create a run bundle and mark cases `skipped` or `failed` with a clear backend or environment reason. Do not edit case YAML to work around environment setup.
