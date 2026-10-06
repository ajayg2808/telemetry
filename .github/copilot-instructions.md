# Spacecraft Telemetry Demo Conventions

- Read [the README](../README.md) and [requirements](../docs/requirements-spec.md) before changing behavior. Requirements are the baseline; distinguish confirmed facts from assumptions.
- This is a local educational demo, never a flight-control or production monitoring system. Do not add commanding, cloud services, live feeds, authentication, or databases without an explicit scope change.
- Start with Python 3.11+, Streamlit, pandas, Plotly, pytest, and Ruff. Reuse the actual repository layout and dependency management once established.
- No real dataset has been provided at baseline. Inspect supplied metadata before mapping fields; otherwise use deterministic, visibly synthetic samples. Never invent mission units, time conversions, or flight limits.
- Normalize explicit-offset timestamps to UTC. Preserve units and quality. Do not silently average conflicts, interpolate missing values, or combine incompatible units.
- Keep ingestion and transformations testable independently of Streamlit. Enforce input limits and actionable validation errors.
- Keep all data processing local. Do not upload user files, add external assets/analytics, commit private datasets, or log raw payloads. Disable Streamlit usage statistics in the implemented app.
- Work in small vertical slices; add focused tests for changed behavior and run them immediately. Run broader applicable checks before release. Never claim an unexecuted check passed.
- Use labeled controls, textual status in addition to color, and responsive layouts. Keep the synthetic-data label and non-operational disclaimer visible.
- Preserve existing user changes. Do not commit, push, delete data, or deploy externally unless explicitly requested.
- Keep setup instructions and FR/NFR acceptance evidence aligned with actual code. Mark unavailable checks as blocked or not run with a reason.