# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/settings/settings.feature`
- Feature: `settings`
- Scenario: `Verify the Delete browsing data dialog should display`
- Tags: `@settings, @smoke, @p0`

## Output

- Output YAML: `fsq-testcases/windows/settings/verify_the_delete_browsing_data_dialog_should_display.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `And I click "Privacy, search, and services"` | `tapOn` | Conservative semantic conversion. |
| `Then I click the "Clear browsing data" button under Privacy, search, and services` | `tapOn` | Conservative semantic conversion. |
| `And I click the "Choose what to clear" button` | `tapOn` | Conservative semantic conversion. |
| `Then the "Delete browsing data" dialog should display` | `assert/assertVisible/assertWithAI` | Conservative semantic conversion. |

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
