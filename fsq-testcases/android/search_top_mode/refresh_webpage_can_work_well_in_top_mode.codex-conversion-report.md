# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/search_top_mode.feature`
- Feature: `search_top_mode`
- Scenario: `Refresh webpage can work well in top mode`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/search_top_mode/refresh_webpage_can_work_well_in_top_mode.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I click on the search box on NTP page` | `tapOn` |  |
| `And I input "https://www.chinatravel.com" in search box and navigate to it` | `inputText, pressKey` |  |
| `And I perform a long press gesture on address bar` | `tapOn` | I perform a long press gesture on address bar |
| `When I click on "Move address bar to top" option` | `tapOn` |  |
| `And I see the refresh button shown on omnibox` | `tapOn` |  |
| `When I click on the refresh button` | `tapOn` |  |
| `Then the web page is reloaded completedly` | `tapOn` | the web page is reloaded completedly |
| `And I scroll the page down for 2 seconds` | `tapOn` | I scroll the page down for 2 seconds |
| `Then the web page is reloaded completedly` | `tapOn` | the web page is reloaded completedly |

## Unresolved Or Low-Confidence Items

- I perform a long press gesture on address bar
- the web page is reloaded completedly
- I scroll the page down for 2 seconds
- the web page is reloaded completedly

## Conversion Rules Applied

- Android scenarios without explicit launch steps receive an implicit `launchApp`.
- Known literal UI labels are converted to semantic `target` actions.
- Unknown UI targets are preserved as semantic `target` descriptions.
- No coordinates were generated.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm `appId: com.microsoft.emmx` matches the runner environment.
- Confirm target wording is specific enough for accessibility-tree locator resolution.
- Add stable Android locators from knowledge base when available.
- Confirm every assertion should remain blocking.

## Post-run Corrections

- Converted long press on address bar to `longPressOn` with the source `url_bar` locator.
- Preserved source `refresh_button` locator for both assertion and tap.
- Converted page reload checks to `assertVisible` on `android.webkit.WebView` and scroll helper to W3C pointer actions.

