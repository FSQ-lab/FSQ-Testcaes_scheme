# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/search_bottom_mode.feature`
- Feature: `search_bottom_mode`
- Scenario: `Search history keyword can be accessiable on zip page`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/search_bottom_mode/search_history_keyword_can_be_accessiable_on_zip_page.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `before_scenario: Given I open edge and go to the NTP page` | `launchApp, assertVisible` | Expanded setup. |
| `When I click on the search box on NTP page` | `tapOn` | NTP search entry. |
| `And I input a keyword "microsoft" in the search box and click "Go" on keyboard` | `inputText, pressKey` | Source sends keys to `url_bar` and presses key `66`. |
| `And I Open a new tab` | `tapOn` | Preserved source `edge_bottom_bar_plus_button`. |
| `And I click on the search box on NTP page` | `tapOn` | NTP search entry. |
| `Then I should see the new search history keyword "microsoft" in list` | `assertVisible` | Preserved source XPath over `line_1`. |

## BDD Execution Model

- Effective scenario includes Behave setup plus the feature scenario steps.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| `before_all` | runner lifecycle / environment requirements | No | Runtime setup only. |
| `before_scenario` NTP setup | setup/state guarantee | Partial | `launchApp` and NTP assertion. |
| `after_scenario` evidence | runtime evidence | No | Runner handles evidence. |

## Environment Requirements

- Search history must not be disabled by policy/private mode.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `Given I open edge and go to the NTP page` | app launch; optional startup helpers; NTP assertion | `features/environment.py:326`; `features/steps/given_steps.py:44` |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `I click on the search box on NTP page` | `features/steps/core/search_bottom_mode.py:9` | click `${PACKAGE}:id/url_bar` |
| `I input a keyword "microsoft"...` | `features/steps/core/search_bottom_mode.py:95` | send keys `microsoft`; press key `66` |
| `I Open a new tab` | `features/steps/core/search_bottom_mode.py:117` | click `edge_bottom_bar_plus_button` |
| history keyword assertion | `features/steps/core/search_bottom_mode.py:125` | XPath for `line_1` text `microsoft` |

## Unresolved Or Low-Confidence Items

- Search history may depend on app privacy settings or prior data state.

## Conversion Rules Applied

- Preserved source locators and operation order.
- Kept assertion blocking.

## Manual Review Checklist

- Confirm history suggestions appear on ZIP/NTP for the current profile.
