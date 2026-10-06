# Spacecraft Telemetry Demo

A planned local dashboard for exploring spacecraft telemetry from CSV or JSON files. This repository currently contains the requirements and GitHub Copilot development workflow, not an implemented application.

This is an educational demonstration. It must not be used for flight operations, spacecraft control, safety decisions, or production monitoring. Threshold indicators are illustrative, not flight-qualified alarms.

## Proposed Demo

- Upload telemetry or open a clearly labeled synthetic sample.
- Validate records and display useful data-quality feedback.
- Filter by spacecraft, subsystem, parameter, and UTC time range.
- Plot time series with units, summary statistics, and missing-data gaps.
- Inspect a telemetry table and optional illustrative threshold excursions.
- Export filtered records to CSV.

No source dataset has been supplied. The proposed schema and limits in the [requirements specification](docs/requirements-spec.md) are assumptions to validate against the actual data.

## Technology Direction

Python 3.11+, Streamlit, pandas, Plotly, pytest, and Ruff. These are agreed starting choices, not installed dependencies. Prefer a local, file-based application without a database, authentication, cloud services, or live spacecraft integration.

## Repository Guide

| File or folder | Purpose |
| --- | --- |
| [docs/requirements-spec.md](docs/requirements-spec.md) | Scope, proposed data contract, functional requirements, and acceptance checks |
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | Shared project conventions for Copilot |
| [.github/agents/telemetry-sdlc.agent.md](.github/agents/telemetry-sdlc.agent.md) | Development agent spanning the complete demo lifecycle |
| [.github/prompts/](.github/prompts/) | Individually runnable SDLC prompt templates |

## Copilot Workflow

Open this workspace in a current VS Code version with GitHub Copilot Chat enabled. Select **Telemetry SDLC** from the agent picker. Start with:

```text
Plan the demo from the requirements specification. Identify assumptions and
produce a small, testable backlog. Do not implement the application yet.
```

For a complete development run, use:

```text
Implement the local spacecraft telemetry demo through the SDLC using the
requirements specification. Use synthetic data until real data is supplied.
Run the applicable checks, document the results, and stop before external deployment.
```

Run a prompt by typing its slash command in Chat, using **Chat: Run Prompt...**, or opening its file and selecting the run button. Append task-specific context, dataset paths, or requirement IDs to the request.

| Step | Prompt | Expected output |
| --- | --- | --- |
| 1. Planning | [telemetry-01-planning](.github/prompts/telemetry-01-planning.prompt.md) | Scope, risks, milestones, and backlog |
| 2. Requirements | [telemetry-02-requirements](.github/prompts/telemetry-02-requirements.prompt.md) | Refined specification and acceptance criteria |
| 3. Data analysis | [telemetry-03-data-analysis](.github/prompts/telemetry-03-data-analysis.prompt.md) | Source-to-canonical mapping and validation rules |
| 4. Design | [telemetry-04-design](.github/prompts/telemetry-04-design.prompt.md) | Architecture, UI states, and test boundaries |
| 5. Implementation | [telemetry-05-implementation](.github/prompts/telemetry-05-implementation.prompt.md) | A working, tested vertical slice |
| 6. Testing | [telemetry-06-testing](.github/prompts/telemetry-06-testing.prompt.md) | Automated tests and acceptance evidence |
| 7. Review | [telemetry-07-review](.github/prompts/telemetry-07-review.prompt.md) | Prioritized, evidence-based findings |
| 8. Release | [telemetry-08-release](.github/prompts/telemetry-08-release.prompt.md) | Reproducible local demo setup and release checklist |
| 9. Maintenance | [telemetry-09-maintenance](.github/prompts/telemetry-09-maintenance.prompt.md) | Reproduced issue, focused fix, and regression test |

Review and planning prompts do not authorize application code changes. Other prompts have explicit, phase-specific boundaries. Review phase outputs before starting the next step; ask the agent to pause after any phase when a manual checkpoint is needed.

## Data Direction

The proposed canonical format is one measurement per row: UTC timestamp, spacecraft ID, subsystem, parameter, numeric value, and unit. CSV has a header; JSON is an array of records. Wide-format data requires an explicit documented mapping rather than guessed column meanings.

Synthetic samples must be deterministic and visibly labeled. Do not upload confidential mission data or commit sensitive datasets. Files remain local; no external processing or telemetry transmission is part of this demo.

## Running the Application Later

The implementation phase should create dependency declarations, an entry point, and tests, then replace this section with verified setup commands. No runnable app exists yet.

Expected Windows PowerShell workflow after implementation, assuming the design selects the names below:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
```

These commands are a proposed future convention, not verified setup instructions. Use the actual dependency file and entry point created during implementation.

## Completion Criteria

The demo is complete when the requirements' acceptance checks have recorded results, setup works in a clean environment, no private data is committed, and known limitations are documented. Production hardening is out of scope.# telemetry
