# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/bottom_bar.feature`
- Feature: `bottom_bar`
- Scenario: `Open new InPrivate tab through overflow menu`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/bottom_bar/open_new_inprivate_tab_through_overflow_menu.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| setup | `launchApp, assertVisible` | Behave NTP setup. |
| `When I open the browser menu...` | `tapOn` | Preserved overflow button id. |
| `And I tap "New InPrivate tab" from the menu` | `tapOn` | Preserved source XPath. |
| `Then a new InPrivate tab should open` | `assertVisible` | Preserved source XPath `Browse InPrivate`. |
| `When I click "Exit InPrivate mode" on InPrivate tab` | `tapOn` | Preserved source button XPath. |
| `Then I should return to the New Tab Page` | `assertVisible` | Preserved NTP root id. |

## BDD Execution Model

- Uses bottom-bar feature scenario plus Behave setup.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| `before_scenario` NTP setup | setup/state guarantee | Partial | `launchApp` plus NTP assertion. |
| screenshots/logging | evidence | No | Runner-owned. |

## Environment Requirements

- InPrivate mode must be allowed by policy.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `Given I open edge and go to the NTP page` | app launch; optional helpers; NTP assertion | `features/environment.py:326`; `features/steps/given_steps.py:44` |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `I tap "New InPrivate tab" from the menu` | `features/steps/core/overflow_menu.py:245` | click XPath `New InPrivate Tab` |
| `a new InPrivate tab should open` | `features/steps/core/overflow_menu.py:258` | verify XPath `Browse InPrivate` |
| `I click "Exit InPrivate mode" on InPrivate tab` | `features/steps/core/overflow_menu.py:271` | click button XPath |

## Unresolved Or Low-Confidence Items

- Menu item casing varies in some app versions; source XPath uses `New InPrivate Tab`.

## Conversion Rules Applied

- Preserved source locators and blocking assertions.

## Manual Review Checklist

- Confirm InPrivate menu item text and policy availability on the target build.
