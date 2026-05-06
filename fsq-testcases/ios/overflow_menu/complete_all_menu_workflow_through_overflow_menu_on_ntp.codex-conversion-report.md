# Conversion Report

Codex-produced conversion report.

## Source
- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `features/core/overflow_menu.feature`
- Feature: `Overflow menu entry on NTP - Complete Workflows`
- Scenario: `Complete all menu workflow through overflow menu on NTP`
- Tags: `@P0`

## Output
- Output YAML: `fsq-testcases/ios/overflow_menu/complete_all_menu_workflow_through_overflow_menu_on_ntp.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping
| Source step | FSQ command | Notes |
| --- | --- | --- |
| tap overflow menu | `tapOn` | Preserves toolbar menu accessibility id. |
| Swipe to next page | `performActions` | Preserves exact source swipe. |
| tap All menu | `tapOn` | Preserves iOS predicate locator. |
| All menu panel assertion | `assertVisible` | Preserves `All Menu` name locator. |
| close panel by swipe down | `performActions` | Preserves exact source swipe down. |

## BDD Execution Model
- Feature steps resolved against `features/steps/core/overflow_menu.py`.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| Appium session setup | Runner infrastructure | No | Runner-owned. |
| screenshot/result hooks | Evidence policy | No | Not case behavior. |

## Environment Requirements
- iOS Edge and Appium 3.x MCP runner.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `Swipe to next page of the overflow menu` | none | Exact `swipe` coordinates from step implementation. |
| `I close the All menu panel by swiping down...` | none | Exact `swipe` coordinates from step implementation. |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| overflow menu next page | `features/steps/core/overflow_menu.py:320` | `swipe`, `(350,640)` to `(50,640)`, duration `1000`. |
| All menu option | `features/steps/core/overflow_menu.py:454` | `click_element`, `AppiumBy.IOS_PREDICATE`. |
| close All menu panel | `features/steps/core/overflow_menu.py:304` | `swipe`, `(196,200)` to `(196,600)`, duration `500`. |

## Unresolved Or Low-Confidence Items
- Uses source gesture coordinates because the original implementation is coordinate-based.

## Conversion Rules Applied
- Preserved exact gesture coordinates and source locator strategy.

