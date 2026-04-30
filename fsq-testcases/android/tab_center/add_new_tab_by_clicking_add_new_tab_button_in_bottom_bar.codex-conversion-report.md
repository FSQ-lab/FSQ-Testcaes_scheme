# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/tab_center.feature`
- Feature: `tab_center`
- Scenario: `Add new tab by clicking 'add new tab' button in bottom bar`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/tab_center/add_new_tab_by_clicking_add_new_tab_button_in_bottom_bar.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I enter tab center by clicking on the tab center icon` | `tapOn` | I enter tab center by clicking on the tab center icon |
| `And I open tab center settings menu` | `tapOn` | I open tab center settings menu |
| `And I click on "Clear all tabs" button` | `tapOn` |  |
| `And  I click "Close all tabs and groups" on dialog` | `tapOn` |  |
| `When I click on "Open a new tab" button` | `tapOn` |  |
| `And I input "https://www.google.com" in search box and navigate to it` | `inputText, pressKey` |  |
| `Then I should see "1" on the tab center icon` | `assertVisible` |  |
| `When I click on new tab button to open a new tab` | `tapOn` |  |
| `Then I should return to the New Tab Page` | `tapOn` |  |
| `Then I should see "2" on the tab center icon` | `assertVisible` |  |

## Unresolved Or Low-Confidence Items

- I enter tab center by clicking on the tab center icon
- I open tab center settings menu

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

- Removed the duplicated Add New Tab action introduced by the first conversion.
- Converted `Then I should return to the New Tab Page` to an NTP search-box assertion instead of another action.
- Preserved source tab-count assertions through `android:id/text1`.

