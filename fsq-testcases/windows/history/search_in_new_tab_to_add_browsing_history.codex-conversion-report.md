# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/history/history.feature`
- Feature: `history`
- Scenario: `Search in new tab to add browsing history`
- Tags: `@p0, @history`

## Output

- Output YAML: `fsq-testcases/windows/history/search_in_new_tab_to_add_browsing_history.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I input "https://www.cgtn.com" in address bar` | `tapOn, inputText, pressKey, waitUntil` | Conservative semantic conversion. |
| `And I press "Enter" key` | `pressKey` | Conservative semantic conversion. |
| `When I press "Ctrl+H" to open history hub` | `pressKey` | Conservative semantic conversion. |
| `And I search "cgtn" in history hub` | `semantic action/assertion` | Conservative semantic conversion. |

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
