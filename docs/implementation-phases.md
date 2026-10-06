---
title: Implementation Phases
status: in-progress
updated: 2026-10-06
spec: requirements-spec.md
current_phase: 1
---

# Implementation Phases

This plan breaks the [requirements specification](requirements-spec.md) into sequential, testable increments. The requirements specification remains authoritative for scope, data rules, and acceptance criteria; this document provides implementation order and phase exit gates. Preserve the existing FR/NFR identifiers in tests and acceptance evidence.

## Progress Tracker

Status values: `yet to start`, `in progress`, `done`. Mark a phase `done` only when its exit gate is met and evidence is recorded.

| Phase | Name | Status | Evidence |
| --- | --- | --- | --- |
| 1 | Scope and Design | In progress | Requirements spec and phase plan drafted; design and backlog not yet reviewed |
| 2 | Ingestion and Validation | Yet to start | - |
| 3 | First Usable Dashboard | Yet to start | - |
| 4 | Filtering, Statistics, and Export | Yet to start | - |
| 5 | Time-Series Visualization | Yet to start | - |
| 6 | Optional Demo Thresholds | Yet to start | - |
| 7 | Verification and Local Release | Yet to start | - |

## Phase 1: Scope and Design

```yaml
phase: 1
status: in progress
depends_on: []
requirements: [Milestone 1, Milestone 2]
exit_gate_met: false
```

**Goal:** Resolve implementation choices without implying that unknown mission details are known.

- Confirm the synthetic fallback, canonical schema, proposed 10 MiB and 100,000-record limits, technology choices, and dependency-management approach.
- Define the ingestion, validation-failure, no-valid-data, empty-selection, and dataset-replacement states.
- Document UTC normalization, quality handling, duplicate/conflict behavior, series identity, and gap rules.
- Establish a small backlog and trace each item to the requirement IDs below.

**Requirements:** Milestone 1 and Milestone 2; assumptions and open questions in Sections 2 and 10.

**Exit gate:** Design and backlog are documented. Mission-specific metadata and thresholds remain explicitly unconfirmed; no compatibility with unseen data is claimed.

## Phase 2: Ingestion and Validation

```yaml
phase: 2
status: yet to start
depends_on: [1]
requirements: [FR-01, FR-02, FR-03, NFR-02, NFR-06]
exit_gate_met: false
```

**Goal:** Load the deterministic synthetic sample and supported local files into the canonical model, independently of Streamlit.

- Implement CSV and JSON ingestion, including UTF-8 and structural validation.
- Enforce required fields, explicit-offset timestamps normalized to UTC, finite numeric values, quality rules, and file/record limits.
- Quarantine invalid records with source position and reason; report extra fields, duplicates, conflicts, and quality counts.
- Sort accepted records chronologically without mutating the source and retain the information needed to show gaps across rejected records.

**Requirements:** FR-01 to FR-03; NFR-02; ingestion and input-limit portions of NFR-06.

**Exit gate:** Focused unit tests cover valid CSV/JSON, malformed structure or encoding, missing fields, naive timestamps, invalid/nonfinite/boolean values, mixed offsets, duplicates, conflicts, all-invalid input, and both limits. Failures return actionable errors without a crash.

## Phase 3: First Usable Dashboard

```yaml
phase: 3
status: yet to start
depends_on: [2]
requirements: [FR-01, FR-02, FR-03, FR-07, FR-10, NFR-01, NFR-04, NFR-05, NFR-06]
exit_gate_met: false
```

**Goal:** Make loading and inspection possible through a thin local Streamlit UI.

- Add sample selection and local file upload with clear validation feedback.
- Display canonical records and accepted/rejected diagnostics with bounded previews.
- Keep the synthetic-data label and non-operational disclaimer visible.
- Handle empty and all-invalid datasets, and ensure dataset replacement does not leave stale data or incompatible state.
- Disable Streamlit usage statistics and keep processing local.

**Requirements:** FR-01 to FR-03, FR-07, and FR-10; NFR-01 and NFR-04 to NFR-06 foundations.

**Exit gate:** UI tests or smoke checks verify sample loading, upload, validation failures, bounded displays, empty states, and replacement behavior. Old data is never shown as if a failed replacement had loaded successfully.

## Phase 4: Filtering, Statistics, and Export

```yaml
phase: 4
status: yet to start
depends_on: [3]
requirements: [FR-04, FR-06, FR-09, FR-10, NFR-08]
exit_gate_met: false
```

**Goal:** Make every downstream view consistent with the selected records.

- Add spacecraft, subsystem, parameter, quality, and inclusive UTC time filters; exclude `bad` quality by default with an explicit opt-in.
- Drive the table, descriptive statistics, and export from the same filtered dataset.
- Report per-series count, minimum, maximum, mean, and latest value; indicate ties at the latest timestamp and show empty states without invented zeros.
- Export all selected canonical records in timestamp order, including quality when present. Neutralize spreadsheet formula prefixes in exported text fields without changing numeric measurements.

**Requirements:** FR-04, FR-06, FR-09, and relevant FR-10 behavior; NFR-08 export handling.

**Exit gate:** Transformation and integration tests verify inclusive boundaries, empty selections, one-point statistics, latest-time conflicts, quality defaults, formula-safe text export, and complete export when the displayed table is capped.

## Phase 5: Time-Series Visualization

```yaml
phase: 5
status: yet to start
depends_on: [4]
requirements: [FR-05, NFR-06]
exit_gate_met: false
```

**Goal:** Show telemetry without hiding unit differences or implying unsupported continuity.

- Plot time against value with UTC labels, units, and hover details identifying the series and value.
- Keep different unit groups on clearly labeled scales; never implicitly convert or combine units.
- Preserve gaps across rejected or excluded measurements and split intervals above the configured gap tolerance.
- Implement the baseline tolerance of five times each series' median positive interval, an override, and point-only rendering when continuity cannot be inferred from fewer than two distinct timestamps.
- Bound chart points and disclose display sampling while retaining full filtered statistics and export.

**Requirements:** FR-05; chart-point and display-sampling portions of NFR-06.

**Exit gate:** Tests cover unit separation, rejected/excluded-data gaps, long-interval gaps, tolerance override, sparse series, and chart sampling. Browser checks confirm labels, gaps, and readable rendering.

## Phase 6: Optional Demo Thresholds

```yaml
phase: 6
status: yet to start
depends_on: [4]
requirements: [FR-08, FR-10]
exit_gate_met: false
```

**Goal:** Add user-entered illustrative limits without presenting them as mission limits.

- Allow optional finite lower and upper limits per series; require lower to be strictly less than upper.
- Mark only strict excursions; a value equal to either boundary is not an excursion.
- Provide no default mission limits and reset incompatible threshold settings when the dataset changes.

**Requirements:** FR-08 and threshold-related FR-10 behavior.

**Exit gate:** Tests cover invalid and finite limits, ordering, strict boundary comparisons, per-series behavior, and dataset replacement. UI text clearly identifies thresholds as user-entered demo settings.

## Phase 7: Verification and Local Release

```yaml
phase: 7
status: yet to start
depends_on: [5, 6]
requirements: [FR-01..FR-10, NFR-01..NFR-08]
exit_gate_met: false
```

**Goal:** Verify the complete demo and document evidence and remaining limitations.

- Run the full pytest and Ruff checks and record results against every FR/NFR as passed, failed, blocked, not run, or deferred with a reason.
- Smoke-check desktop 1440x900 and mobile 390x844 layouts, keyboard operation, labels, contrast, empty/error states, chart rendering, filters, and downloads.
- Inspect configuration and browser network behavior for local-only processing, disabled usage statistics, and absence of remote assets or uploads.
- Measure ingestion and filter-update performance for 100,000 records on a named machine; record dataset, method, versions, and timings. Do not mark unmeasured targets as passed.
- Verify setup from a fresh environment, safe handling of user data, and accurate local run instructions.

**Requirements:** FR-01, FR-02, FR-03, FR-04, FR-05, FR-06, FR-07, FR-08, FR-09, FR-10; NFR-01, NFR-02, NFR-03, NFR-04, NFR-05, NFR-06, NFR-07, NFR-08.

**Exit gate:** Acceptance evidence reflects only executed checks; setup and applicable automated checks pass; unresolved checks and limitations are documented. No external deployment is part of this phase.

## Working Rule

Complete one phase at a time: implement small vertical slices, run the focused check for each slice immediately, then update the acceptance evidence. Begin implementation only after Phase 1 is reviewed. A phase is complete only when its exit gate is met; later-phase work remains backlog, not implied functionality.
