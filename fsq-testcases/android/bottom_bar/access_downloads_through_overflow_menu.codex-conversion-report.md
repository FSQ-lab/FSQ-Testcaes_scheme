# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/bottom_bar.feature`
- Feature: `bottom_bar`
- Scenario: `Access downloads through overflow menu`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/bottom_bar/access_downloads_through_overflow_menu.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I open the browser menu by tapping on the three dots icon at the bottom right corner` | `tapOn` |  |
| `And I tap "Downloads" from the menu` | `tapOn` |  |
| `Then the Downloads panel should open` | `tapOn` | the Downloads panel should open |
| `And the panel title should display "Downloads"` | `tapOn` | the panel title should display "Downloads" |
| `When I close the Downloads panel` | `pressKey` |  |
| `Then I should return to the New Tab Page` | `tapOn` |  |
| `When I open the browser menu by tapping on the three dots icon at the bottom right corner` | `tapOn` |  |
| `And I tap "Downloads" from the menu` | `tapOn` |  |
| `Then the panel title should display "Downloads"` | `tapOn` | the panel title should display "Downloads" |
| `When I click the return button on phone navigation bar` | `pressKey` |  |
| `Then I should return to the New Tab Page` | `tapOn` |  |

## Unresolved Or Low-Confidence Items

- the Downloads panel should open
- the panel title should display "Downloads"
- the panel title should display "Downloads"

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
- Preserved source locators for browser menu, Downloads menu item, hub view pager, Downloads title, close button, and NTP return assertion.
- Kept the second close path as Android Back because the source step uses key code 4.

