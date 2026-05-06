# Conversion Report

Codex-produced conversion report.

## Source
- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `features/settings_and_more/settings_and_more.feature`
- Feature: `Settings and more functionality`
- Scenario: `Open a new Inprivate window by clicking the "Settings and more" button`
- Tags: `@regression @p0 @settings_and_more @inprivate_mode`

## Output
- Output YAML: `fsq-testcases/macos/settings_and_more/open_new_inprivate_window_by_clicking_settings_and_more_button.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping
| Source step | FSQ command | Notes |
| --- | --- | --- |
| click Settings and more | `tapOn` | Reuses shared source locator `Settings and more`. |
| select New InPrivate window | `tapOn` | Preserves accessibility id with shortcut text. |
| InPrivate window/icon assertions | `assertVisible` x2 | Preserves source accessibility ids. |
| click icon and verify popup text | `tapOn` + `assert` | Preserves XPath text check. |

## BDD Execution Model
- Direct scenario resolved from feature and step implementation.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| Edge temp profile launch | Setup/state guarantee | Partially | `launchApp` only; temp profile remains runner-owned. |
| evidence hooks | Evidence policy | No | Not case behavior. |

## Environment Requirements
- macOS Edge and Appium 3.x MCP runner.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `I select "New InPrivate window"...` | none | `click_element` with accessibility id. |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| Settings and more | `features/steps/settings/settings.py:10` | `click_element`, accessibility id `Settings and more`. |
| New InPrivate window | `features/steps/settings_and_more/settings_and_more.py:230` | `click_element`, accessibility id. |
| InPrivate assertions | `features/steps/settings_and_more/settings_and_more.py:251` | `verify_element_exists`, `verify_element_attribute`. |

## Unresolved Or Low-Confidence Items
- Source uses `context.app_window_name`; converted to the default visible title `Microsoft Edge` for review.

## Conversion Rules Applied
- Preserved source accessibility IDs and blocking assertions.

