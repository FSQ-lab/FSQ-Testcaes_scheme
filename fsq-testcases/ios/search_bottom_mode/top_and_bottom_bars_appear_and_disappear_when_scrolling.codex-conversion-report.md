# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/search_bottom_mode.feature`
- Feature: `search_bottom_mode`
- Scenario: `Top and bottom bars appear and disappear when scrolling`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/ios/search_bottom_mode/top_and_bottom_bars_appear_and_disappear_when_scrolling.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | iOS source scenarios commonly omit explicit launch step. |
| `When I click on the search box on NTP page` | `tapOn` |  |
| `And I input "https://www.chinatravel.com" in search box` | `inputText` |  |
| `And I click "Go" on keyboard` | `tapOn` |  |
| `When I scroll up the web page for 2 second` | `tapOn` | I scroll up the web page for 2 second |
| `Then The address bar is minimized and show "chinatravel.com"` | `assertVisible` |  |
| `When I scroll down the web page for 2 second` | `tapOn` | I scroll down the web page for 2 second |
| `Then the address bar is fully expanded and show "chinatravel.com"` | `assertVisible` |  |
| `When I click + button on the bottom toolbar` | `tapOn` |  |
| `Then I am landing on new tab page` | `assertVisible` |  |

## Unresolved Or Low-Confidence Items

- I scroll up the web page for 2 second
- I scroll down the web page for 2 second

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
