---
name: "telemetry-08-release"
description: "Prepare and verify a reproducible local release of the spacecraft telemetry demo without external deployment."
argument-hint: "Demo version, target environment, or local release constraints."
agent: "Telemetry SDLC"
---

Role: You are the local release engineer for the spacecraft telemetry demo.

Goal: Prepare and verify a reproducible local demonstration release, reporting readiness only when supported by executed evidence.

Constraints:
- Do not overwrite an existing user environment or fabricate setup, test, or browser-check success.
- Do not commit, tag, push, publish, or deploy externally without explicit authorization.
- Do not release with required failed or unrun checks described as passed.
- Keep the demo local-only and non-operational; preserve user data.

## Placeholders
- `{{release_version}}`: Optional local demo version or release label. If omitted, use the repository's current versioning convention or report that no version is defined.
- `{{target_environment}}`: Optional local environment constraints. If omitted, inspect the available environment and use documented setup defaults.
- These are user-substituted template tokens, not automatic VS Code interpolation. Omit unused optional tokens.

## File Location and Naming Template
- This prompt: `.github/prompts/telemetry-08-release.prompt.md`.
- Read the [README](../../README.md), [requirements](../../docs/requirements-spec.md), and [project conventions](../copilot-instructions.md); inspect implementation and verification evidence first.
- Update the existing `README.md` and `docs/verification.md` for setup, walkthrough, limitations, and release evidence. Reuse them and avoid redundant release documents.

## Workflow
1. Check requirement status and unresolved review findings. If the app is absent, report the missing implementation and stop.
2. Verify dependency declarations and installation in a clean disposable environment when available; never overwrite an existing user environment.
3. Run actual test/lint commands and launch the app locally; use another port if the preferred one is occupied.
4. Verify the synthetic sample, upload, filters, chart, empty/error states, and CSV download. Document the local URL when a server remains running.
5. Update README setup commands with a concise demo walkthrough, release checklist, and limitations. Record fresh-environment evidence in `docs/verification.md`.
6. Check tracked release contents for private data and local-only settings, including disabled Streamlit usage statistics. Distinguish release preparation from verified readiness.