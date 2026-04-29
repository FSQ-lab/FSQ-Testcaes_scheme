# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/settings/settings.feature`
- Feature: `settings`
- Scenario: `Search in settings search box`
- Tags: `@regression, @p0, @settings`

## Output

- Output YAML: `fsq-testcases/macos/settings/search_in_settings_search_box.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `launchApp` |  |
| `When I click "Settings and more" button on toolbar` | `tapOn` |  |
| `And I select "Settings" button from the dropdown menu` | `tapOn` |  |
| `Then the settings page should be opened` | `assert` |  |
| `When I input "Privacy" in the settings search box` | `inputText` |  |
| `Then the search results should display relevant settings related to "Privacy"` | `assertVisible` |  |
| `When I clear the search box` | `clearText` |  |
| `Then the search results should reset to show all settings` | `assertVisible` |  |
| `When I input "123" in the settings search box` | `inputText` |  |
| `Then the search results should display "No search results found"` | `assertVisible` |  |

## Unresolved Or Low-Confidence Items

- None

## Conversion Rules Applied

- Known address bar interactions use `accessibilityId: Address and search bar`.
- Unknown UI targets are preserved as semantic `target` descriptions.
- Relation locators are used only when the source step explicitly provides context.
- No coordinates were generated.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm `appId: com.microsoft.edgemac` matches the runner environment.
- Confirm target wording is specific enough for accessibility-tree locator resolution.
- Add stable locators from knowledge base when available.
- Confirm every assertion should remain blocking.
