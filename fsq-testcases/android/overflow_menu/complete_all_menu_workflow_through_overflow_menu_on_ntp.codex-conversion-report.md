# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/overflow_menu.feature`
- Feature: `overflow_menu`
- Scenario: `Complete all menu workflow through overflow menu on NTP`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/overflow_menu/complete_all_menu_workflow_through_overflow_menu_on_ntp.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I open the browser menu by tapping on the three dots icon at the bottom right corner` | `tapOn` | Preserved Appium ID: `com.microsoft.emmx:id/overflow_button_bottom`. |
| `And I swipe within the scrollable area on menu from right to left to go to the second page` | `swipe` | Preserved action semantics as a left swipe. |
| `And I tap "All Menu" from the menu` | `tapOn` | Preserved source XPath: `//android.widget.TextView[@text='All menu']`. |
| `Then the All Menu panel should open` | `assertVisible` | Preserved source XPath: `//android.widget.TextView[@text='All Menu']`. |
| `When I click "Edit" on All menu panel` | `tapOn` | Preserved Appium ID: `com.microsoft.emmx:id/toolbar_button_edit_done`. |
| `Then The All menu edit mode should be opened` | `assertVisible` | Preserved source XPath: `//android.widget.TextView[@text='Edit Menu']`. |
| `And The "Favorites" is disabled` | `assert` | Preserved source XPath and enabled=false assertion. |
| `When I click "Drop" icon` | `tapOn` | Preserved source XPath: `//android.widget.TextView[@text='Drop']/..`. |
| `And I click "Done" on All menu panel` | `tapOn` | Preserved source XPath: `//android.widget.Button[@text='Done']`. |
| `And I click back button on All menu panel` | `tapOn` | Preserved Appium ID: `com.microsoft.emmx:id/back_button`. |
| `And I open the browser menu by tapping on the three dots icon at the bottom right corner` | `tapOn` | Preserved Appium ID: `com.microsoft.emmx:id/overflow_button_bottom`. |
| `And I swipe within the scrollable area on menu from right to left to go to the second page` | `swipe` | Preserved action semantics as a left swipe. |
| `Then I should not see "Drop" on menu` | `assertNotVisible` | Preserved source XPath: `//android.widget.TextView[@text='Drop']`. |
| `When I tap "All Menu" from the menu` | `tapOn` | Preserved source XPath: `//android.widget.TextView[@text='All menu']`. |
| `And I click "Edit" on All menu panel` | `tapOn` | Preserved Appium ID: `com.microsoft.emmx:id/toolbar_button_edit_done`. |
| `And I scroll the page up slightly` | `swipe` | Preserved action semantics as an upward swipe. |
| `And I click "Drop" icon` | `tapOn` | Preserved source XPath: `//android.widget.TextView[@text='Drop']/..`. |
| `And I click "Done" on All menu panel` | `tapOn` | Preserved source XPath: `//android.widget.Button[@text='Done']`. |
| `And I click back button on All menu panel` | `tapOn` | Preserved Appium ID: `com.microsoft.emmx:id/back_button`. |
| `And I open the browser menu by tapping on the three dots icon at the bottom right corner` | `tapOn` | Preserved Appium ID: `com.microsoft.emmx:id/overflow_button_bottom`. |
| `And I swipe within the scrollable area on menu from right to left to go to the second page` | `swipe` | Preserved action semantics as a left swipe. |
| `Then I should see "Drop" on menu` | `assertVisible` | Preserved source XPath: `//android.widget.TextView[@text='Drop']`. |

## Unresolved Or Low-Confidence Items

- None for locator preservation. Runner still needs device validation for exact gesture distance and current app build locators.

## Conversion Rules Applied

- Android scenarios without explicit launch steps receive an implicit `launchApp`.
- Known literal UI labels are converted to semantic `target` actions.
- Appium locators found in Behave step definitions are preserved as dual-layer `target` + `locator` or locator-backed assertions.
- Swipe steps are kept as direct action commands instead of prose `tapOn` steps.
- No coordinates were generated.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm `appId: com.microsoft.emmx` matches the runner environment.
- Confirm target wording is specific enough for accessibility-tree locator resolution.
- Confirm preserved Appium locators still match the current Android app build.
- Confirm the left swipe reaches the second overflow-menu page on the test device size.
- Confirm every assertion should remain blocking.

## Post-run Corrections

- Preserved source horizontal menu swipe as W3C pointer actions with exact coordinates `(800,1900)->(200,1900)` and `duration=1000`.
- Avoided generic `swipe: left` because menu paging depends on the original gesture target and path.

