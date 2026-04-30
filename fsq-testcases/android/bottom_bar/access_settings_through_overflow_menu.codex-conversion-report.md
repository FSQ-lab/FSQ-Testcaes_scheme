# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/bottom_bar.feature`
- Feature: `bottom_bar`
- Scenario: `Access settings through overflow menu`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/bottom_bar/access_settings_through_overflow_menu.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I open the browser menu by tapping on the three dots icon at the bottom right corner` | `tapOn` |  |
| `And I tap "Settings" from the menu` | `tapOn` |  |
| `Then the Settings panel should open` | `tapOn` | the Settings panel should open |
| `And the panel title should display "Settings"` | `tapOn` | the panel title should display "Settings" |
| `When I click back button on setting page` | `pressKey` |  |
| `Then I should return to the New Tab Page` | `tapOn` |  |
| `When I open the browser menu by tapping on the three dots icon at the bottom right corner` | `tapOn` |  |
| `And I tap "Settings" from the menu` | `tapOn` |  |
| `Then the panel title should display "Settings"` | `tapOn` | the panel title should display "Settings" |
| `When I click the return button on phone navigation bar` | `pressKey` |  |
| `Then I should return to the New Tab Page` | `tapOn` |  |

## Unresolved Or Low-Confidence Items

- the Settings panel should open
- the panel title should display "Settings"
- the panel title should display "Settings"

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

## Codex Whole-pass Reconciliation

- Replaced assertion-like `tapOn` placeholders with locator-backed assertions.
- Preserved source locators for browser menu, Settings menu item, Settings title, and NTP return assertion.
- Kept setting-page close as Android Back/return according to the source steps.

