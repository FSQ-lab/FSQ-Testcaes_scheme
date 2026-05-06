# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/search_bottom_mode.feature`
- Feature: `search_bottom_mode`
- Scenario: `Refresh webpage can work well in bottom mode`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/search_bottom_mode/refresh_webpage_can_work_well_in_bottom_mode.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| setup | `launchApp, assertVisible` | Behave NTP setup. |
| `When I click on the search box on NTP page` | `tapOn` | NTP search entry. |
| `And I input "https://www.chinatravel.com" in search box and navigate to it` | `inputText, pressKey` | Preserved source compound action. |
| `Then I should navigate to "https://www.chinatravel.com"` | `assert` | Preserved address-bar text contains. |
| `And I see the refresh button shown on omnibox` | `assertVisible` | Preserved `refresh_button`. |
| `When I click on the refresh button` | `tapOn` | Preserved `refresh_button`. |
| `Then the web page is reloaded completedly` | `assertVisible` | Converted to WebView visible state. |
| `And I scroll the page down for 2 seconds` | `performActions` | Preserved source swipe. |
| `Then the web page is reloaded completedly` | `assertVisible` | WebView visible state. |

## BDD Execution Model

- Scenario uses shared search-bottom-mode steps plus Behave setup.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| `before_scenario` NTP setup | setup/state guarantee | Partial | `launchApp` plus NTP assertion. |
| runtime screenshot/logging | evidence | No | Runner-owned. |

## Environment Requirements

- Network access to `chinatravel.com`.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `Given I open edge and go to the NTP page` | app launch; optional helpers; NTP assertion | `features/environment.py:326`; `features/steps/given_steps.py:44` |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `I see the refresh button shown on omnibox` | `features/steps/core/search_bottom_mode.py:846` | `verify_element_exists` on `refresh_button` |
| `I click on the refresh button` | `features/steps/core/search_bottom_mode.py:859` | click `refresh_button` |
| `the web page is reloaded completedly` | `features/steps/core/search_bottom_mode.py:872` | page load verification; converted to WebView visible state |

## Unresolved Or Low-Confidence Items

- Source reload completion assertion is broad; YAML uses WebView visibility as the simple pilot signal.

## Conversion Rules Applied

- Preserved source locators where available.
- Kept reload assertions blocking.

## Manual Review Checklist

- Confirm WebView visibility is enough for this pilot; a future runner may add page-state/readiness checks.
