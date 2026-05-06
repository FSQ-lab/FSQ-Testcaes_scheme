# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/search_bottom_mode.feature`
- Feature: `search`
- Scenario: `Input complete keyword in search box`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/ios/search_bottom_mode/input_complete_keyword_in_search_box.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I click + button on the bottom toolbar` | `tapOn` | Converted from matched step implementation. |
| `When I click on the search box on NTP page` | `tapOn` | Converted from matched step implementation. |
| `And I input a keyword "machine learning tutorials" in the search box` | `inputText` | Converted from matched step implementation. |
| `And I click "Go" on keyboard` | `tapOn` | Converted from matched step implementation. |
| `When I dismiss the permission dialog from bing` | `assertVisible, tapOn, assertVisible, tapOn, assertVisible, tapOn` | Converted from matched step implementation. |
| `Then Analyze the screenshot to verify search result is machine learning related` | `assertWithAI` | Converted from matched step implementation. |
| `And I scroll the page up for 2 seconds` | `performActions` | Converted from matched step implementation. |
| `And I scroll the page down for 2 seconds` | `performActions` | Converted from matched step implementation. |
| `Then I should navigate to bing.com with "machine learning tutorials" in search box` | `assert` | Converted from matched step implementation. |

## BDD Execution Model

- Converted using the latest Codex FSQ Case Converter rule: feature scenario supplies intent and order; Behave step implementations supply executable operations, locators, assertions, waits, and helper behavior.
- Effective steps include Gherkin Background plus scenario steps when present.
- `features/steps/**/*.py` is treated as the global Behave step registry; matching is by exact or parameterized decorator before semantic fallback.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| `before_all` / Appium session setup | runner lifecycle / environment requirements | No | Keep Appium/MCP session creation and telemetry out of case YAML. |
| `before_scenario` / setup helpers | setup/state guarantee | Partial | Material app launch/NTP assumptions are represented by `launchApp`; optional dialogs remain runner repair/evidence unless safely expressible. |
| `after_scenario` / result capture | runtime evidence | No | Screenshots, reports, and logs are not converted into case commands. |

## Environment Requirements

- iOS Edge app installed and launchable with Appium 3.x MCP.
- Account credentials are required only for account/MSA/rewards flows and are not written into YAML.
- Source runtime screenshots/logs are runner evidence, not case commands.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| Scenario steps | none or already reflected in Step Implementation Evidence | No unresolved `context.execute_steps()` expansion was identified during this report upgrade; any material setup/precondition is documented in Hook Normalization or Unresolved items. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `When I click + button on the bottom toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:396` | operations=click_element; locator={"accessibilityId": "kToolbarEdgeNewTabButtonIdentifier"} |
| `When I click on the search box on NTP page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:11` | operations=click_element; locator={"name": "Search and address bar"} |
| `And I input a keyword "machine learning tutorials" in the search box` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:446` | operations=send_keys; locator={"name": "Address"} |
| `And I click "Go" on keyboard` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:433` | operations=click_element; locator={"name": "Go"} |
| `When I dismiss the permission dialog from bing` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:477` | operations=verify_element_exists, click_element, verify_element_exists, click_element, verify_element_exists, click_element, Accept; locator={"name": "Allow While Using App"} |
| `Then Analyze the screenshot to verify search result is machine learning related` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:595` | operations=verify_visual_task |
| `And I scroll the page up for 2 seconds` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:130` | operations=swipe |
| `And I scroll the page down for 2 seconds` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:146` | operations=swipe |
| `Then I should navigate to bing.com with "machine learning tutorials" in search box` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:460` | operations=verify_element_attribute; locator={"name": "Search and address bar"} |

## Unresolved Or Low-Confidence Items

- None

## Conversion Rules Applied

- Applied Codex dual-source conversion: feature scenario for intent/order and Behave step implementation for executable operations.
- Preserved source locators from Appium/pywinauto step definitions where available.
- Preserved URL/current-page checks as locator-backed element assertions when source code verifies UI state.
- Converted screenshot/visual checks to blocking `assertWithAI` assertions instead of coordinate fallback.
- Every case starts with `launchApp` and ends with `killApp` for isolated runs.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm app identity and runner backend match the target execution environment.
- Confirm semantic targets remain specific enough for accessibility-tree locator resolution.
- Confirm any unresolved source steps before using this case for gating.
- Confirm visual assertions are run with a vision-capable analysis path.
