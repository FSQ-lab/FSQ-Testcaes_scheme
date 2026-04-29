# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/search_top_mode.feature`
- Feature: `search_top_mode`
- Scenario: `Refresh webpage can work well in top mode`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/ios/search_top_mode/refresh_webpage_can_work_well_in_top_mode.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | iOS source scenarios commonly omit explicit launch step. |
| `When I click on the search box on NTP page` | `tapOn` |  |
| `When I input a keyword "microsoft" in the search box` | `inputText` |  |
| `When I dismiss the permission dialog from bing` | `tapOn` |  |
| `And I click "Go" on keyboard` | `tapOn` |  |
| `When I perform a long press gesture on address bar` | `tapOn` | I perform a long press gesture on address bar |
| `Then I click on "Move address bar to top" option` | `tapOn` |  |
| `And I see the refresh button shown on omnibox` | `tapOn` |  |
| `When I click on the refresh button` | `tapOn` |  |
| `Then analyze the screenshot to verify the web page does not have large blank spaces, and the content loads well` | `assertWithAI` |  |
| `And I scroll the page down for 2 seconds` | `swipe` |  |
| `Then analyze the screenshot to verify the web page does not have large blank spaces, and the content loads well` | `assertWithAI` |  |

## Unresolved Or Low-Confidence Items

- I perform a long press gesture on address bar

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
