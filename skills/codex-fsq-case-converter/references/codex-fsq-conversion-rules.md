# Codex FSQ Conversion Rules

## Selection Heuristics

Prefer pilot cases that exercise important product paths while staying executable:

- Omnibox/address bar navigation and search.
- Settings navigation and toggles.
- Downloads, favorites, history, and tab management with clear UI states.
- Scenarios tagged `p0`, `smoke`, or `regression` when not skipped or marked broken.

Avoid first-pass conversion for:

- Cases tagged `skip`, `need_fix`, or equivalent unless the user asks for them.
- Cases whose only executable behavior is coordinate-heavy gesture logic.
- Cases requiring special accounts, lab data, external services, or very large downloads unless the environment is already known.


## Lifecycle Policy

Every converted case must be self-contained:

```yaml
---
- launchApp
# scenario commands
- killApp
```

Rules:

- Preserve `launchApp` as the first command even when the source relies on a fixture/background.
- Append `killApp` as the final command so the next case starts from a clean app process.
- If the source scenario restarts the app mid-flow, keep that explicit `stopApp`/`killApp` plus `launchApp`, and still end with final `killApp`.
- Do not replace final `killApp` with `stopApp` unless the user explicitly asks for graceful close semantics.

## Step Mapping Patterns

For BDD/Behave sources, first resolve each feature step to the decorated Python implementation. Use the feature step for intent and human-readable target text, then use the implementation body for executable facts.

For Gherkin/Behave repositories, do this only after building the BDD Execution Model described in `codex-bdd-execution-model.md` and normalizing hooks described in `codex-behave-hook-normalization.md`. This file is the operation-to-command mapping layer, not the parser for BDD execution semantics.

Implementation extraction rules:

- `click_element` / `element_click` -> `tapOn` with preserved locator.
- `send_keys` / `enter_text` -> `inputText` with preserved locator and text.
- `send_keystrokes` -> `pressKey` for key tokens such as `{ENTER}`/`{F12}`, or `inputText` for literal text. Preserve source ordering.
- `native_navigate` -> `executeMethod` with the original URL and timeout, unless the target runner explicitly requires address-bar UI actions.
- `verify_element_exists` -> `assertVisible` or `assert.element` with preserved locator.
- `verify_element_not_exists` / `verify_element_not_exist` -> `assertNotVisible` with preserved locator.
- `verify_element_attribute` / `verify_element_value` -> `assert.element` plus source-observed state/text matcher when schema supports it.
- `verify_visual_task` / screenshot analysis -> blocking `assertWithAI` or the runner's visual assertion path; never use screenshots for coordinate fallback.
- `press_key` -> `pressKey`.
- `swipe` -> `swipe` or `performActions`; do not convert it to prose `tapOn`.
- `time_sleep` -> pause-style `performActions` only when the wait is material to execution.
- Helper/setup code -> explicit precondition commands only when required for isolated execution and safely supported by the DSL/runner. Unsupported setup must be listed as unresolved, not converted into a prose action.

Conditional helper rules:

- If source code checks for an optional dialog, permission prompt, cookie banner, or cleanup target and continues when it is absent, do not emit a blocking `assertVisible` for the probe.
- Preserve only the action that changes state, such as a best-effort dismiss/click, when the DSL/runner can express optional behavior safely.
- If optional helper behavior cannot be represented without changing semantics, record it in the conversion report as unresolved or low-confidence.

| Source intent | FSQ pattern |
| --- | --- |
| Launch browser/app | `launchApp` |
| Open a new tab | `tapOn: New Tab button` or platform-specific locator object |
| Navigate to URL | Preserve the source mechanism: `native_navigate` becomes `executeMethod`; address-bar implementations become tap/select/input/`pressKey: Enter`; only use `waitUntil.url` when source reads browser current URL or runner has a reliable current-URL API |
| Search keyword | address bar input plus Enter, then source-observed assertion (`assert.element`, title/text assertion, or `assertWithAI` when visual/semantic) |
| Click named UI | `tapOn.target` with locator only when known |
| Right click / hover | `rightClickOn` / `hoverOn` |
| Keyboard shortcut | `pressKey` object with `key` and `modifiers` |
| Dialog should appear | `assertVisible.target` |
| Visual layout/theme verification | blocking `assertWithAI` |
| Not displayed | `assertNotVisible.target` |
| Restart app | `stopApp`, then `launchApp` |



## Preconditions And Unsupported Setup

Convert setup only when it has a safe, executable representation:

- App launch/relaunch -> `launchApp`, `stopApp`, or `killApp`/`launchApp` as appropriate.
- Clear app/browser state -> `clearState` only when the target runner supports it for that platform.
- Windows temporary user data or native setup -> `executeMethod` only when the runner exposes the same operation.
- Account login, external lab data, uninstall/reinstall, clearing downloads/cache, and device/system state changes -> explicit commands only when the project runner has a known implementation.

When no safe equivalent exists, do not invent a UI action from the BDD sentence. Add the item to `Unresolved Or Low-Confidence Items` with the source file/line and expected environment state.

## URL And Current Page Assertions

Use the assertion source that the original implementation actually observes:

- Address bar text or URL field attribute -> `assert.element` plus `text.contains`/`text.equals` using the preserved locator.
- Tab title, WebView text, page heading, or document node -> locator-backed `assertVisible` or `assert.element`.
- Browser current URL API or runner-provided current page state -> `assert.url` / `waitUntil.url`.
- Visual completeness, layout, blank page, theme, or image/icon-only evidence -> blocking `assertWithAI`.

Do not upgrade a UI-state assertion to bare `assert.url` only because the BDD sentence says "navigate to".

## Android Behave Lessons From Pilot Runs

Apply these rules when converting Android Behave cases with Appium step implementations:

- Preserve operation order inside compound BDD steps. A step such as `input ... and click Go` maps to source order: focus/type first, then `pressKey: Enter`; never emit `tapOn: Go` before `inputText`.
- Preserve exact source swipe coordinates when the implementation uses Appium `swipe(start_x, start_y, end_x, end_y, duration)`. Convert those to W3C `performActions` pointer sequences when generic `swipe.direction` would change the gesture target or path.
- Convert waits and page-scroll helper steps to executable waits or gestures, not prose `tapOn` commands. If a source step is `time_sleep`, use a pause-style `performActions` only when the wait is material to execution.
- Convert Behave fixtures, `before_scenario`, `Background`, and helper setup when they materially establish NTP, signed-in state, top/bottom omnibox mode, or tab count. Do not assume source fixtures are automatically applied by the FSQ runner.
- Treat helper flows such as `Given I login to edge with MSA` as preconditions or expanded helper flows. Do not convert them into a single `tapOn` against the sentence text.
- When the source says the app should return to NTP, convert that to an assertion for the NTP surface, not an extra `Add new tab` action.
- Preserve locator-backed icon, topsite, suggestion-list, refresh, and URL/current-page assertions from the step implementation. Use screenshot AI only when the source assertion is truly visual or no accessibility locator exists.
- For tab thumbnail close actions, prefer the most specific locator visible in source/evidence, such as resource id plus content description, before using broad sibling XPath.

## Locator Policy

Use semantic target first when uncertain:

```yaml
- tapOn:
    target: Settings and more button on toolbar
```

Use dual-layer targeting when the locator is known:

```yaml
- tapOn:
    target: Settings and more button on toolbar
    locator:
      name: Settings and more
      controlType: Button
```

Use relation locators only when the source step gives real context:

```yaml
- inputText:
    text: '123456'
    target: Password input box
    locator:
      text: Password
      below:
        text: Username
```

Do not convert vague source text into arbitrary `id`, `automationId`, XPath, CSS, or coordinates.

## AI And Repair Principles

Executor-side behavior should be:

1. Get the current accessibility tree.
2. Send accessibility tree plus target description to the LLM when semantic resolution is needed.
3. Let the LLM infer the best locator strategy from accessible information.
4. Execute through Appium, pywinauto MCP, WebDriver, or the configured backend.
5. On failure, enter repair flow: analyze element-not-found, wrong state, or page-not-ready, then retry with an adjusted strategy.

Prohibited conversion behavior:

- Do not screenshot-guess coordinates under a non-vision model.
- Do not fallback to visual guessing when accessibility location fails.
- Do not encode repair policy in every case unless the repo explicitly asks for it.

## Assertion Policy

Use blocking assertions by default:

```yaml
- assertVisible:
    target: Delete browsing data dialog
```

For structured assertions:

```yaml
- assert:
    url:
      contains: edge://settings
    optional: false
```

For AI assertions:

```yaml
- assertWithAI:
    prompt: Verify the active tab shows Bing search results related to "cat".
    optional: false
    timeout: 30000
```

## Windows Notes

For Windows Edge cases, preserve pywinauto MCP source operations before falling back to synthetic UI actions. In particular, `native_navigate` should map to `executeMethod` with the original URL/timeout, because that is the source runner contract. Use address-bar click/type/Enter only when the source implementation actually performs address-bar UI actions.

Prefer accessibility-tree semantics and pywinauto-friendly fields:

```yaml
platform: windows
app:
  name: edge
  exe: C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
  windowTitleRegex: .*Microsoft Edge.*
runner:
  backend: pywinauto-mcp
```

Common Windows locator fields:

- `name`
- `automationId`
- `controlType`
- `className`
- `frameworkId`

Address bar convention:

```yaml
locator:
  name: Address and search bar
  controlType: Edit
```

## Final Checks

Before committing:

- Count generated `.codex.yaml` and `.codex-conversion-report.md` files.
- Validate all generated YAML against the schema.
- Search for accidental coordinates, YAML anchors, aliases, or `optional: true`.
- Sample-read at least one YAML and one report from each platform/area.
- Confirm source repos were not modified.
