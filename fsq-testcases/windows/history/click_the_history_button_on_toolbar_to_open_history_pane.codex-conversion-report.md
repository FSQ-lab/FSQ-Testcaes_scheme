# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/history/history.feature`
- Feature: `history`
- Scenario: `Click the History button on toolbar to open History pane`
- Tags: `@p0, @history`

## Output

- Output YAML: `fsq-testcases/windows/history/click_the_history_button_on_toolbar_to_open_history_pane.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I click Settings and more button in toolbar` | `tapOn` | Conservative semantic conversion. |
| `And I right click "History" button in the menu` | `tapOn` | Conservative semantic conversion. |
| `And I click "Show in toolbar" in menu` | `tapOn` | Conservative semantic conversion. |
| `Then the History button should be displayed in the toolbar` | `assert/assertVisible/assertWithAI` | Conservative semantic conversion. |

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
