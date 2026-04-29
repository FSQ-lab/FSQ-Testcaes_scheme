# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/ominibox/ominibox.feature`
- Feature: `ominibox`
- Scenario: `Type a website URL and enter to navigate directly to site`
- Tags: `@p0, @ominibox`

## Output

- Output YAML: `fsq-testcases/macos/ominibox/type_a_website_url_and_enter_to_navigate_directly_to_site.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `launchApp` |  |
| `When I input "www.163.com" in address bar` | `tapOn, inputText` |  |
| `And I press the "Enter" key` | `pressKey` |  |
| `Then "163" website should be opened` | `assertVisible` |  |
| `And the address bar should display the complete URL "https://www.163.com"` | `assert` |  |

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
