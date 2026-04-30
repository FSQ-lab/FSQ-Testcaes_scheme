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

Implementation extraction rules:

- `click_element` -> `tapOn` with preserved locator.
- `send_keys` -> `inputText` with preserved locator and text.
- `verify_element_exists` -> `assertVisible` or `assert.element` with preserved locator.
- `verify_element_not_exists` -> `assertNotVisible` with preserved locator.
- `verify_element_attribute` -> `assert.element` plus state/text matcher when schema supports it.
- `press_key` -> `pressKey`.
- `swipe` -> `swipe` or `performActions`; do not convert it to prose `tapOn`.
- Screenshot analysis -> blocking `assertWithAI` or the runner's visual assertion path; never use screenshots for coordinate fallback.
- Helper/setup code -> explicit precondition commands only when required for isolated execution.

| Source intent | FSQ pattern |
| --- | --- |
| Launch browser/app | `launchApp` |
| Open a new tab | `tapOn: New Tab button` or platform-specific locator object |
| Navigate to URL | tap address bar, select all, `inputText`, `pressKey: Enter`, then `waitUntil.url` when navigation URL is stable |
| Search keyword | address bar input plus Enter, then `assertWithAI` or URL/title/text assertion |
| Click named UI | `tapOn.target` with locator only when known |
| Right click / hover | `rightClickOn` / `hoverOn` |
| Keyboard shortcut | `pressKey` object with `key` and `modifiers` |
| Dialog should appear | `assertVisible.target` |
| Visual layout/theme verification | blocking `assertWithAI` |
| Not displayed | `assertNotVisible.target` |
| Restart app | `stopApp`, then `launchApp` |


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

For Windows Edge cases, prefer accessibility-tree semantics and pywinauto-friendly fields:

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
