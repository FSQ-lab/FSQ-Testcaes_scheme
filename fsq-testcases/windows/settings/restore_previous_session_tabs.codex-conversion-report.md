# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/settings/settings.feature`
- Feature: `settings`
- Scenario: `Restore previous session tabs`
- Tags: `@settings, @smoke, @p0`

## Output

- Output YAML: `fsq-testcases/windows/settings/restore_previous_session_tabs.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `And I click "Start, home, and new tab page"` | `tapOn` | Conservative semantic conversion. |
| `When I select the option "Open tabs from the previous session"` | `tapOn` | Conservative semantic conversion. |
| `When I open a new tab` | `semantic action/assertion` | Conservative semantic conversion. |
| `And I navigate to "https://www.bbc.com"` | `tapOn, inputText, pressKey, waitUntil` | Conservative semantic conversion. |
| `And I close and restart Edge` | `semantic action/assertion` | Conservative semantic conversion. |

## Unresolved Or Low-Confidence Items

- Confirm Windows accessibility names against pywinauto MCP tree during first execution.

## Conversion Rules Applied

- Windows cases use `runner.backend: pywinauto-mcp` and Edge app metadata.
- Known address bar interactions use `name: Address and search bar` with `controlType: Edit`.
- Unknown UI targets are preserved as semantic `target` descriptions for accessibility-tree locator resolution.
- Screenshot/visual validation steps are represented as blocking `assertWithAI`; no visual coordinate fallback was generated.
- No coordinates were generated.

## Manual Review Checklist

- Confirm Edge executable path matches the runner machine.
- Confirm target wording is specific enough for accessibility-tree locator resolution.
- Add stable Windows locators from knowledge base when available.
- Confirm every assertion should remain blocking.
