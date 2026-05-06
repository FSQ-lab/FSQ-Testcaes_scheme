# Conversion Report

Codex-produced conversion report.

## Source
- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `features/core/overflow_menu.feature`
- Feature: `Overflow menu entry on NTP - Complete Workflows`
- Scenario: `Complete favorites workflow through overflow menu on NTP`
- Tags: `@wip @P0`

## Output
- Output YAML: `fsq-testcases/ios/overflow_menu/complete_favorites_workflow_through_overflow_menu_on_ntp.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping
| Source step | FSQ command | Notes |
| --- | --- | --- |
| tap overflow menu | `tapOn` | Preserves accessibility id `kLegacyToolbarToolsMenuButtonIdentifier`. |
| tap Favorites option | `tapOn` | Preserves XPath supporting `Favourites` or `Favorites`. |
| Favorites panel/title assertions | `assertVisible` + `assert` | Preserves XPath navigation bar checks. |
| close panel and return NTP | `tapOn` + `assertVisible` | Preserves Done button and NTP collection locator. |

## BDD Execution Model
- Scenario converted from feature plus Behave step implementations.
- No nested `context.execute_steps()` for scenario body.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| Appium/MCP setup | Runner infrastructure | No | Runner-owned. |
| Screenshots/results | Evidence policy | No | Not case behavior. |

## Environment Requirements
- iOS Edge and Appium 3.x MCP runner.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `I tap the "Favorites" option` | none | `features/steps/core/overflow_menu.py` uses XPath click. |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| overflow menu button | `features/steps/core/overflow_menu.py:291` | `click_element`, AppiumBy.NAME. |
| Favorites option | `features/steps/core/overflow_menu.py:8` | `click_element`, AppiumBy.XPATH. |
| Favorites title | `features/steps/core/overflow_menu.py:31` | `verify_element_attribute`. |

## Unresolved Or Low-Confidence Items
- Source scenario is tagged `@wip`; converted as draft for team validation.

## Conversion Rules Applied
- Preserved source locators and blocking assertions.
- Kept AI-friendly target text alongside precise locators.

