# Conversion Report

Codex-produced conversion report.

## Source
- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `features/favorite/favorite.feature`
- Feature: `favorite`
- Scenario: `Show and hide favorites bar`
- Tags: `@P0 @Regression @Favorites`

## Output
- Output YAML: `fsq-testcases/macos/favorites/show_and_hide_favorites_bar.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping
| Source step | FSQ command | Notes |
| --- | --- | --- |
| press Shift+cmd+B | `pressKey` | Preserves shortcut. |
| Favorites bar hidden | `assertNotVisible` | Preserves source XPath for `Import favorites`. |
| press Shift+cmd+B again | `pressKey` | Preserves shortcut. |
| Favorites bar shown | `assertVisible` | Preserves source XPath. |

## BDD Execution Model
- Direct scenario; no nested expansion.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| Edge temp profile launch | Setup/state guarantee | Partially | `launchApp` only; temp profile remains runner-owned. |

## Environment Requirements
- macOS Edge and Appium 3.x MCP runner.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `I press "Shift+cmd+B"...` | none | `press_key` with `shift+cmd+b`. |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| toggle favorites bar | `features/steps/favorite/favorite.py:656` | `press_key`, `shift+cmd+b`. |
| hidden assertion | `features/steps/favorite/favorite.py:676` | `verify_element_not_exists`, XPath. |
| shown assertion | `features/steps/favorite/favorite.py:717` | `verify_element_exists`, XPath. |

## Unresolved Or Low-Confidence Items
- Initial favorites bar visibility can make the first toggle invert expectations if runner does not use a clean profile.

## Conversion Rules Applied
- Preserved source shortcut and XPath assertions.

