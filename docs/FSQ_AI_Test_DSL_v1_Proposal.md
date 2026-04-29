# FSQ AI Test DSL v1 Proposal

> Review draft for an AI Agent Friendly automated test case DSL and schema.

## 1. Positioning

FSQ v1 should define a **Maestro-like declarative action DSL** for AI-generated test cases.

The testcase YAML is not free-form natural language and is not raw Appium code. It is a stable, schema-validated action description that an AI agent can generate, inspect, repair, and hand to a runner. The runner lowers the DSL into Plan IR, then into Appium 3.x MCP, CLI, or WebDriver execution.

```text
Goal / Knowledge Base
  -> FSQ YAML testcase
  -> Plan IR
  -> Appium 3.x MCP / CLI / WebDriver
  -> Evidence
  -> Repair
```

The testcase file should focus on the flow and assertions. Project-wide evidence collection, repair policy, global retry strategy, and legacy conversion reports should live outside individual testcase YAML files.

## 2. Design Principles

1. **Maestro-like shape**: top-level config, `---`, then a linear command list.
2. **One command per list item**: each command item has exactly one command key.
3. **Direct action commands**: use action names like `tapOn`, `inputText`, `pressKey`, `assertVisible`, and `performActions`.
4. **Schema first**: all commands and properties are represented in JSON Schema, with unknown fields rejected unless explicitly marked as extensions.
5. **String/object dual forms**: simple cases stay short, complex cases expand into typed objects.
6. **Appium 3 aligned**: use W3C Actions through `performActions`/`releaseActions`, and driver extensions through `executeMethod`.
7. **Knowledge-base friendly**: selectors, relation selectors, retry, optional, timeout, and platform conditions are allowed when produced from trusted knowledge and validated by schema.

## 3. Recommended File Shape

```yaml
schemaVersion: fsq.ai-test/v1
appId: com.microsoft.edgemac
name: Omnibox URL navigation
description: Verify that typing a URL in the omnibox navigates to the target site.
platform: macos
tags:
  - p0
  - omnibox
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

Required config fields:

- `schemaVersion`
- one of `appId` or `url`
- `name`

Recommended config fields:

- `platform`
- `tags`
- `env`
- `description`
- `properties`

## 4. Command Set v1

The v1 command set should be broad enough to avoid redesign, but still small enough for AI to learn reliably.

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
inputText
clearText
pressKey
swipe
scrollUntilVisible
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

Evidence helper commands may exist in a flow, but default evidence policy should live outside testcase YAML.

## 5. Command Shape

Bare command:

```yaml
- launchApp
- releaseActions
```

Only commands with no required arguments may use the bare form.

String shorthand:

```yaml
- tapOn: Login
- inputText: hello world
- pressKey: Enter
- assertVisible: Welcome
```

String shorthand must have deterministic expansion. For example:

```yaml
- tapOn: Login
```

expands to:

```yaml
- tapOn:
    text: Login
```

Object form:

```yaml
- tapOn:
    text: Login
    below: Username
    timeout: 10000
```

Object form is the canonical representation for validation, repair, and Plan IR.

## 6. Selector Model

Selectors should follow Maestro's string/object dual shape, with additional fields for Appium cross-platform support.

```yaml
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
below: Username
above: Forgot password
leftOf: Cancel
rightOf: Icon
childOf:
  id: login_form
contains:
  text: Icon
containsDescendants:
  - text: Title
  - text: Subtitle
timeout: 10000
optional: false
retry: 2
label: Tap login button
```

Selector guidance:

- Prefer knowledge-base supplied stable selectors.
- Prefer accessibility identifiers when available.
- Prefer visible text when stable and unique.
- Use relation selectors to disambiguate repeated labels.
- Allow XPath and coordinates as explicit fallback, not the default generation strategy.

### Target, Locator, And Relation Constraints

Selector-based commands may use a two-layer targeting model when semantic intent and precise locator data both matter.

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

Relation constraints belong inside `locator`, so it is clear that they disambiguate locator matches rather than describe the command as a whole.

Targeting rules:

- `target` is a human-readable semantic description.
- `locator` is a structured selector used by the executor.
- `locator` may contain relation constraints such as `below`, `above`, `leftOf`, `rightOf`, `childOf`, `contains`, and `containsDescendants`.
- If `locator` exists, the executor uses it first.
- If multiple elements match, relation constraints disambiguate the match.
- If `locator` is absent, the executor may resolve `target` through the accessibility tree.
- If locator resolution fails, execution enters Repair flow instead of falling back to non-vision screenshot coordinate guessing.

Windows UIA selector guidance:

- `automationId`, `name`, `controlType`, and `className` map naturally to pywinauto UIA lookup fields.
- `controlType` must come from UIA snapshot or knowledge base. The agent should not infer it from visible text.
- `index` is zero-based in the FSQ DSL. The pywinauto MCP adapter translates it to `control_idx`, which is one-based.
- `parent` relation selectors should lower to `parent_name`, `parent_control_type`, and `parent_automation_id` for pywinauto.
- `localizedControlType`, `frameworkId`, `processId`, and `handle` are diagnostic or advanced fields. They are allowed for evidence and repair, but should not be required for normal authoring.

## 7. Windows / pywinauto MCP Adapter

FSQ should support Windows through a platform adapter that targets the existing AutoGenesis `pywinauto-mcp-server`. This should not change the core action DSL. Test authors still write `launchApp`, `tapOn`, `inputText`, `pressKey`, `assertVisible`, and `takeScreenshot`; the runner lowers those commands into pywinauto MCP tools.

Reference backend: [AutoGenesis pywinauto MCP server](https://github.com/microsoft/AutoGenesis/tree/main/pywinauto-mcp-server).

Windows app config should support the same concepts as the MCP server config:

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
    name: Address and search bar
    controlType: Edit
    automationId: addressEditBox
- inputText: www.163.com
- pressKey: Enter
- assertVisible:
    name: "163"
    controlType: Text
```

Recommended Windows config fields:

```text
app.name
app.exe
app.windowTitleRegex
app.launchArgs
runner.backend
runner.mcpServer
```

Mapping to the current pywinauto MCP tools:

| FSQ command | pywinauto MCP tool | Mapping notes |
| --- | --- | --- |
| `launchApp` | `app_launch` | Uses `exe`, `window_title_re`, and `launch_args` from app config. |
| `stopApp` / `killApp` | `app_close` | The current server closes and kills matching app processes. |
| `takeScreenshot` | `app_screenshot` | Captures the main app window. |
| `tapOn` | `element_click` | `click_count: 1`; selector lowers to `name`, `control_type`, `automation_id`, `class_name`, parent fields. |
| `doubleTapOn` | `element_click` | `click_count: 2`. |
| `rightClickOn` | `right_click` | Should be included in v1 if Windows desktop context matters. |
| `inputText` after focused element | `enter_text` or `send_keystrokes` | Prefer `enter_text` when a selector is supplied; use `send_keystrokes` for active focus or shortcuts. |
| `pressKey` | `send_keystrokes` | Runner maps normalized key names to pywinauto keystroke syntax. |
| `swipe` / drag | `mouse_drag_drop` | Supports element-to-element, pixel-to-element, and offset drag. |
| `scrollUntilVisible` / `scroll` | `mouse_scroll` | Wheel distance and target selector lower to MCP arguments. |
| `hoverOn` | `mouse_hover` | Add as an optional v1 desktop/web command if hover scenarios are common. |
| `assertVisible` | `verify_element_exists` | Same selector lowering as click. |
| `assertNotVisible` | `verify_element_not_exist` | Same selector lowering as click. |
| `assert` for checkbox state | `verify_checkbox_state` | Lower from `assert.element.checked` or `assert.element.selected`. |
| `assert` for element value | `verify_element_value` | Lower from `assert.element.value`. |
| `assertWithAI` | `verify_visual_task` | Visual assertion remains blocking unless `optional: true` is explicit. |

Selector lowering example:

```yaml
- tapOn:
    name: Settings
    controlType: Button
    automationId: SettingsButton
    parent:
      name: Toolbar
      controlType: ToolBar
    timeout: 5000
```

lowers to:

```json
{
  "tool": "element_click",
  "arguments": {
    "control_framework": "pywinauto",
    "name": "Settings",
    "control_type": "Button",
    "automation_id": "SettingsButton",
    "parent_name": "Toolbar",
    "parent_control_type": "ToolBar",
    "control_idx": 1,
    "timeout": 5,
    "click_count": 1
  }
}
```

Windows adapter rules:

- The DSL uses `timeout` in milliseconds. The pywinauto MCP adapter converts to seconds.
- The DSL uses `optional: false` by default. MCP `failed` and `error` statuses are blocking unless optional is explicit.
- The adapter should pass `scenario`, `step`, and `step_raw` from runner context for logging and code generation, not require authors to write them in YAML.
- `need_snapshot` should be controlled by evidence policy, not repeated in testcase YAML.
- Coordinate and pixel operations are allowed only when explicit in the YAML or produced by a trusted repair step.
- `control_framework` is adapter-owned and should default to `pywinauto`; authors should not need to set it in ordinary cases.

## 8. Appium 3 Action Alignment

`performActions` maps directly to W3C WebDriver Actions.

Supported source types:

```text
none
key
pointer
wheel
```

Supported action items:

```text
pause
keyDown
keyUp
pointerMove
pointerDown
pointerUp
scroll
```

Touch swipe example:

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

Keyboard shortcut example:

```yaml
- performActions:
    - type: key
      id: keyboard
      actions:
        - type: keyDown
          value: "\uE03D"
        - type: keyDown
          value: l
        - type: keyUp
          value: l
        - type: keyUp
          value: "\uE03D"
```

Release actions:

```yaml
- releaseActions
```

## 9. Appium Execute Methods

Appium 3 removes or de-emphasizes several older endpoints. Driver-specific capabilities should use execute methods.

```yaml
- executeMethod:
    script: "mobile: activateApp"
    args:
      appId: com.microsoft.emmx
```

```yaml
- executeMethod:
    script: "macos: launchApp"
    args:
      bundleId: com.microsoft.edgemac
```

Schema rules:

- `script` is required.
- `args` is an object and defaults to `{}`.
- `script` should allow prefixes such as `mobile:`, `macos:`, `windows:`, and project-owned prefixes.

## 10. Generic Assert And Wait

Element assertions are not enough for browser and desktop tests. FSQ should include generic `assert` and `waitUntil` commands for non-element state.

```yaml
- waitUntil:
    url:
      contains: "163.com"
    timeout: 15000
```

```yaml
- assert:
    url:
      matches: "^https://www\\.163\\.com/?$"
```

Recommended assertion subjects:

```text
url
title
text
element
clipboard
appState
orientation
network
visual
```

Recommended match operators:

```text
equals
contains
matches
exists
notExists
isTrue
isFalse
```

## 11. Flow Control And Conditions

```yaml
- runFlow: flows/login.yaml
```

```yaml
- runFlow:
    file: flows/login.yaml
    env:
      USERNAME: ${USERNAME}
    when:
      platform: android
```

```yaml
- repeat:
    times: 3
    commands:
      - tapOn: Next
```

```yaml
- retry:
    maxRetries: 3
    commands:
      - tapOn: Reload
      - waitUntil:
          element:
            text: Loaded
          timeout: 10000
```

Condition fields:

```text
platform
visible
notVisible
url
title
expression
```

## 12. Executor Locator Resolution Policy

Executor may use the current accessibility tree plus the command target description to ask an LLM to infer the best locator strategy. The LLM must return structured locator candidates such as `accessibilityId`, `id`, `text`, `name`, `automationId`, `controlType`, or relation selectors. The executor then uses those locators through Appium, pywinauto, or the configured backend.

Locator resolution should follow this flow:

```text
Get current accessibility tree
  -> send accessibility tree + target description to LLM
  -> receive structured locator candidates
  -> execute action through Appium / pywinauto / configured backend
  -> on failure, enter Repair flow
```

If locator resolution fails, the executor must enter the Repair flow. Repair may refresh the accessibility tree, choose an alternative stable locator, adjust wait timing, or disambiguate with parent and relation selectors. Repair must not weaken assertions, skip required actions, or change the test goal.

Non-vision models must never infer coordinates from screenshots. Locator failure must not fall back to screenshot-based coordinate guessing. Coordinate actions are allowed only when coordinates are explicitly authored, derived from backend-reported element bounds, produced by an approved vision model, or created by an allowed repair policy.

This policy belongs in the executor and repair layer, not in every testcase YAML file.

## 13. Policy Files Outside Testcase YAML

The following should not be repeated in every testcase:

- default evidence collection
- repair permissions
- global retry strategy
- screenshot and recording policy
- AI model routing
- BDD or legacy conversion metadata

Recommended policy shape:

```yaml
schemaVersion: fsq.ai-test-policy/v1
evidence:
  onFailure:
    - screenshot
    - accessibilityTree
    - appiumLogs
  onSuccess:
    - finalScreenshot
repair:
  allowed:
    - refineSelector
    - adjustWait
    - useAlternativeStableLocator
  forbidden:
    - weakenAssertion
    - skipCriticalAssertion
    - changeTestGoal
```

## 14. Schema Requirements

The JSON Schema should enforce:

- top-level config fields before command list
- command list with at least one command
- exactly one command key per command item
- no unknown command keys
- strict object properties by default
- string/object dual forms for selector-based commands
- W3C action source types and action item types
- `executeMethod.script` required
- `optional`, `timeout`, and `retry` types and ranges
- recursive selector relation fields
- enum validation for platform, pointer type, orientation, and match operators
- Windows `app.exe`, `app.windowTitleRegex`, and `app.launchArgs` fields
- Windows UIA selector fields such as `automationId`, `controlType`, `frameworkId`, `processId`, and `handle`
- Executor locator resolution and repair policy as external policy, not repeated testcase fields

Recommended schema draft: `JSON Schema draft 2020-12`.

Use `oneOf` for command variants and `$defs` for reusable selector, condition, assertion, W3C action, and execute method definitions.

## 15. Differences From Current Draft

The current `AI_Test_Agent_DSL_Design.md` should be updated in these ways:

- Replace snake_case commands with Maestro-style camelCase commands.
- Prefer `appId + --- + command list` over `config.steps` as the primary authoring format.
- Add `performActions`, `releaseActions`, and `executeMethod`.
- Replace deprecated Appium mappings such as `TouchAction`, `driver.swipe`, `driver.reset`, and `driver.launch_app` with W3C Actions and Appium execute methods.
- Expand selector fields for macOS, iOS, Android, and web contexts.
- Add Windows UIA selector fields and pywinauto MCP adapter mapping.
- Add executor locator resolution policy based on accessibility tree, structured locator candidates, and repair flow.
- Add generic `assert` and `waitUntil` for URL/title/app state assertions.
- Move evidence and repair defaults into policy files.
- Keep BDD conversion outside the testcase DSL.

## 16. Recommended Next Step

After this proposal is reviewed, create two production artifacts:

1. `docs/fsq-ai-test-dsl-v1.md`: finalized DSL specification.
2. `docs/fsq-ai-test-dsl-v1.schema.json`: JSON Schema draft 2020-12 definition.
