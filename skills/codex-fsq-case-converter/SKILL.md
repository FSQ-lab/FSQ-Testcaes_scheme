---
name: codex-fsq-case-converter
description: Use when converting platform-specific automated test cases, BDD/Gherkin feature files, Behave scenarios, Maestro-like flows, or manually written UI test cases into FSQ AI Test DSL Codex YAML and conversion reports.
---

# Codex FSQ Case Converter

## Overview

Convert source UI test cases into FSQ AI Test DSL v1 artifacts that are easy for an AI agent to execute, review, repair, and validate. Keep conversion conservative: preserve source intent, avoid invented locators, and prefer semantic targets plus known accessibility locators.

## Output Contract

Create outputs in the destination repo, not the source test repo:

```text
fsq-testcases/<platform>/<area>/<scenario_slug>.codex.yaml
fsq-testcases/<platform>/<area>/<scenario_slug>.codex-conversion-report.md
```

Use the two-document YAML shape:

```yaml
schemaVersion: fsq.ai-test/v1
name: Example scenario
platform: windows
app:
  name: edge
runner:
  backend: pywinauto-mcp
tags: [p0, codex-converted]
---
- launchApp
- tapOn:
    target: Address bar
- inputText:
    text: https://www.bing.com
    target: Address bar
- pressKey: Enter
- waitUntil:
    url:
      contains: bing.com
    timeout: 30000
    optional: false
```

Every generated artifact must include `codex` in the filename or artifact name.

## Workflow

1. Inspect existing converted cases in the destination repo before writing new ones.
2. Read source feature/scenario files and nearby step definitions when available.
3. Select cases with clear action/assertion intent first; avoid skipped, broken, highly coordinate-driven, or environment-heavy cases in pilot batches.
4. Convert source steps into direct FSQ actions: `tapOn`, `inputText`, `pressKey`, `assertVisible`, `assert`, `assertWithAI`, `performActions`, or `executeMethod` only when needed.
5. Preserve `steps` as commands; do not collapse a scenario into a prose objective.
6. Generate a conversion report for each case with source path, scenario name, tags, step mapping, unresolved items, and manual review checklist.
7. Validate all generated YAML against the FSQ schema before claiming completion.
8. Commit converted cases only after validation passes.

## Conversion Discipline

Read `references/codex-fsq-conversion-rules.md` when converting more than one case, adding a new platform, or handling ambiguous locators/assertions.

Core rules:

- Do not guess coordinates.
- Do not use screenshot-based coordinate inference under a non-vision model.
- Convert screenshot verification into blocking `assertWithAI`, not a fallback tap location.
- Do not invent stable locators. Use semantic `target` when locator is unknown.
- Use a dual-layer locator only when the source, knowledge base, or platform convention supports it.
- Keep assertions blocking by default; use `optional: true` only when the source explicitly treats the check as optional.
- Add `launchApp` when source background/fixture clearly launches the app or the scenario cannot run without it.
- Keep repair/evidence policy out of each case unless the schema or repo convention explicitly requires it.

## Platform Defaults

Use these defaults unless the repo already has more specific local conventions:

| Platform | Config default |
| --- | --- |
| macos | `platform: macos`, `appId: com.microsoft.edgemac` |
| android | `platform: android`, `appId: com.microsoft.emmx` |
| ios | `platform: ios`, `appId: com.microsoft.msedge` |
| windows | `platform: windows`, `app.name: edge`, `runner.backend: pywinauto-mcp` |

For Windows Edge, prefer this when useful:

```yaml
app:
  name: edge
  exe: C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
  windowTitleRegex: .*Microsoft Edge.*
runner:
  backend: pywinauto-mcp
```

Known address bar locator pattern:

```yaml
locator:
  name: Address and search bar
  controlType: Edit
```

## Validation

Run the bundled validator from the destination repo root:

```bash
python3 skills/codex-fsq-case-converter/scripts/validate_fsq_cases.py \
  --schema docs/codex-fsq-ai-test-dsl-v1.schema.json \
  --cases fsq-testcases
```

The validator expects raw FSQ multi-document YAML and validates the normalized `{config, commands}` model.

## Reports

Each `.codex-conversion-report.md` should include:

```markdown
# Conversion Report

Codex-produced conversion report.

## Source
- Source repo: `<path-or-url>`
- Source feature: `<path>`
- Feature: `<area>`
- Scenario: `<name>`
- Tags: `<tags>`

## Output
- Output YAML: `<path>`
- Platform: `<platform>`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping
| Source step | FSQ command | Notes |
| --- | --- | --- |

## Unresolved Or Low-Confidence Items

## Conversion Rules Applied

## Manual Review Checklist
```

## Common Mistakes

- Waiting for a URL after a direct download URL when the browser may keep focus on the current page. Prefer asserting the downloads panel/page state.
- Turning BDD phrases into prose `step` items. Use direct action commands instead.
- Adding locator fields because they look plausible. Keep unknowns semantic and let the executor resolve through the accessibility tree and repair flow.
- Marking AI visual assertions optional. Visual assertions often carry the real product requirement.
- Editing source test repositories. Treat them as read-only unless the user explicitly asks otherwise.
