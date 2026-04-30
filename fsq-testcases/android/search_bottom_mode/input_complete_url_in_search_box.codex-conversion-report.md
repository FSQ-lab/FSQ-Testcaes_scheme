# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/search_bottom_mode.feature`
- Feature: `search_bottom_mode`
- Scenario: `Input complete URL in search box`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/search_bottom_mode/input_complete_url_in_search_box.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I click on the search box on NTP page` | `tapOn` |  |
| `And I input "https://www.chinatravel.com" in search box and navigate to it` | `inputText, pressKey` |  |
| `Then I should navigate to "https://www.chinatravel.com"` | `assert` | Preserved `verify_element_attribute`: `com.microsoft.emmx:id/url_bar` text contains `chinatravel.com`. |
| `When I click "Create My Trip" on page` | `tapOn` |  |
| `And I scroll the page up for 2 seconds` | `swipe` |  |
| `And I scroll the page down for 2 seconds` | `tapOn` | I scroll the page down for 2 seconds |
| `And I click the back button on bottom toolbar` | `pressKey` |  |
| `Then I should navigate to "https://www.chinatravel.com"` | `assert` | Preserved `verify_element_attribute`: `com.microsoft.emmx:id/url_bar` text contains `chinatravel.com`. |

## Unresolved Or Low-Confidence Items

- I scroll the page down for 2 seconds

## Conversion Rules Applied

- Android scenarios without explicit launch steps receive an implicit `launchApp`.
- Known literal UI labels are converted to semantic `target` actions.
- Unknown UI targets are preserved as semantic `target` descriptions.
- URL navigation assertions preserve the source Appium address-bar locator instead of using a generic browser URL assertion.
- No coordinates were generated.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm `appId: com.microsoft.emmx` matches the runner environment.
- Confirm target wording is specific enough for accessibility-tree locator resolution.
- Confirm preserved Appium address-bar resource IDs still match the current Android app build.
- Confirm every assertion should remain blocking.

## Post-run Corrections

- Preserved source `url_bar` resource id for both focus and input steps.
- Converted source scroll helpers to exact W3C pointer `performActions` using source coordinates `(540,1500)->(540,800)` and `(540,800)->(540,1500)`.
- Preserved `Create My Trip` XPath and bottom toolbar `Go back` accessibility id.
- Removed prose `tapOn` placeholders for scroll/wait-style helper steps.

