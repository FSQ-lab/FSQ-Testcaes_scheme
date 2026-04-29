# FSQ AI Test DSL v1 Codex Specification

> Codex-produced artifact. This document defines the FSQ v1 AI Agent Friendly automated test DSL and execution contract.

## 1. Positioning

FSQ v1 is a Maestro-like declarative action DSL for AI-generated automated test cases. A testcase is not free-form natural language and is not raw Appium, pywinauto, or WebDriver code. It is a stable, schema-validated action description that an AI agent can generate, inspect, repair, and hand to a runner.

```text
Goal / Knowledge Base
  -> FSQ YAML testcase
  -> Parser-normalized command model
  -> Plan IR
  -> Appium 3.x / pywinauto MCP / CLI / WebDriver
  -> Evidence
  -> Repair
```

The testcase file focuses on flow and assertions. Evidence collection, repair policy, global retry strategy, model routing, and legacy conversion metadata belong in project policy files or executor configuration.

## 2. File Shape

Authoring YAML uses two documents separated by `---`:

1. Metadata document: testcase config.
2. Commands document: linear command list.

```yaml
schemaVersion: fsq.ai-test/v1
appId: com.microsoft.edgemac
name: Omnibox URL navigation
description: Verify that typing a URL in the omnibox navigates to the target site.
platform: macos
tags: [p0, omnibox]
env:
  TARGET_URL: www.163.com
---
- launchApp
- tapOn:
    text: Address and search bar
    timeout: 10000
- inputText: ${TARGET_URL}
- pressKey: Enter
- waitUntil:
    url:
      contains: "163.com"
    timeout: 15000
- assert:
    url:
      matches: "^https://www\\.163\\.com/?$"
- assertVisible:
    text: "163"
    optional: false
```

JSON Schema validates the parser-normalized model, not raw multi-document YAML text:

```json
{
  "config": {
    "schemaVersion": "fsq.ai-test/v1",
    "appId": "com.microsoft.edgemac",
    "name": "Omnibox URL navigation",
    "platform": "macos"
  },
  "commands": [
    "launchApp",
    { "tapOn": { "text": "Address and search bar", "timeout": 10000 } }
  ]
}
```

Required config fields:

- `schemaVersion`
- `name`
- one of `appId`, `url`, or `app`

Recommended config fields:

- `platform`
- `tags`
- `env`
- `description`
- `properties`
- `runner`

## 3. Design Principles

1. **Maestro-like shape**: top-level config, `---`, then a linear command list.
2. **One command per list item**: each command item has exactly one command key.
3. **Direct action commands**: use `tapOn`, `inputText`, `pressKey`, `assertVisible`, and `performActions` instead of vague intent commands.
4. **Schema first**: all commands and properties are represented in JSON Schema, with unknown fields rejected unless explicitly marked as extensions.
5. **String/object dual forms**: simple cases stay short, complex cases expand into typed objects.
6. **Appium 3 aligned**: W3C Actions use `performActions` and `releaseActions`; driver extensions use `executeMethod`.
7. **Knowledge-base friendly**: selectors, relation constraints, retry, optional, timeout, and platform conditions are allowed when produced from trusted knowledge and validated by schema.

## 4. Command Set

App lifecycle:

```text
launchApp
stopApp
killApp
clearState
setPermissions
```

Element interaction:

```text
tapOn
doubleTapOn
longPressOn
rightClickOn
hoverOn
inputText
clearText
pressKey
swipe
scrollUntilVisible
scroll
```

Assertions and waiting:

```text
assertVisible
assertNotVisible
assert
assertWithAI
waitUntil
waitForAnimationToEnd
```

Appium 3 escape hatches:

```text
performActions
releaseActions
executeMethod
```

Flow composition:

```text
runFlow
repeat
retry
```

Evidence helpers:

```text
takeScreenshot
startRecording
stopRecording
```

## 5. Command Shape

Bare command:

```yaml
- launchApp
- releaseActions
```

String shorthand:

```yaml
- tapOn: Login
- inputText: hello world
- pressKey: Enter
- assertVisible: Welcome
```

String shorthand has deterministic expansion. For selector-based commands, the string expands to `target`:

```yaml
- tapOn:
    target: Login
```

Object form is canonical for validation, repair, and Plan IR:

```yaml
- tapOn:
    target: Login
    locator:
      text: Login
    timeout: 10000
```

## 6. Selector Model

Selectors support common fields plus platform-specific fields.

```yaml
target: Login button
locator:
  text: Login
  id: login_button
  accessibilityId: login_button
  name: Login
  label: Login
  value: Login
  resourceId: com.example:id/login
  className: android.widget.Button
  xpath: //android.widget.Button[@text='Login']
  css: button.login
  predicate: "label == 'Login'"
  classChain: "**/XCUIElementTypeButton[`label == 'Login'`]"
  uiautomator: 'new UiSelector().text("Login")'
  automationId: login_button
  controlType: Button
  localizedControlType: button
  frameworkId: Win32
  processId: 1234
  handle: "0x000104A2"
  image: assets/login_button.png
  point:
    x: 120
    y: 240
  index: 0
  enabled: true
  visible: true
  selected: false
  checked: false
  focused: false
  below:
    text: Username
  containsDescendants:
    - text: Title
    - text: Subtitle
timeout: 10000
optional: false
retry: 2
```

Selector guidance:

- Prefer knowledge-base supplied stable selectors.
- Prefer accessibility identifiers when available.
- Prefer visible text when stable and unique.
- Use relation constraints to disambiguate repeated labels.
- Allow XPath and coordinates as explicit fallback, not the default generation strategy.

## 7. Target, Locator, And Relation Constraints

Selector-based commands may use a two-layer targeting model.

```yaml
- tapOn: "Settings and more button on toolbar"
```

This shorthand is a semantic target. The executor resolves it through the accessibility tree and returns structured locator candidates. Non-vision models must not use screenshots to guess coordinates.

```yaml
- tapOn:
    target: "Settings button from dropdown"
    locator:
      accessibilityId: SettingsButton
```

When `locator` is present, it is the primary execution contract. `target` is auxiliary context for review, logging, evidence, and repair.

```yaml
- inputText:
    text: "123456"
    target: "Password input field"
    locator:
      text: "Password"
      below:
        text: "Username"
```

Rules:

- `target` is a human-readable semantic description.
- `locator` is a structured selector used by the executor.
- `locator` may contain relation constraints such as `below`, `above`, `leftOf`, `rightOf`, `childOf`, `contains`, and `containsDescendants`.
- If `locator` exists, the executor uses it first.
- If multiple elements match, relation constraints disambiguate the match.
- If `locator` is absent, the executor may resolve `target` through the accessibility tree.
- If locator resolution fails, execution enters Repair flow instead of falling back to non-vision screenshot coordinate guessing.

## 8. Windows / pywinauto MCP Adapter

FSQ supports Windows through a platform adapter targeting the AutoGenesis `pywinauto-mcp-server`. This does not change the core action DSL.

```yaml
schemaVersion: fsq.ai-test/v1
name: Edge Windows omnibox navigation
platform: windows
app:
  name: edge
  exe: "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
  windowTitleRegex: ".*Microsoft Edge.*"
  launchArgs:
    - "--profile-directory=Default"
runner:
  backend: pywinauto-mcp
  mcpServer: auto-genesis-mcp-pywinauto-stdio
---
- launchApp
- tapOn:
    target: Address and search bar
    locator:
      name: Address and search bar
      controlType: Edit
      automationId: addressEditBox
- inputText: www.163.com
- pressKey: Enter
- assertVisible:
    locator:
      name: "163"
      controlType: Text
```

Mapping to current pywinauto MCP tools:

| FSQ command | pywinauto MCP tool |
| --- | --- |
| `launchApp` | `app_launch` |
| `stopApp` / `killApp` | `app_close` |
| `takeScreenshot` | `app_screenshot` |
| `tapOn` | `element_click` |
| `doubleTapOn` | `element_click` with `click_count: 2` |
| `rightClickOn` | `right_click` |
| `inputText` | `enter_text` or `send_keystrokes` |
| `pressKey` | `send_keystrokes` |
| `swipe` / drag | `mouse_drag_drop` |
| `scrollUntilVisible` / `scroll` | `mouse_scroll` |
| `hoverOn` | `mouse_hover` |
| `assertVisible` | `verify_element_exists` |
| `assertNotVisible` | `verify_element_not_exist` |
| `assert` for checkbox state | `verify_checkbox_state` |
| `assert` for element value | `verify_element_value` |
| `assertWithAI` | `verify_visual_task` |

Windows adapter rules:

- `automationId`, `name`, `controlType`, and `className` map naturally to pywinauto UIA lookup fields.
- `controlType` must come from UIA snapshot or knowledge base. The agent should not infer it from visible text.
- FSQ `index` is zero-based; pywinauto MCP `control_idx` is one-based.
- The adapter owns `control_framework`, defaulting to `pywinauto`.
- `timeout` is expressed in milliseconds in FSQ and converted to seconds for pywinauto MCP.
- `need_snapshot`, `scenario`, `step`, and `step_raw` are runner/evidence concerns, not authoring fields.

## 9. Appium 3 Actions And Execute Methods

`performActions` maps directly to W3C WebDriver Actions. Supported source types are `none`, `key`, `pointer`, and `wheel`. Supported action item types are `pause`, `keyDown`, `keyUp`, `pointerMove`, `pointerDown`, `pointerUp`, and `scroll`.

```yaml
- performActions:
    - type: pointer
      id: finger1
      parameters:
        pointerType: touch
      actions:
        - type: pointerMove
          duration: 0
          origin: viewport
          x: 200
          y: 700
        - type: pointerDown
          button: 0
        - type: pointerMove
          duration: 500
          origin: viewport
          x: 200
          y: 200
        - type: pointerUp
          button: 0
```

Driver-specific capabilities use `executeMethod`:

```yaml
- executeMethod:
    script: "mobile: activateApp"
    args:
      appId: com.microsoft.emmx
```

## 10. Generic Assert And Wait

FSQ includes generic `assert` and `waitUntil` commands for non-element state.

```yaml
- waitUntil:
    url:
      contains: "163.com"
    timeout: 15000

- assert:
    url:
      matches: "^https://www\\.163\\.com/?$"
```

Recommended assertion subjects are `url`, `title`, `text`, `element`, `clipboard`, `appState`, `orientation`, `network`, and `visual`. Recommended match operators are `equals`, `contains`, `matches`, `exists`, `notExists`, `isTrue`, and `isFalse`.

## 11. Flow Control And Conditions

```yaml
- runFlow: flows/login.yaml

- runFlow:
    file: flows/login.yaml
    env:
      USERNAME: ${USERNAME}
    when:
      platform: android

- repeat:
    times: 3
    commands:
      - tapOn: Next

- retry:
    maxRetries: 3
    commands:
      - tapOn: Reload
      - waitUntil:
          element:
            text: Loaded
          timeout: 10000
```

Condition fields are `platform`, `visible`, `notVisible`, `url`, `title`, and `expression`.

## 12. Executor Locator Resolution Policy

Executor may use the current accessibility tree plus the command target description to ask an LLM to infer the best locator strategy. The LLM must return structured locator candidates such as `accessibilityId`, `id`, `text`, `name`, `automationId`, `controlType`, or relation selectors. The executor then uses those locators through Appium, pywinauto, or the configured backend.

```text
Get current accessibility tree
  -> send accessibility tree + target description to LLM
  -> receive structured locator candidates
  -> execute action through Appium / pywinauto / configured backend
  -> on failure, enter Repair flow
```

If locator resolution fails, the executor must enter Repair flow. Repair may refresh the accessibility tree, choose an alternative stable locator, adjust wait timing, or disambiguate with parent and relation selectors. Repair must not weaken assertions, skip required actions, or change the test goal.

Non-vision models must never infer coordinates from screenshots. Locator failure must not fall back to screenshot-based coordinate guessing. Coordinate actions are allowed only when coordinates are explicitly authored, derived from backend-reported element bounds, produced by an approved vision model, or created by an allowed repair policy.

## 13. Policy Files

The following should not be repeated in every testcase:

- default evidence collection
- repair permissions
- global retry strategy
- screenshot and recording policy
- AI model routing
- BDD or legacy conversion metadata

```yaml
schemaVersion: fsq.ai-test-policy/v1
evidence:
  onFailure: [screenshot, accessibilityTree, appiumLogs]
  onSuccess: [finalScreenshot]
repair:
  allowed:
    - refineSelector
    - adjustWait
    - useAlternativeStableLocator
  forbidden:
    - weakenAssertion
    - skipCriticalAssertion
    - changeTestGoal
    - inferCoordinatesFromScreenshotWithoutVision
```

## 14. Schema Model

The JSON Schema validates the normalized `{ config, commands }` model and should enforce strict object properties, command items with exactly one command key, reusable selector definitions, W3C action source types, `executeMethod.script`, Windows app config, Windows UIA selector fields, and policy-layer separation for evidence and repair.

Recommended schema draft: JSON Schema draft 2020-12.
