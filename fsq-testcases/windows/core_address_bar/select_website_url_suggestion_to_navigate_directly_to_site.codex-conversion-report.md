# Conversion Report

Codex-produced conversion report.

## Source
- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `features/core_address_bar/core_address_bar.feature`
- Feature: `Core Address Bar`
- Scenario: `Select website URL suggestion to navigate directly to site`
- Tags: `@navigation @regression @p0`

## Output
- Output YAML: `fsq-testcases/windows/core_address_bar/select_website_url_suggestion_to_navigate_directly_to_site.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping
| Source step | FSQ command | Notes |
| --- | --- | --- |
| I navigate to `https://www.bing.com/?cc=us` | `executeMethod: native_navigate` | Preserves Windows pywinauto MCP helper rather than synthetic address-bar actions. |
| I type "apple" in address bar | `inputText` | Preserves source `enter_text` into `OmniboxViewViews`. |
| I click the "apple.com" in the dropdown list | `tapOn` | Preserves `ListItem` name `apple.com`. |
| Apple navigation assertions | `assertVisible` + `assert` | Preserves tab/document and address-bar value checks. |

## BDD Execution Model
- Direct Behave step mapping, no nested expansion.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| MCP/session startup | Runner infrastructure | No | Should stay in runner. |
| screenshot/telemetry hooks | Evidence policy | No | Not converted into case commands. |

## Environment Requirements
- Windows Edge with pywinauto MCP and network access to Bing/Apple.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `I navigate to "{param}"` | none | `native_navigate` in `features/steps/common.py`. |
| `I type "apple" in address bar` | none | `enter_text` in `core_address_bar.py`. |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `I navigate to "{param}"` | `features/steps/common.py:47` | `native_navigate` with URL. |
| `I type "apple" in address bar` | `features/steps/core_address_bar/core_address_bar.py:302` | `enter_text`, `OmniboxViewViews`. |
| `I click the "apple.com"...` | `features/steps/core_address_bar/core_address_bar.py:319` | `element_click`, `ListItem`. |

## Unresolved Or Low-Confidence Items
- `executeMethod: native_navigate` assumes the Windows runner maps this script to the pywinauto MCP tool.

## Conversion Rules Applied
- Preserved Windows `native_navigate` explicitly.
- Preserved locator-backed assertions rather than bare URL assertion.

