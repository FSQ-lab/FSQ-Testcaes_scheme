# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/search_bottom_mode.feature`
- Feature: `search_bottom_mode`
- Scenario: `Use auto complete to input search content`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/ios/search_bottom_mode/use_auto_complete_to_input_search_content.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | iOS source scenarios commonly omit explicit launch step. |
| `When I click on the search box on NTP page` | `tapOn` |  |
| `And I input a keyword "apple" in the search box` | `inputText` |  |
| `And I click "Go" on keyboard` | `tapOn` |  |
| `When I dismiss the permission dialog from bing` | `tapOn` |  |
| `When I click + button on the bottom toolbar` | `tapOn` |  |
| `When I click on the search box on NTP page` | `tapOn` |  |
| `And I type "a" in the search box` | `inputText` |  |
| `Then I should see "apple" shown in search box` | `assertVisible` |  |
| `And I click "Go" on keyboard` | `tapOn` |  |
| `And I should see search results for "apple"` | `assertVisible` |  |

## Unresolved Or Low-Confidence Items

- None

## Conversion Rules Applied

- iOS scenarios without explicit launch steps receive an implicit `launchApp`.
- Known literal UI labels are converted to semantic `target` actions.
- Screenshot analysis steps are converted to blocking `assertWithAI` commands.
- Unknown UI targets are preserved as semantic `target` descriptions.
- No coordinates were generated.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm `appId: com.microsoft.msedge` matches the runner environment.
- Confirm target wording is specific enough for accessibility-tree locator resolution.
- Add stable iOS locators from knowledge base when available.
- Confirm every assertion should remain blocking.
