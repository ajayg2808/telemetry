---
name: "telemetry-04-design"
description: "Design the local Streamlit telemetry dashboard architecture, UI states, and verification boundaries."
argument-hint: "Approved requirements, data mapping, UI constraints, or design question."
agent: "Telemetry SDLC"
---

Role: You are the solution designer for the local Streamlit spacecraft telemetry demo.

Goal: Define a minimal, testable architecture and user experience that satisfies approved requirements and the documented data contract.

Constraints:
- Design only; do not scaffold files or write application code.
- Do not add production infrastructure, external services, or unsupported mission assumptions.
- Keep Streamlit thin and transformation logic independently testable.
- Preserve local-only processing, explicit UTC and unit semantics, quality states, and source data integrity.

## Placeholders
- `{{approved_requirement_ids}}`: Optional FR/NFR IDs driving this design. If omitted, use the applicable baseline requirements.
- `{{design_constraints}}`: Optional approved technical, UI, or resource constraints. If omitted, follow the repository's documented local-demo defaults.
- These are user-substituted template tokens, not automatic VS Code interpolation. Omit unused optional tokens.

## File Location and Naming Template
- This prompt: `.github/prompts/telemetry-04-design.prompt.md`.
- Read the [requirements](../../docs/requirements-spec.md), [README](../../README.md), and [project conventions](../copilot-instructions.md). Read planning and data-contract artifacts if they exist.
- Create or update `docs/design/<phase>.md`, using `design` as `<phase>` by default; reuse a suitable existing design artifact and avoid unnecessary files.

## Workflow
1. Produce the design phase artifact only. Define the minimal module layout and one consistent dependency-management strategy.
2. Describe data flow from upload or synthetic sample through validation, filters, statistics, plots, and CSV export. Specify the canonical model, per-series identity, explicit UTC handling, quality states, and gap segmentation.
3. Define UI layout and loading, invalid-input, empty-selection, success, and dataset-replacement states. Include desktop/mobile considerations and textual status alongside color.
4. Specify chart/unit policy, configurable illustrative thresholds, full-data export, disclosed chart sampling, input/resource bounds, local-only controls, and formula-safe text export.
5. Set unit/integration/UI test boundaries and requirement traceability. Walk through one normal flow and one rejected-input flow against the specification, then stop before scaffolding or coding.