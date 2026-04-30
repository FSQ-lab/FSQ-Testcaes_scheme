# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/search_bottom_mode.feature`
- Feature: `search_bottom_mode`
- Scenario: `Complete search process with bottom omnibox`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/search_bottom_mode/complete_search_process_with_bottom_omnibox.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I click on the address bar on NTP page` | `tapOn` |  |
| `Then I should see the topsites shown on ZIP` | `assertVisible` | Preserved Appium ID from step definition: `com.microsoft.emmx:id/suggestion_top_sites_list`. |
| `And I should see the camera search icon on omnibox` | `assertVisible` | Preserved Appium ID from step definition: `com.microsoft.emmx:id/attachment_right_camera_button`. |
| `And I should see the Copilot voice icon on omnibox` | `assertVisible` | Preserved Appium ID from step definition: `com.microsoft.emmx:id/attachment_right_mic_button`. |
| `When I input a keyword "chinatravel.com"` | `inputText` |  |
| `Then I should see the suggestion list shown next to Omnibox` | `assertVisible` | Preserved Appium ID from step definition: `com.microsoft.emmx:id/omnibox_suggestions_dropdown`. |
| `When I click "Go" on keyboard` | `tapOn` |  |
| `Then the address bar is fully expanded and show "chinatravel.com"` | `tapOn` | the address bar is fully expanded and show "chinatravel.com" |

## Unresolved Or Low-Confidence Items

- the address bar is fully expanded and show "chinatravel.com"

## Conversion Rules Applied

- Android scenarios without explicit launch steps receive an implicit `launchApp`.
- Known literal UI labels are converted to semantic `target` actions.
- Unknown UI targets are preserved as semantic `target` descriptions.
- Appium locators found in Behave step definitions are preserved as dual-layer `target` + `locator` fields.
- No coordinates were generated.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm `appId: com.microsoft.emmx` matches the runner environment.
- Confirm target wording is specific enough for accessibility-tree locator resolution.
- Confirm preserved Appium resource IDs still match the current Android app build.
- Confirm every assertion should remain blocking.

## Post-run Corrections

- Preserved source locators for top sites, camera icon, Copilot voice icon, suggestion dropdown, and address bar text assertion.
- Kept icon assertions accessibility-backed rather than screenshot-backed because the source step uses Appium ids.

