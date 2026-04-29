# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/search_bottom_mode.feature`
- Feature: `search_bottom_mode`
- Scenario: `Input complete keyword in search box`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/ios/search_bottom_mode/input_complete_keyword_in_search_box.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | iOS source scenarios commonly omit explicit launch step. |
| `When I click + button on the bottom toolbar` | `tapOn` |  |
| `When I click on the search box on NTP page` | `tapOn` |  |
| `And I input a keyword "machine learning tutorials" in the search box` | `inputText` |  |
| `And I click "Go" on keyboard` | `tapOn` |  |
| `When I dismiss the permission dialog from bing` | `tapOn` |  |
| `Then Analyze the screenshot to verify search result is machine learning related` | `assertWithAI` |  |
| `And I scroll the page up for 2 seconds` | `swipe` |  |
| `And I scroll the page down for 2 seconds` | `swipe` |  |
| `Then I should navigate to bing.com with "machine learning tutorials" in search box` | `assert` |  |

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
