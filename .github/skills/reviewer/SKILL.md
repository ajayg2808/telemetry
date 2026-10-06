---
name: reviewer
description: 'Review code quality, architecture, and best practices. Use when reviewing pull requests, validating code quality, checking architectural conformance, and providing code review feedback.'
argument-hint: 'Describe the code to review, acceptance criteria, architectural constraints, and review focus areas'
user-invocable: true
---

# Reviewer Skill

## When to Use

- Reviewing pull requests and code changes
- Validating code against architectural standards
- Checking adherence to coding standards
- Verifying test coverage and quality
- Assessing performance and security implications
- Providing constructive feedback
- Creating code review reports

## Core Principles

1. **Constructive** – Provide helpful, actionable feedback
2. **Objective** – Base reviews on standards and requirements
3. **Thorough** – Check all aspects: functionality, quality, testing, architecture
4. **Respectful** – Focus on code, not the developer
5. **Timely** – Provide feedback promptly
6. **Evidence-Based** – Reference standards and metrics

## Review Dimensions

### Functionality
- Does the code implement the feature as specified?
- Are acceptance criteria met?
- Are edge cases handled?
- Do tests pass?

### Code Quality
- Follows [coding-standards](./references/coding-standards.md)
- Clear naming and readability
- Appropriate complexity level
- Minimal duplication
- Proper error handling

### Architecture
- Adheres to [architectural-principles](./references/architectural-principles.md)
- Maintains modularity and loose coupling
- Respects module boundaries
- Uses appropriate design patterns
- No circular dependencies

### Testing
- Adequate test coverage
- Tests are meaningful and isolated
- Edge cases tested
- Error scenarios covered
- Check for [test-gaps](./references/test-gap-analysis.md)

### Performance & Security
- No obvious performance regressions
- Secure coding practices followed
- No hardcoded secrets
- Input validation present
- Dependencies are appropriate

## Procedure

### 1. Prepare for Review
- Understand the feature and requirements
- Review [code-review checklist](./assets/code-review-checklist.md)
- Gather context: architecture, standards, tests
- Check [review-focus-guide](./references/review-focus-guide.md)

### 2. Verify Acceptance Criteria
- Confirm feature is complete
- Check [acceptance-criteria template](./assets/acceptance-criteria-checklist.md)
- Review associated tests pass
- Validate against requirements

### 3. Review Code Quality
- Use [code-quality-checklist](./assets/code-quality-checklist.md)
- Check [coding-standards](./references/coding-standards.md) compliance
- Analyze complexity using [complexity-analyzer](./scripts/complexity-analyzer.py)
- Identify refactoring opportunities

### 4. Review Architecture & Design
- Verify architectural conformance
- Check [architecture-review-checklist](./assets/architecture-review-checklist.md)
- Use [dependency-analyzer](./scripts/dependency-analyzer.py)
- Ensure modularity and loose coupling

### 5. Review Testing
- Run [coverage-analyzer](./scripts/coverage-analyzer.py)
- Check test quality and coverage
- Use [test-gap-analyzer](./scripts/test-gap-analyzer.py)
- Verify edge cases and error scenarios tested

### 6. Check for Security & Performance
- Review [security-checklist](./assets/security-checklist.md)
- Look for performance implications
- Check dependency updates
- Verify no hardcoded values

### 7. Provide Feedback
- Use [review-feedback template](./assets/review-feedback-template.md)
- Categorize findings: critical, major, minor, informational
- Provide constructive suggestions
- Ask clarifying questions

### 8. Generate Review Report
- Document findings systematically
- Use [review-report template](./assets/review-report-template.md)
- Summarize decision: approved, approved with comments, request changes
- Run [report-generator](./scripts/report-generator.py)

## Review Levels

### Critical Issues
- Breaks functionality
- Security vulnerabilities
- Violates architectural principles
- Missing test coverage for critical paths
- **Action**: Request changes

### Major Issues
- Significant code quality problems
- Moderate architectural violations
- Suboptimal design choices
- Incomplete testing
- **Action**: Request changes or discuss

### Minor Issues
- Code style nitpicks
- Small refactoring suggestions
- Documentation improvements
- Edge case improvements
- **Action**: Consider for next iteration

### Informational
- Suggestions for consideration
- Pattern improvements
- Performance opportunities
- **Action**: Note for future

## Feedback Guidelines

Use [feedback-template](./assets/review-feedback-template.md):

**Instead of:**
> "This is bad code"

**Say:**
> "This function is complex (CC=12). Consider breaking it into smaller functions to improve testability and readability. See [complexity-guidelines](./references/complexity-guidelines.md)."

**Instead of:**
> "Why did you do this?"

**Say:**
> "I'm curious about this design choice. Did you consider [alternative approach]? It might provide better [benefit]."

## References

Detailed guides for comprehensive code reviews:
- [Code Review Checklist](./references/code-review-checklist.md)
- [Coding Standards](./references/coding-standards.md)
- [Architectural Principles](./references/architectural-principles.md)
- [Review Focus Guide](./references/review-focus-guide.md)
- [Complexity Guidelines](./references/complexity-guidelines.md)
- [Test Gap Analysis](./references/test-gap-analysis.md)
- [Security Checklist](./references/security-checklist.md)

## Assets

Templates and checklists for conducting thorough reviews:
- [Code Review Checklist](./assets/code-review-checklist.md)
- [Code Quality Checklist](./assets/code-quality-checklist.md)
- [Architecture Review Checklist](./assets/architecture-review-checklist.md)
- [Security Checklist](./assets/security-checklist.md)
- [Acceptance Criteria Checklist](./assets/acceptance-criteria-checklist.md)
- [Review Feedback Template](./assets/review-feedback-template.md)
- [Review Report Template](./assets/review-report-template.md)

## Scripts

Run these tools to analyze and report on code reviews:
- [complexity-analyzer.py](./scripts/complexity-analyzer.py) – Measure cyclomatic complexity
- [dependency-analyzer.py](./scripts/dependency-analyzer.py) – Analyze dependencies and coupling
- [coverage-analyzer.py](./scripts/coverage-analyzer.py) – Check test coverage
- [test-gap-analyzer.py](./scripts/test-gap-analyzer.py) – Identify test gaps
- [duplication-detector.py](./scripts/duplication-detector.py) – Find code duplication
- [report-generator.py](./scripts/report-generator.py) – Generate review reports
