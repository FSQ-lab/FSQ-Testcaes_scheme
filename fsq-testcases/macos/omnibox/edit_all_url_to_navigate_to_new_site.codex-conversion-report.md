# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/ominibox/ominibox.feature`
- Feature: `ominibox`
- Scenario: `Edit all URL to navigate to new site`
- Tags: `@p0, @ominibox`

## Output

- Output YAML: `fsq-testcases/macos/ominibox/edit_all_url_to_navigate_to_new_site.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `launchApp` |  |
| `When I type "https://www.google.com" in the address bar` | `tapOn, inputText` |  |
| `And the address bar should display the complete URL "https://www.google.com"` | `assert` |  |
| `When I select all text in the address bar` | `tapOn` | I select all text in the address bar |
| `And I type "https://www.apple.com" in the address bar` | `tapOn, inputText` |  |
| `And I press the "Enter" key` | `pressKey` |  |
| `Then I should navigate to "https://www.apple.com" successfully` | `tapOn, inputText, pressKey` |  |
| `And the address bar should display the complete URL "https://www.apple.com"` | `assert` |  |

## Unresolved Or Low-Confidence Items

- I select all text in the address bar

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
