# Conversion Report

Codex-produced conversion report.

## Source
- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `features/core/overflow_menu.feature`
- Feature: `Overflow menu entry on NTP - Complete Workflows`
- Scenario: `Complete dark mode workflow through overflow menu on NTP`
- Tags: `@P0`

## Output
- Output YAML: `fsq-testcases/ios/overflow_menu/complete_dark_mode_workflow_through_overflow_menu_on_ntp.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping
| Source step | FSQ command | Notes |
| --- | --- | --- |
| Swipe to next page of overflow menu | `performActions` | Preserves exact source swipe coordinates. |
| tap Dark mode option | `tapOn` | Preserves XPath cell locator. |
| verify options visible | `assertVisible` x3 | Preserves `Light`, `Dark`, `System default`. |
| close panel | `tapOn` point | Source used `tap_coordinates` at `(196, 400)`. |

## BDD Execution Model
- Direct scenario resolved to Behave steps.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| Appium setup/evidence hooks | Runner/evidence policy | No | Not case behavior. |

## Environment Requirements
- iOS Edge and Appium 3.x MCP runner.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `Swipe to next page of the overflow menu` | none | `swipe` with source coordinates. |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| overflow menu next page | `features/steps/core/overflow_menu.py:320` | `swipe`, `(350,640)` to `(50,640)`, duration `1000`. |
| Dark mode option | `features/steps/core/overflow_menu.py:206` | `click_element`, XPath. |
| close Dark mode panel | `features/steps/core/overflow_menu.py:281` | `tap_coordinates`, `(196,400)`. |

## Unresolved Or Low-Confidence Items
- Close action intentionally preserves source coordinate because no semantic locator exists.

## Conversion Rules Applied
- Exact gesture coordinates were preserved; no coordinate guessing.

