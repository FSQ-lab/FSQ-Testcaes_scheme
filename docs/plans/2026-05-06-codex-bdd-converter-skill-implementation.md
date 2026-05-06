# Codex BDD Converter Skill Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Update the Codex FSQ case converter skill so BDD/Behave cases are converted through a BDD Execution Model before YAML generation.

**Architecture:** Keep `SKILL.md` concise and move detailed BDD/Behave behavior into two Codex reference files. The converter workflow will parse Gherkin, resolve Behave steps, expand `context.execute_steps()`, normalize environment hooks, then generate FSQ DSL and conversion reports.

**Tech Stack:** Markdown skill files, FSQ DSL YAML schema, Behave/Gherkin source conventions, existing FSQ validator.

---

### Task 1: Add BDD Execution Model Reference

**Files:**
- Create: `skills/codex-fsq-case-converter/references/codex-bdd-execution-model.md`

**Steps:**
1. Document Gherkin effective scenario parsing for Feature, Rule, Background, Scenario, Scenario Outline, Examples, tags, DocString, and DataTable.
2. Document Behave global step registry resolution across `features/steps/**/*.py`.
3. Document recursive `context.execute_steps()` expansion with source evidence, recursion limits, unresolved cycles, and operation extraction.

### Task 2: Add Hook Normalization Reference

**Files:**
- Create: `skills/codex-fsq-case-converter/references/codex-behave-hook-normalization.md`

**Steps:**
1. Classify hooks into setup/teardown, runner lifecycle, and runtime evidence.
2. Define which hook logic becomes YAML setup/teardown and which remains in conversion report or runner policy.
3. Add Android `environment.py` handling and environment variable rules for `TEST_ACCOUNT_EMAIL`, `TEST_ACCOUNT_PASSWORD`, and `PACKAGE`.

### Task 3: Update Skill Entry Point

**Files:**
- Modify: `skills/codex-fsq-case-converter/SKILL.md`

**Steps:**
1. Require BDD/Behave conversion to build the BDD Execution Model before writing YAML.
2. Link the two new references and state when to read each one.
3. Update report requirements to include BDD Execution Model, Hook Normalization, Environment Requirements, and Step Expansion Evidence.

### Task 4: Connect Existing Conversion Rules

**Files:**
- Modify: `skills/codex-fsq-case-converter/references/codex-fsq-conversion-rules.md`

**Steps:**
1. Add a short prerequisite note that operation mapping starts after BDD model construction.
2. Keep existing operation mapping rules as the command-generation layer.

### Task 5: Validate And Sync Skill

**Files:**
- Source: `skills/codex-fsq-case-converter/**`
- Destination: `/Users/qunmi/.agents/skills/codex-fsq-case-converter/**`

**Steps:**
1. Validate existing converted cases with `python3 skills/codex-fsq-case-converter/scripts/validate_fsq_cases.py --schema docs/codex-fsq-ai-test-dsl-v1.schema.json --cases fsq-testcases`.
2. Sync the updated skill files to `/Users/qunmi/.agents/skills/codex-fsq-case-converter`.
3. Check `git status` and commit only the intended repo files.
