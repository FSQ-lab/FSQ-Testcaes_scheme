# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/settings/settings.feature`
- Feature: `settings`
- Scenario: `Show or hide Downloads button on toolbar`
- Tags: `@regression, @p0, @settings`

## Output

- Output YAML: `fsq-testcases/windows/settings/show_or_hide_downloads_button_on_toolbar.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I click "Appearance"` | `tapOn` | Conservative semantic conversion. |
| `And I click the option "Page zoom" button under "Appearance"` | `tapOn` | Conservative semantic conversion. |
| `And I click "Toolbar" in the webpage` | `tapOn` | Conservative semantic conversion. |
| `And I click on "Downloads" button on the settings page to turn it on` | `tapOn` | Conservative semantic conversion. |

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
