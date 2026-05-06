# Conversion Report

Codex-produced conversion report.

## Source
- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `features/core_address_bar/core_address_bar.feature`
- Feature: `Core Address Bar`
- Scenario: `Search keywords by selecting search item in dropdown list of address bar`
- Tags: `@search @regression @p0`

## Output
- Output YAML: `fsq-testcases/windows/core_address_bar/search_keywords_by_selecting_search_item_in_dropdown_list_of_address_bar.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping
| Source step | FSQ command | Notes |
| --- | --- | --- |
| Background: launch Edge with empty user data directory | `launchApp` | Runtime state isolation is represented by launch/kill in this pilot DSL. |
| I input "cat" in address bar | `tapOn` + `inputText` | Preserves `enter_text` target `OmniboxViewViews` edit. |
| I click the top item "cat" in the dropdown list | `tapOn` | Preserves pywinauto `ListItem` name `cat, Bing search`. |
| tab should jump to search results page related to "cat" | `assertVisible` | Preserves `RootWebArea` document name `cat - Search`. |
| End of case | `killApp` | Required by Codex case isolation policy. |

## BDD Execution Model
- Feature scenario plus Behave steps were both used.
- No `context.execute_steps()` expansion in this scenario.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| `before_all` MCP startup | Runner infrastructure | No | Should remain runner setup. |
| screenshot/telemetry hooks | Evidence policy | No | Not case behavior. |

## Environment Requirements
- Windows Edge available through pywinauto MCP.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `I input "cat" in address bar` | none | `features/steps/common.py` uses `enter_text`. |
| `I click the top item "cat" in the dropdown list` | none | `features/steps/core_address_bar/core_address_bar.py` uses `element_click`. |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `I input "{param}" in address bar` | `features/steps/common.py:78` | `enter_text`, class `OmniboxViewViews`, control type `Edit`. |
| `I click the top item "cat" in the dropdown list` | `features/steps/core_address_bar/core_address_bar.py:257` | `element_click`, `ListItem`, `cat, Bing search`. |
| `the tab should jump...` | `features/steps/core_address_bar/core_address_bar.py:57` | `verify_element_exists`, `RootWebArea`, `cat - Search`. |

## Unresolved Or Low-Confidence Items
- Empty user data directory setup is not expressed with a dedicated Windows temp profile command in v1 YAML.

## Conversion Rules Applied
- Preserved source pywinauto locators and operation order.
- Kept assertions blocking by default.

