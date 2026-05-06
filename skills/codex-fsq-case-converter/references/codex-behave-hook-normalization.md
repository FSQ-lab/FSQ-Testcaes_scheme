# Codex Behave Hook Normalization

Use this reference when a Behave repo contains `features/environment.py`, fixtures, scenario hooks, or environment variables that affect test execution.

## Hook Classification

Classify hook code before YAML generation.

| Hook behavior | Classification | YAML conversion |
| --- | --- | --- |
| Open app/browser, navigate to NTP, restore app state | setup/state guarantee | Convert to setup commands when safe |
| Login, account setup, permissions, tab count, top/bottom omnibox mode | setup/state guarantee | Convert when needed by scenario and safely expressible |
| State cleanup that affects the next case | teardown/state restore | Convert to teardown when safe |
| Start MCP/Appium session, create telemetry client, close worker/session | runner lifecycle | Do not convert to case commands |
| Screenshot, video, log collection, Application Insights, metrics | runtime evidence | Do not convert to case commands for now |
| Retry monkey patches, report naming, archival | runner policy | Do not convert to case commands |
| Version, skip, unsupported-device checks | environment constraints | Record as report metadata or unresolved |

## Setup And Teardown Conversion

Convert setup only when it materially affects execution and has a safe DSL or runner equivalent.

Examples that can become setup:

- `launchApp` / `killApp` / relaunch.
- Navigate to NTP when every scenario assumes NTP.
- Optional alert dismissal.
- Required permission prompt handling.
- Prepare address bar top/bottom mode for a scenario.
- Prepare signed-in state when the scenario is explicitly account-related.

Examples that should be unresolved unless the runner has a known command:

- Clear downloads/cache.
- Uninstall/reinstall app.
- Clear app data.
- Device language/system setting changes.
- External lab data or account state outside the app.

Never invent UI commands like `tapOn: clean cache` from hook prose.

## Runtime Evidence Exclusion

Do not put these in YAML commands:

- `after_scenario` screenshot capture.
- `after_step` telemetry or metric recording.
- Log file copying or naming.
- Appium/MCP session shutdown.

Mention them in the conversion report only when useful for runner expectations.

## Android `environment.py` Pattern

Common Android Behave behavior:

- `before_all` loads `.env`, starts MCP/session, sets telemetry, and reads credentials/package. Treat this as runner/environment requirements.
- `before_scenario` may skip by tags or version. Record skip/version constraints in the report.
- `before_scenario` may execute `context.execute_steps("Given I open edge and go to the NTP page")`. Expand it through the BDD Execution Model and convert it into setup commands.
- `after_scenario` screenshot capture is runtime evidence. Do not convert it.
- `after_step` telemetry is runtime evidence. Do not convert it.
- `after_all` session close is runner lifecycle. Do not convert it.

## Environment Variables

Handle secrets and platform identity as requirements, not literal values.

### `TEST_ACCOUNT_EMAIL`

- Required only for login, account, sync, profile, rewards, or MSA scenarios.
- If login setup is not skipped, assume the provided account can log in successfully.
- Do not write a real email address into YAML.
- Use `${TEST_ACCOUNT_EMAIL}` only when the DSL and runner support env placeholders safely.

### `TEST_ACCOUNT_PASSWORD`

- Required only for login, account, sync, profile, rewards, or MSA scenarios.
- If login setup is not skipped, assume login succeeds with the provided password.
- Never write plaintext passwords into YAML.
- Use `${TEST_ACCOUNT_PASSWORD}` only when the DSL and runner support env placeholders safely.

### `PACKAGE`

- Use as Android `appId` and resource-id prefix when appropriate.
- If install/uninstall setup is skipped or absent, assume the app is already installed and launchable.
- Prefer `appId: ${PACKAGE}` when runner support is expected.
- If source code installs, uninstalls, or clears app state and the DSL has no safe equivalent, mark it unresolved or as a runner requirement.

## Report Sections

Add these sections for hook-aware conversions:

```markdown
## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |

## Environment Requirements
```
