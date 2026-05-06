# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/search_bottom_mode.feature`
- Feature: `search_bottom_mode`
- Scenario: `Top and bottom bars appear and disappear when scrolling`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/search_bottom_mode/top_and_bottom_bars_appear_and_disappear_when_scrolling.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `before_scenario: Given I open edge and go to the NTP page` | `launchApp, assertVisible` | Expanded setup; optional startup helpers remain runner policy. |
| `When I click on the address bar on NTP page` | `tapOn` | Source uses `url_bar`; DSL uses NTP search entry intent with runner fallback for bottom omnibox. |
| `And I input "https://www.chinatravel.com" in search box and navigate to it` | `inputText, pressKey` | Preserved source `url_bar` input and Enter key. |
| `When I scroll up the web page for 2 second` | `performActions` | Preserved source swipe `(540,1500)->(540,800)`, duration `2000`. |
| `Then The address bar disappears` | `assertNotVisible` | Preserved source `control_container` not-exists assertion. |
| `And I scroll down the web page for 2 second` | `performActions` | Preserved source swipe `(540,800)->(540,1500)`, duration `2000`. |
| `Then the address bar is fully expanded and show "chinatravel.com"` | `assert` | Preserved source XPath over address-bar text. |

## BDD Execution Model

- Effective scenario steps are source scenario steps plus Behave `before_scenario` NTP setup.
- `Given I open edge and go to the NTP page` expands through `features/steps/given_steps.py` into app launch, optional alert dismissal, optional new-tab click, and NTP assertion.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| `before_all` | runner lifecycle / environment requirements | No | Loads `.env`, starts MCP session, and reads `PACKAGE`/account env. |
| `before_scenario` NTP setup | setup/state guarantee | Partial | Converted to `launchApp` plus NTP assertion. |
| `after_scenario` screenshot/logging | runtime evidence | No | Runner evidence policy. |

## Environment Requirements

- `PACKAGE`: Android app id/resource prefix; YAML uses `com.microsoft.emmx`.
- App is assumed installed and launchable.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `Given I open edge and go to the NTP page` | `Given I open edge`; `And I dismiss the alert dialog`; `And I click new tab button to open a new tab`; `Then I can see the new tab page` | `features/environment.py:326`; `features/steps/given_steps.py:44` |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `I click on the address bar on NTP page` | `features/steps/core/search_bottom_mode.py:48` | `click_element` on `${PACKAGE}:id/url_bar` |
| `I input "https://www.chinatravel.com" in search box and navigate to it` | `features/steps/core/search_bottom_mode.py:32` | click `url_bar`; send keys; press key `66` |
| `I scroll up the web page for 2 second` | `features/steps/core/search_bottom_mode.py:56` | swipe coordinates |
| `The address bar disappears` | `features/steps/core/search_bottom_mode.py:85` | `verify_element_not_exists` on `control_container` |
| `I scroll down the web page for 2 second` | `features/steps/core/search_bottom_mode.py:75` | swipe coordinates |
| `the address bar is fully expanded and show "chinatravel.com"` | `features/steps/core/search_bottom_mode.py:65` | XPath text assertion |

## Unresolved Or Low-Confidence Items

- Source checks disappearance of `control_container`; current app builds may expose bottom omnibox differently after scroll.

## Conversion Rules Applied

- Preserved source locators and exact gesture coordinates.
- Kept NTP entry target semantic enough for runner address-bar-mode repair.
- No screenshot-based coordinate inference was used.

## Manual Review Checklist

- Confirm scroll distance hides and restores the omnibox on the target device.
- Confirm `control_container` remains the correct hidden-toolbar signal.
