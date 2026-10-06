# Spacecraft Telemetry Demo: Requirements Specification

Status: draft baseline for implementation. Version: 0.1. Date: 2026-10-06.

## 1. Purpose and Audience

Build a local, interactive dashboard that helps a developer or reviewer explore spacecraft telemetry and demonstrate data ingestion, validation, filtering, visualization, and testing. The demo is not an operational ground system and must never send spacecraft commands.

## 2. Baseline and Assumptions

- No actual dataset, source schema, mission, or flight limits have been supplied.
- Agreed starting stack: Python 3.11+, Streamlit, pandas, Plotly, pytest, and Ruff.
- Input is a local CSV or JSON file, or a deterministic synthetic sample.
- Users access the app locally in a desktop or mobile browser; internet access is not required during normal use after installation.
- One local user and one selected dataset per session are sufficient.
- Proposed limits: 10 MiB per uploaded file and 100,000 input records. Confirm these during design and measure them during testing.
- Mission units, validity flags, time systems, and thresholds must be confirmed against actual source metadata before interpreting real telemetry.

## 3. Scope

In scope: file ingestion, a synthetic sample, validation feedback, filters, time-series charts, descriptive statistics, a table, CSV export, optional demo threshold indicators, and reproducible local setup.

Out of scope: spacecraft commanding, real-time feeds, mission planning, authentication, multi-user collaboration, cloud deployment, databases, binary telemetry decoders, flight-qualified alarms, automated operational decisions, ML anomaly detection, and production reliability guarantees.

## 4. Proposed Data Contract

Canonical long-form representation: one measurement per record.

| Field | Type | Required | Rule |
| --- | --- | --- | --- |
| `timestamp` | ISO 8601 string | Yes | Explicit `Z` or numeric offset; normalize to UTC |
| `spacecraft_id` | String | Yes | Nonempty after trimming |
| `subsystem` | String | Yes | Nonempty after trimming, e.g. `power` |
| `parameter` | String | Yes | Nonempty after trimming, e.g. `battery_voltage` |
| `value` | Number | Yes | Finite numeric value; missing/invalid values flagged and excluded |
| `unit` | String | Yes | Nonempty; use `1` for dimensionless values |
| `quality` | String | No | Allowed: `good`, `suspect`, `bad`; absent means unknown |

CSV is UTF-8, comma-delimited, with a header. JSON is UTF-8 with a top-level array of record objects. Both use the same required fields. Reject non-object JSON records with a clear error. Additional fields are reported and ignored by the canonical model; do not silently interpret them.

Example synthetic CSV, not supplied mission data:

```csv
timestamp,spacecraft_id,subsystem,parameter,value,unit,quality
2026-01-01T00:00:00Z,DEMO-1,power,battery_voltage,28.1,V,good
2026-01-01T00:01:00Z,DEMO-1,power,battery_voltage,27.9,V,good
2026-01-01T00:00:00Z,DEMO-1,thermal,panel_temperature,18.5,degC,good
```

Validation policy:

- Reject the file for unreadable encoding, malformed structure, missing required columns, or exceeded limits. Never execute uploaded content.
- Quarantine invalid records with their source position and reason; show accepted/rejected counts and a capped diagnostic preview. No charts when zero valid records remain.
- Reject timezone-naive timestamps rather than guessing a timezone. Sort accepted records chronologically without mutating the source.
- Reject booleans, NaN, infinity, and values that cannot be parsed numerically. Do not impute or interpolate missing values.
- Treat `(spacecraft_id, subsystem, parameter, unit)` as a series identity. Keep different units separate; no implicit conversion.
- Remove exact canonical duplicates and report the count. Retain conflicting measurements at the same timestamp, flag them, and never silently average them.
- Preserve quality metadata. Unknown is not equivalent to good. Exclude `bad` records by default with an explicit opt-in filter; make suspect/unknown states visible.
- Show plot gaps across rejected or excluded measurements and intervals exceeding a configurable gap tolerance; do not imply continuous coverage. Baseline tolerance is five times the median positive interval per series; permit an override and document the rule. With fewer than two distinct timestamps, render points without inferred continuity.
- Wide-format or mission-specific inputs require a documented adapter or user-confirmed mapping. Raw files must not be overwritten.

## 5. Functional Requirements

| ID | Requirement | Acceptance check |
| --- | --- | --- |
| FR-01 | Load a supported local file or a deterministic bundled sample | Both canonical formats load; sample works without a user upload and is labeled synthetic |
| FR-02 | Validate before rendering | Missing columns, malformed JSON, naive timestamps, invalid values, and oversized input yield actionable feedback without a crash |
| FR-03 | Report data quality | Accepted, rejected, duplicate, conflicting, and quality counts are visible; all-invalid input has an empty-state message |
| FR-04 | Filter the accepted data | Spacecraft, subsystem, parameter, quality, and inclusive UTC time filters update charts, table, statistics, and export consistently |
| FR-05 | Plot telemetry over time | Axes show UTC time and unit; hover identifies series and value; multiple unit groups never share an unlabeled scale; gaps remain visible |
| FR-06 | Summarize selected data | Per-series count, min, max, mean, and latest value are correct; no-data selections show no invented zeros; latest timestamp ties show a conflict indicator |
| FR-07 | Inspect records | A sortable table shows the canonical fields and quality; displayed and exported counts are clear when the table is capped |
| FR-08 | Offer optional demo thresholds | Users can set finite lower/upper limits per series; lower must be less than upper; strict excursions are marked; equal-boundary values are not excursions; no defaults are presented as mission limits |
| FR-09 | Export selected records | Downloadable UTF-8 CSV contains all filtered canonical records in timestamp order, including quality when present; no export for an empty selection |
| FR-10 | Maintain clear state | Synthetic label and non-operational disclaimer remain visible; replacing a dataset resets incompatible filters and thresholds; validation failure does not present old data as newly loaded |

## 6. Nonfunctional Requirements

| ID | Requirement | Verification |
| --- | --- | --- |
| NFR-01 | Local-only processing; no app-initiated network upload, analytics, or external processing | Inspect code/dependencies/config; disable Streamlit usage statistics and remote assets; browser network check |
| NFR-02 | Keep ingestion and transformation logic independent of the UI | Pure-function unit tests do not require launching Streamlit |
| NFR-03 | Proposed target: load/validate 100,000 records within 5 seconds and update filters within 2 seconds | Measure on a named machine; record dataset size, method, versions, and timing; unmeasured is not passed |
| NFR-04 | Usable at desktop 1440x900 and mobile 390x844 | Smoke-check no overlapping controls or labels; table may scroll horizontally; state changes remain clear |
| NFR-05 | Accessible controls and status indicators | Labels, keyboard-operable filters, readable contrast, and textual indicators alongside color |
| NFR-06 | Bounded resource consumption | Enforce file-size and record limits before expensive chart work; bound chart points and diagnostic/table previews; disclose display sampling while preserving full filtered statistics/export |
| NFR-07 | Repeatable installation and testing | Dependency declarations, local run instructions, pytest and Ruff pass in the supported environment |
| NFR-08 | Safe handling of user data | No committed sensitive files or payload logging; escape untrusted text; neutralize CSV formula prefixes in text fields on export; do not change numeric measurements |

## 7. Proposed Architecture

Use a thin Streamlit entry point and a small telemetry package with separate ingestion/validation, filtering/statistics, and chart construction responsibilities. Use in-memory pandas data frames. Design exact paths before scaffolding; avoid services and elaborate abstractions.

Proposed future layout: `app.py`, `telemetry/`, `tests/`, `data/sample/`, and one dependency declaration strategy. These paths do not yet exist. Only deterministic synthetic data belongs in the sample directory.

## 8. Test and Acceptance Plan

- Unit fixtures: valid CSV/JSON, wrong schema, malformed encoding/JSON, empty input, all-invalid input, mixed timezone offsets, naive timestamps, out-of-order rows, nonfinite values, booleans, duplicates, timestamp conflicts, unit mismatch, and quality states.
- Transformation tests: inclusive filter boundaries, empty results, statistics with one point, latest timestamp conflicts, strict threshold comparisons, unit separation, and gap segmentation.
- Integration tests: ingestion through filtered export, dataset replacement, bad-quality defaults, full export under display sampling, formula-safe text export, and file/record-limit enforcement.
- UI smoke checks: sample loading, file upload, validation feedback, filter reset, empty states, chart labels/gaps, download, and both target viewports. Use Streamlit testing support where suitable and browser checks for rendering/download behavior.
- Record each FR/NFR as passed, failed, blocked, not run, or explicitly deferred with reason. Only executed checks may be marked passed.

## 9. Milestones and Exit Gates

1. Planning and requirements: scope, assumptions, acceptance IDs, and small backlog established.
2. Data and design: actual-source mapping or explicit synthetic fallback documented; architecture and UI states agreed.
3. Implementation: sample-to-chart-to-export vertical slice works, followed by validation and quality handling.
4. Verification and review: automated checks, browser smoke checks, requirement traceability, and unresolved findings recorded.
5. Local release: fresh-environment setup verified, demonstration steps documented, limitations stated, no external deployment.
6. Maintenance: reproduce issues, add focused regression tests, fix within demo scope, update affected documentation.

## 10. Open Questions

- What are the actual file format, columns, units, time system, sampling cadence, and quality flags?
- Does source data use spacecraft clock counts or another non-UTC time system that needs a supplied conversion?
- Are there trusted thresholds to show, or should all thresholds remain user-entered demo settings?
- Are the proposed size/performance targets sufficient for the eventual dataset?

Proceed with the explicitly labeled synthetic fallback when these inputs are unavailable. Do not claim compatibility with unseen data or correctness for flight operations.