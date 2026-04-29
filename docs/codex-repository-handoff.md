# Codex Repository Handoff

## Current Scope

This repository contains the Codex-produced FSQ AI Test DSL artifacts, converted cases, and local skills for manual conversion and execution handoff.

## Primary Artifacts

- `docs/codex-fsq-ai-test-dsl-v1.md`: FSQ AI Test DSL v1 design document.
- `docs/codex-fsq-ai-test-dsl-v1.schema.json`: JSON Schema for Codex DSL cases.
- `docs/codex-fsq-case-converter-design.md`: converter design notes.
- `skills/codex-fsq-case-converter/`: Codex skill for converting source cases into FSQ DSL YAML.
- `skills/codex-fsq-case-runner/`: Codex skill for selecting, validating, manifesting, and running cases through a backend runner command.
- `fsq-testcases/`: converted Codex YAML cases and per-case conversion reports.

## Converted Case Inventory

| Platform | Cases | Conversion Reports |
| --- | ---: | ---: |
| Android | 20 | 20 |
| iOS | 20 | 20 |
| macOS | 20 | 20 |
| Windows | 20 | 20 |
| Total | 80 | 80 |

## Generated Local Evidence

Runtime outputs such as `runs/`, `logs/`, screenshots, JSONL results, videos, traces, and other evidence files are intentionally ignored by git. They can be regenerated locally and should not be committed unless the team intentionally creates a curated report artifact.

## Validation Commands

Validate all converted cases against the Codex schema:

```bash
python3 skills/codex-fsq-case-converter/scripts/validate_fsq_cases.py \
  --schema docs/codex-fsq-ai-test-dsl-v1.schema.json \
  --cases fsq-testcases
```

List Android cases:

```bash
python3 skills/codex-fsq-case-runner/scripts/list_fsq_cases.py \
  --cases fsq-testcases \
  --platform android
```

Run one case through a concrete backend runner command:

```bash
python3 skills/codex-fsq-case-runner/scripts/run_fsq_cases.py \
  --cases fsq-testcases/android/bottom_bar/access_settings_through_overflow_menu.codex.yaml \
  --runner-command "<runner> --case {case} --backend {backend} --output {output} --manifest {manifest}"
```

## Android Execution Notes

The local Android smoke execution proved that Appium 3.x, UiAutomator2, device connectivity, schema validation, manifest generation, and basic bottom-bar menu flows can work end to end.

Observed Android results from the current local runs:

- 4 bottom-bar cases passed with the temporary local Appium runner.
- 16 previously failing cases still failed after switching the Android device UI to English.
- The main remaining gap is not language alone. The runner needs a real accessibility-tree driven semantic target resolver and repair classifier.

Failure classes observed during Android retry:

- Visual or screenshot semantic assertions require a vision-capable assertion path and must not fall back to non-vision coordinate guessing.
- Account-dependent flows need explicit login or profile preconditions.
- Natural-language compound actions need semantic parsing, such as selecting quoted suggestion text from a list.
- UI semantic targets need locator knowledge, such as top sites, omnibox icons, settings sections, and tab center controls.
- URL assertions need platform-aware normalization because Appium page source and address bar text may expose partial or redirected URLs.

## Recommended Next Work

1. Promote the temporary Android runner concept into a repository-owned Codex/Appium runner adapter.
2. Add accessibility tree capture before each unresolved action or assertion.
3. Implement semantic target resolution over `resource-id`, text, content description, class, hierarchy, and relation hints.
4. Add repair classification for missing element, stale page, wrong state, missing precondition, unsupported visual assertion, and conversion gap.
5. Keep case YAML stable during runner repair; do not auto-edit converted cases from runtime failures without review.

