---
name: tester
description: 'Create test specifications and perform comprehensive testing. Use when writing test specs, executing tests, analyzing test coverage, identifying test gaps, and generating test reports.'
argument-hint: 'Describe what to test, coverage goals, test environment, and acceptance criteria'
user-invocable: true
---

# Tester Skill

## When to Use

- Creating test specifications and test plans
- Implementing unit, integration, and end-to-end tests
- Performing manual and automated testing
- Analyzing test coverage and identifying gaps
- Writing test reports and findings
- Validating acceptance criteria
- Testing edge cases and error scenarios

## Core Principles

1. **Test-Driven Development** – Write tests before or alongside code
2. **Comprehensive Coverage** – Cover happy paths, edge cases, and error scenarios
3. **Automation** – Automate repeatable tests
4. **Isolation** – Tests should be independent and deterministic
5. **Clarity** – Test names should describe what is being tested
6. **Traceability** – Link tests to requirements

## Procedure

### 1. Analyze Requirements
- Review feature specifications and acceptance criteria
- Identify test scenarios and edge cases
- Check [test-planning guide](./references/test-planning.md)
- Use [requirement-traceability template](./assets/requirement-traceability.md)

### 2. Create Test Specification
- Document test objectives
- List test cases with inputs and expected outputs
- Use [test-spec template](./assets/test-specification-template.md)
- Identify success and failure criteria

### 3. Design Test Cases
- Cover normal operations
- Test boundary conditions
- Test error scenarios
- Use [test-case-design guide](./references/test-case-design.md)
- Apply [test-patterns](./references/test-patterns.md)

### 4. Implement Tests
- Write unit tests for individual components
- Write integration tests for component interactions
- Write end-to-end tests for workflows
- Use language-specific [test-frameworks guide](./references/test-frameworks.md)
- Reference [testing-best-practices](./references/testing-best-practices.md)

### 5. Execute Tests
- Run full test suite
- Run [coverage-analysis.py](./scripts/coverage-analysis.py) to measure coverage
- Execute [test-runner.py](./scripts/test-runner.py) to generate reports
- Document test results

### 6. Identify Test Gaps
- Analyze uncovered code paths
- Run [gap-analysis.py](./scripts/gap-analysis.py) to identify missing tests
- Document gaps and prioritize
- Add tests for critical gaps

### 7. Generate Test Report
- Use [test-report template](./assets/test-report-template.md)
- Document coverage metrics
- Report test results and findings
- Identify remaining risks
- Run [report-generator.py](./scripts/report-generator.py)

## Test Types

### Unit Tests
- Test individual functions/methods
- Fast and isolated
- Mock external dependencies
- Aim for 80%+ coverage

### Integration Tests
- Test multiple components together
- Verify contracts between modules
- Use test fixtures and databases
- Slower than unit tests

### End-to-End Tests
- Test complete workflows
- Use actual system components
- Verify user scenarios
- Most realistic but slowest

### Performance Tests
- Verify performance criteria
- Identify bottlenecks
- Test under load

## Test Coverage

Measure coverage with [coverage-analysis.py](./scripts/coverage-analysis.py):
- Line coverage – percentage of code executed
- Branch coverage – coverage of conditional paths
- Function coverage – coverage of functions/methods

Target coverage varies by component:
- Critical/core logic: 80-100%
- Integration points: 70-80%
- UI/presentation: 40-60% (harder to test)

## Gap Analysis

Use [gap-analysis.py](./scripts/gap-analysis.py) to identify:
- Untested code paths
- Missing edge case tests
- Untested error scenarios
- Integration gaps
- Performance gaps

## References

Detailed guides for testing practices:
- [Test Planning Guide](./references/test-planning.md)
- [Test Case Design](./references/test-case-design.md)
- [Test Patterns](./references/test-patterns.md)
- [Testing Best Practices](./references/testing-best-practices.md)
- [Test Frameworks](./references/test-frameworks.md)

## Assets

Templates and tools for test creation and reporting:
- [Test Specification Template](./assets/test-specification-template.md)
- [Test Case Template](./assets/test-case-template.md)
- [Test Report Template](./assets/test-report-template.md)
- [Requirement Traceability Matrix](./assets/requirement-traceability.md)

## Scripts

Run these tools to execute, analyze, and report on tests:
- [test-runner.py](./scripts/test-runner.py) – Execute test suite and generate results
- [coverage-analysis.py](./scripts/coverage-analysis.py) – Analyze test coverage
- [gap-analysis.py](./scripts/gap-analysis.py) – Identify gaps in test coverage
- [report-generator.py](./scripts/report-generator.py) – Generate consolidated test reports
