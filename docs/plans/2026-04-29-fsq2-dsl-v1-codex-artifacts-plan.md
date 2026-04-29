# FSQ DSL v1 Codex Artifacts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce Codex-marked production artifacts for the FSQ AI Agent Friendly DSL v1 specification and JSON Schema.

**Architecture:** The proposal remains the review source, while the new Codex artifacts become implementation-ready outputs. The Markdown spec defines authoring semantics, executor policy, Windows adapter behavior, and examples; the JSON Schema validates the normalized YAML model after the parser splits metadata and command documents.

**Tech Stack:** Markdown, YAML examples, JSON Schema draft 2020-12.

---

### Task 1: Create Codex DSL Specification

**Files:**
- Create: `docs/codex-fsq-ai-test-dsl-v1.md`
- Source: `docs/FSQ_AI_Test_DSL_v1_Proposal.md`

- [ ] **Step 1: Copy the reviewed proposal into a production spec structure**

Use the proposal content as the source of truth and remove review-only framing.

- [ ] **Step 2: Make parser contract explicit**

State that authoring YAML uses two documents separated by `---`, and validation runs against a normalized object with `config` and `commands`.

- [ ] **Step 3: Preserve agreed design decisions**

Include Maestro-like shape, camelCase actions, Appium 3 primitives, Windows pywinauto MCP adapter, target/locator relation model, executor locator resolution policy, and external policy files.

### Task 2: Create Codex JSON Schema

**Files:**
- Create: `docs/codex-fsq-ai-test-dsl-v1.schema.json`

- [ ] **Step 1: Define normalized root object**

The schema validates `{ "config": {}, "commands": [] }`, not raw multi-document YAML text.

- [ ] **Step 2: Define reusable `$defs`**

Include selector, locator wrapper, command variants, W3C action sources, execute method, assertions, conditions, and Windows app config.

- [ ] **Step 3: Enforce strict command shape**

Each command item should be either a bare command string or an object with exactly one command key.

### Task 3: Verify Artifacts

**Files:**
- Check: `docs/codex-fsq-ai-test-dsl-v1.md`
- Check: `docs/codex-fsq-ai-test-dsl-v1.schema.json`

- [ ] **Step 1: Validate JSON syntax**

Run: `python3 -m json.tool docs/codex-fsq-ai-test-dsl-v1.schema.json >/tmp/codex-fsq-schema.json`

Expected: exit code 0.

- [ ] **Step 2: Check Codex naming**

Run: `ls docs | rg 'codex-fsq-ai-test-dsl-v1'`

Expected: both Codex artifact files are listed.

- [ ] **Step 3: Check headings**

Run: `rg -n '^## ' docs/codex-fsq-ai-test-dsl-v1.md`

Expected: major sections for file shape, commands, selectors, executor policy, Windows adapter, schema model, and policy files.
