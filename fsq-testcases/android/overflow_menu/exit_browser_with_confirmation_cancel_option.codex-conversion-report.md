# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/overflow_menu.feature`
- Feature: `overflow_menu`
- Scenario: `Exit browser with confirmation - Cancel option`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/overflow_menu/exit_browser_with_confirmation_cancel_option.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| setup | `launchApp, assertVisible` | Behave NTP setup. |
| `When I open the browser menu...` | `tapOn` | Preserved overflow button id. |
| `And I swipe within the scrollable area...` | `performActions` | Preserved source menu page gesture `(800,1900)->(200,1900)`. |
| `And I tap "Exit browser" from the menu` | `tapOn` | Preserved source XPath. |
| `Then the "Exit Microsoft Edge" confirmation dialog should appear` | `assertVisible` | Preserved source XPath. |
| `When I tap "Cancel" in the confirmation dialog` | `tapOn` | Preserved source XPath. |
| `Then the confirmation dialog should disappear` | `assertNotVisible` | Preserved source XPath. |
| `Then I should return to the New Tab Page` | `assertVisible` | Preserved NTP root id. |

## BDD Execution Model

- Uses overflow-menu feature steps plus Behave setup.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| `before_scenario` NTP setup | setup/state guarantee | Partial | `launchApp` plus NTP assertion. |
| screenshots/logging | evidence | No | Runner-owned. |

## Environment Requirements

- None beyond app being launchable.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `Given I open edge and go to the NTP page` | app launch; optional helpers; NTP assertion | `features/environment.py:326`; `features/steps/given_steps.py:44` |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `I tap "Exit browser" from the menu` | `features/steps/core/overflow_menu.py:446` | click XPath `Exit browser` |
| confirmation dialog steps | `features/steps/core/overflow_menu.py:459`, `:472`, `:485` | verify/click/not-exists XPaths |

## Unresolved Or Low-Confidence Items

- Menu page gesture depends on current device dimensions; coordinates are source-provided.

## Conversion Rules Applied

- Preserved source locators and exact menu paging gesture.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm the second overflow-menu page exposes `Exit browser` on the target build.
