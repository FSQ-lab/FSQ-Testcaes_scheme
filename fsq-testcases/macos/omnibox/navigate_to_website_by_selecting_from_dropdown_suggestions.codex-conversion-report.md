# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/ominibox/ominibox.feature`
- Feature: `ominibox`
- Scenario: `Navigate to website by selecting from dropdown suggestions`
- Tags: `@p0, @ominibox`

## Output

- Output YAML: `fsq-testcases/macos/ominibox/navigate_to_website_by_selecting_from_dropdown_suggestions.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `launchApp` |  |
| `And I open a new tab` | `tapOn` |  |
| `When I type "www.apple.com" in the address bar` | `tapOn, inputText` |  |
| `Then a dropdown list should appear with URL suggestions` | `tapOn` | a dropdown list should appear with URL suggestions |
| `When I click the top item "www.apple.com" in the dropdown list` | `tapOn` | I click the top item "www.apple.com" in the dropdown list |
| `Then I should navigate to "https://www.apple.com" successfully` | `tapOn, inputText, pressKey` |  |
| `And the address bar should display the complete URL "https://www.apple.com"` | `assert` |  |

## Unresolved Or Low-Confidence Items

- a dropdown list should appear with URL suggestions
- I click the top item "www.apple.com" in the dropdown list

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
