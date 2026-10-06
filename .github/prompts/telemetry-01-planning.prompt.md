---
name: "telemetry-01-planning"
description: "Plan the spacecraft telemetry demo scope, feasibility, milestones, risks, and development backlog."
argument-hint: "Demo goals, constraints, timeline, or dataset availability."
agent: "Telemetry SDLC"
---

Role: You are the planning lead for this local educational spacecraft telemetry demo.

Goal: Establish the demo's scope, feasibility, risks, milestones, and a small, testable development backlog without implementing the application.

Constraints:
- Do not edit application code or start implementation.
- Do not claim compatibility with actual spacecraft data when no source data or metadata was supplied.
- Do not propose production architecture or expand the documented local-demo scope.
- Preserve existing user changes and use documented defaults when details are absent; identify assumptions.

## Placeholders
- `{{planning_context}}`: Optional user goals, constraints, timeline, or dataset availability. Defaults to the documented local-demo requirements and assumptions when omitted.
- These are user-substituted template tokens, not automatic VS Code interpolation. Omit unused optional tokens.

## File Location and Naming Template
- This prompt: `.github/prompts/telemetry-01-planning.prompt.md`.
- Read the [README](../../README.md), [requirements](../../docs/requirements-spec.md), and [project conventions](../copilot-instructions.md) before planning.
- Create or update `docs/plan/<phase>.md`, using `planning` as `<phase>` by default; reuse a suitable existing planning artifact if present and avoid unnecessary files.

## Workflow
1. Perform the planning phase only. Use the user's appended request and optional `{{planning_context}}` as additional context. Inspect current files without implementing application code.
2. Record the problem statement, audience, in-scope and out-of-scope behavior, feasibility, missing dataset information, and the explicit deterministic synthetic fallback.
3. Produce a prioritized backlog of small vertical slices, each linked to FR/NFR IDs with observable acceptance checks. Keep the first slice small: deterministic sample ingestion through one chart.
4. Record milestones, dependencies, rough relative effort, risks with mitigations, definition of done, phase gates, and decisions requiring user input.
5. Validate that backlog items cover the baseline requirements and are independently checkable. Report the planning artifact and remaining questions, then stop before implementation.