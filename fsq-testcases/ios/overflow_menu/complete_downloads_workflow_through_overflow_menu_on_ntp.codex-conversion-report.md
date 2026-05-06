# Conversion Report

Codex-produced conversion report.

## Source
- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `features/core/overflow_menu.feature`
- Feature: `Overflow menu entry on NTP - Complete Workflows`
- Scenario: `Complete downloads workflow through overflow menu on NTP`
- Tags: `@wip @P0`

## Output
- Output YAML: `fsq-testcases/ios/overflow_menu/complete_downloads_workflow_through_overflow_menu_on_ntp.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping
| Source step | FSQ command | Notes |
| --- | --- | --- |
| tap overflow menu | `tapOn` | Preserves toolbar menu accessibility id. |
| tap Downloads option | `tapOn` | Preserves source XPath. |
| Downloads panel/title assertions | `assertVisible` | Preserves `Download Manager` and title XPath. |
| close panel and return NTP | `tapOn` + `assertVisible` | Preserves Done button and NTP collection locator. |

## BDD Execution Model
- Direct feature steps resolved to Behave implementation.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| Appium session setup | Runner infrastructure | No | Runner-owned. |

## Environment Requirements
- iOS Edge and Appium 3.x MCP runner.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `I tap the "Downloads" option` | none | `click_element` with XPath. |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| Downloads option | `features/steps/core/overflow_menu.py:62` | `click_element`, XPath. |
| Downloads panel | `features/steps/core/overflow_menu.py:76` | `verify_element_exists`, AppiumBy.NAME. |
| close Downloads panel | `features/steps/core/overflow_menu.py:99` | `click_element`, XPath. |

## Unresolved Or Low-Confidence Items
- Source scenario is tagged `@wip`; converted as draft.

## Conversion Rules Applied
- Preserved source locator strategy and operation order.

