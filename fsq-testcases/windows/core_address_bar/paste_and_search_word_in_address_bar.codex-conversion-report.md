# Conversion Report

Codex-produced conversion report.

## Source
- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `features/core_address_bar/core_address_bar.feature`
- Feature: `Core Address Bar`
- Scenario: `Paste and Search word in address bar`
- Tags: `@search @regression @p0`

## Output
- Output YAML: `fsq-testcases/windows/core_address_bar/paste_and_search_word_in_address_bar.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping
| Source step | FSQ command | Notes |
| --- | --- | --- |
| copy `cat` to clipboard | `inputText`, `Ctrl+A`, `Ctrl+C`, `Delete` | Mirrors source helper. |
| right click in address bar | `rightClickOn` | Preserves source edit target. |
| select Paste and search | `tapOn` | Preserves menu item. |
| search results assertion | `assertVisible` | Preserves `RootWebArea` document `cat - Search`. |

## BDD Execution Model
- Direct scenario; no nested `execute_steps()`.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| MCP/session startup | Runner infrastructure | No | Runner-owned. |

## Environment Requirements
- Windows Edge with clipboard and pywinauto MCP support.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `I copy "cat" to clipboard` | `enter_text`, `Ctrl+A`, `Ctrl+C`, `Delete` | Compound implementation in `core_address_bar.py`. |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| copy word to clipboard | `features/steps/core_address_bar/core_address_bar.py:421` | `enter_text`, `send_keystrokes` `^a`, `^c`, `{DELETE}`. |
| select Paste and search | `features/steps/core_address_bar/core_address_bar.py:470` | `element_click`, menu item. |
| search result assertion | `features/steps/core_address_bar/core_address_bar.py:57` | `verify_element_exists`, `RootWebArea`. |

## Unresolved Or Low-Confidence Items
- Clipboard behavior depends on runner support for modifier `pressKey` on Windows.

## Conversion Rules Applied
- Preserved operation order and source locators.
- Kept assertion blocking.

