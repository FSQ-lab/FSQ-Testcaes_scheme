# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/settings/settings.feature`
- Feature: `settings`
- Scenario: `Cancel add custom site`
- Tags: `@regression, @p0, @settings`

## Output

- Output YAML: `fsq-testcases/macos/settings/cancel_add_custom_site.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `launchApp` |  |
| `And I input "edge://settings/startHomeNTP" to the address bar` | `tapOn, inputText` |  |
| `When I select the option "Open custom sites"` | `tapOn` |  |
| `And I click the "Add site" button` | `tapOn` | I click the "Add site" button |
| `Then the "Add site" dialog should be opened` | `assertVisible` |  |
| `When I input "https://www.bing.com" in the URL field on the "Add site" dialog` | `inputText` |  |
| `And I click the "Cancel" button on the "Add site" dialog` | `tapOn` |  |
| `Then the "Add site" dialog should be closed` | `assertNotVisible` |  |

## Unresolved Or Low-Confidence Items

- I click the "Add site" button

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
