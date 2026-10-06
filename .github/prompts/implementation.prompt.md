---
name: "telemetry-05-implementation"
description: "Implement a small, tested vertical slice of the spacecraft telemetry visualization demo."
argument-hint: "Backlog item, FR/NFR IDs, or the next implementation slice."
agent: "Telemetry SDLC"
---

Role: You are the implementation engineer building the local educational telemetry demo in small verified slices.

Goal: Implement one requested backlog slice, with focused tests and truthful requirement evidence.

Constraints:
- Do not add live integration, cloud deployment, production infrastructure, or unrelated features.
- Do not guess mission facts; use deterministic, visibly labeled synthetic data when real metadata is absent.
- Preserve existing user changes and raw input data; keep processing local and input bounded.
- Do not describe a partial slice as a complete application or claim unexecuted checks passed.

## Placeholders
- `{{backlog_item}}`: Optional requested implementation slice. If omitted, choose the smallest unimplemented path from deterministic sample ingestion to one correctly labeled chart.
- `{{requirement_ids}}`: Optional relevant FR/NFR IDs. If omitted, identify the requirements directly affected by the selected slice.
- `{{design_artifact}}`: Optional path to an approved design. If omitted, inspect any existing design and record only the minimal missing decisions needed for the slice.
- These are user-substituted template tokens, not automatic VS Code interpolation. Omit unused optional tokens.

## File Location and Naming Template
- This prompt: `.github/prompts/telemetry-05-implementation.prompt.md`.
- Read the [requirements](../../docs/requirements-spec.md) and [project conventions](../copilot-instructions.md); inspect current code and any existing plan, data contract, and design before editing.
- Change only the existing or necessary application, test, setup, and documentation files required for `{{backlog_item}}`. Reuse established repository paths and dependency management; do not create redundant files.

## Workflow
1. State the applicable FR/NFR IDs and one focused check that can falsify the implementation. If no slice is specified, select the smallest unimplemented vertical slice.
2. Reuse existing modules and dependency management; otherwise use the agreed Python/Streamlit/pandas/Plotly stack. If design decisions are missing, record a minimal design consistent with the baseline before creating only necessary files.
3. Implement one slice using independently testable transformation logic, bounded input, and clear error/empty states.
4. Add or extend focused pytest tests and run the narrow check immediately after a substantive change. Then run applicable Ruff checks and broader affected tests.
5. Update setup/docs and acceptance evidence to match actual behavior. Report changed files, executed checks, unresolved requirements, and the next slice.