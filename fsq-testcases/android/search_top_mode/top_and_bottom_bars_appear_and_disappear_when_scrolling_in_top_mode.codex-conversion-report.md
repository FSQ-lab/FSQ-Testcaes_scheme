# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/search_top_mode.feature`
- Feature: `search_top_mode`
- Scenario: `Top and bottom bars appear and disappear when scrolling in top mode`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/search_top_mode/top_and_bottom_bars_appear_and_disappear_when_scrolling_in_top_mode.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `before_scenario: Given I open edge and go to the NTP page` | `launchApp, assertVisible` | Expanded setup. |
| `When I click on the top address bar on NTP page` | `tapOn` | Preserved source `search_box_text`; runner may fallback to `url_bar` on bottom omnibox devices. |
| `And I input "https://www.chinatravel.com" in search box and navigate to it` | `inputText, pressKey` | Compound source step split into direct actions. |
| `And I scroll up the web page for 2 second` x3 | `performActions` x3 | Preserved exact source swipe coordinates. |
| `Then The address bar disappears` | `assertNotVisible` | Preserved `control_container` hidden assertion. |
| `And I scroll down the web page for 2 second` x2 | `performActions` x2 | Preserved exact source swipe coordinates. |
| `Then the address bar is fully expanded and show "chinatravel.com"` | `assert` | Preserved source XPath text assertion. |

## BDD Execution Model

- Effective scenario steps are source scenario steps plus Behave `before_scenario` NTP setup.
- Setup expansion is recorded but optional startup helpers are kept as runner policy.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| `before_all` | runner lifecycle / environment requirements | No | Loads `.env` and starts MCP session. |
| `before_scenario` NTP setup | setup/state guarantee | Partial | Converted to `launchApp` plus NTP assertion. |
| `after_scenario` screenshot/logging | runtime evidence | No | Runner evidence policy. |

## Environment Requirements

- App is assumed installed and launchable.
- The source scenario name says top mode; current pilot runner may execute on bottom omnibox devices and rely on fallback.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `Given I open edge and go to the NTP page` | `Given I open edge`; optional alert/new-tab helpers; NTP assertion | `features/environment.py:326`; `features/steps/given_steps.py:44` |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `I click on the top address bar on NTP page` | `features/steps/core/search_top_mode.py:69` | `click_element` on `${PACKAGE}:id/search_box_text` |
| `I input "https://www.chinatravel.com" in search box and navigate to it` | `features/steps/core/search_bottom_mode.py:32` | click `url_bar`; send keys; press key `66` |
| scroll and address-bar assertions | `features/steps/core/search_bottom_mode.py:56`, `:75`, `:85`, `:65` | source coordinates and locators |

## Unresolved Or Low-Confidence Items

- Scenario assumes top omnibox mode; device state should be controlled for a strict top-mode run.

## Conversion Rules Applied

- Preserved source locators and exact gesture coordinates.
- Did not invent visual checks.

## Manual Review Checklist

- Confirm the test environment is in top mode when strict mode-specific behavior is required.
