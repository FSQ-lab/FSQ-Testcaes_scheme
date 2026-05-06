# Conversion Report

Codex-produced conversion report.

## Source
- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `features/core_address_bar/core_address_bar.feature`
- Feature: `Core Address Bar`
- Scenario: `Paste and Go to website in address bar`
- Tags: `@navigation @regression @p0`

## Output
- Output YAML: `fsq-testcases/windows/core_address_bar/paste_and_go_to_website_in_address_bar.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping
| Source step | FSQ command | Notes |
| --- | --- | --- |
| copy `https://www.apple.com` to clipboard | `inputText`, `Ctrl+A`, `Ctrl+C`, `Delete` | Mirrors source helper behavior. |
| right click in address bar | `rightClickOn` | Preserves `OmniboxViewViews` edit target. |
| select Paste and go | `tapOn` | Preserves menu item name. |
| navigation assertions | `assertVisible` + `assert` | Preserves tab, document, and address-bar checks. |

## BDD Execution Model
- Direct scenario; helper step contains multiple extracted keyboard operations.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| MCP/session startup | Runner infrastructure | No | Runner-owned. |

## Environment Requirements
- Windows Edge with clipboard and pywinauto MCP support.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `I copy "https://www.apple.com" to clipboard` | `enter_text`, `Ctrl+A`, `Ctrl+C`, `Delete` | Compound implementation in `core_address_bar.py`. |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| copy URL to clipboard | `features/steps/core_address_bar/core_address_bar.py:338` | `enter_text`, `send_keystrokes` `^a`, `^c`, `{DELETE}`. |
| right click in address bar | `features/steps/common.py:95` | `right_click`, `OmniboxViewViews`. |
| select Paste and go | `features/steps/core_address_bar/core_address_bar.py:404` | `element_click`, menu item. |

## Unresolved Or Low-Confidence Items
- Clipboard behavior depends on runner support for modifier `pressKey` on Windows.

## Conversion Rules Applied
- Preserved compound helper operation order.
- Did not collapse clipboard setup into prose.

