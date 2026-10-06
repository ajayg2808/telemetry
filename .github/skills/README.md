# Skills Overview

This directory contains specialized skills for different roles in the spacecraft telemetry demo development. Each skill provides focused guidance, templates, and tools for its specific area.

## Available Skills

### 1. **Architect** — Modular & Loosely Coupled Design
**Path**: `.github/skills/architect/`

Design systems with modularity and loose coupling as core principles.

**Use When:**
- Designing system architecture and component structure
- Defining module boundaries and interfaces
- Planning separation of concerns
- Establishing patterns for loose coupling

**Key Resources:**
- [Architecture Checklist](./architect/references/architecture-checklist.md) — Validate architectural decisions
- [Interface Design Patterns](./architect/references/interface-design-patterns.md) — Design effective interfaces
- [Module Design Guidelines](./architect/references/module-design.md) — Create focused, cohesive modules
- [Architecture Template](./architect/assets/architecture-template.md) — Document your design
- [Validate Architecture Script](./architect/scripts/validate-architecture.py) — Check for coupling issues

**Core Principles:**
- **Modularity** — Single-purpose components
- **Loose Coupling** — Depend on abstractions
- **High Cohesion** — Related code grouped together
- **Testability** — Independently testable modules
- **Extensibility** — Add features without modification

---

### 2. **Developer** — Code Implementation & Best Practices
**Path**: `.github/skills/developer/`

Implement code following SOLID principles and best practices.

**Use When:**
- Implementing new features and functionality
- Refactoring code for clarity and maintainability
- Establishing coding standards
- Applying design patterns
- Writing clean, idiomatic code

**Key Resources:**
- [Python Conventions](./developer/references/python-conventions.md) — Naming, style, SOLID principles
- [Design Patterns](./developer/references/design-patterns.md) — Common architectural patterns
- [Refactoring Checklist](./developer/references/refactoring-checklist.md) — Refactor safely
- [Complexity Analyzer Script](./developer/scripts/complexity-analyzer.py) — Identify complex functions

**Core Principles:**
- **SOLID Principles** — Single Responsibility, Open/Closed, Liskov, Interface Segregation, Dependency Inversion
- **DRY** — Don't Repeat Yourself
- **KISS** — Keep It Simple, Stupid
- **Clean Code** — Clear naming, readable structure
- **Testability** — Write code that's easy to test

**SOLID Quick Reference:**
```
S — Single Responsibility: One reason to change
O — Open/Closed: Open for extension, closed for modification
L — Liskov Substitution: Subclasses are substitutable
I — Interface Segregation: Clients depend on narrow interfaces
D — Dependency Inversion: Depend on abstractions, not implementations
```

---

### 3. **Tester** — Test Specification & Execution
**Path**: `.github/skills/tester/`

Create comprehensive test specifications and perform testing with quality metrics.

**Use When:**
- Creating test specifications and test plans
- Implementing unit, integration, and end-to-end tests
- Analyzing test coverage
- Identifying test gaps
- Generating test reports

**Key Resources:**
- [Testing Best Practices](./tester/references/testing-best-practices.md) — FIRST principles and patterns
- [Test Case Design](./tester/references/test-case-design.md) — AAA pattern, positive/negative cases
- [Test Specification Template](./tester/assets/test-specification-template.md) — Document your test plan
- [Test Report Template](./tester/assets/test-report-template.md) — Executive-level reporting
- [Test Runner Script](./tester/scripts/test-runner.py) — Execute tests with coverage
- [Gap Analysis Script](./tester/scripts/gap-analysis.py) — Identify untested functions

**Test Categories:**
- **Unit Tests** — Individual functions/methods (80-100% coverage goal)
- **Integration Tests** — Component interactions (70-80% coverage goal)
- **End-to-End Tests** — Complete workflows (60%+ coverage goal)
- **Performance Tests** — Load and response time
- **Error Scenario Tests** — Edge cases and failures

**F.I.R.S.T. Principles:**
- **Fast** — Tests run quickly
- **Independent** — No test order dependency
- **Repeatable** — Same result every run
- **Self-Checking** — Clear pass/fail
- **Timely** — Written early

---

### 4. **Reviewer** — Code Quality & Architecture Review
**Path**: `.github/skills/reviewer/`

Review code for quality, architecture compliance, and best practices after tests pass.

**Use When:**
- Reviewing pull requests and code changes
- Validating code against architectural standards
- Checking adherence to coding standards
- Verifying test coverage and quality
- Assessing performance and security

**Key Resources:**
- [Code Review Checklist](./reviewer/assets/code-review-checklist.md) — Comprehensive review framework
- [Architectural Principles](./reviewer/references/architectural-principles.md) — Architecture review guidance
- [Review Feedback Template](./reviewer/assets/review-feedback-template.md) — Constructive feedback format
- [Review Report Template](./reviewer/assets/review-report-template.md) — Document findings

**Review Dimensions:**
1. **Functionality** — Meets requirements, tests pass
2. **Code Quality** — Follows standards, readable, appropriate complexity
3. **Architecture** — Modular, loosely coupled, follows principles
4. **Testing** — Adequate coverage, meaningful tests
5. **Performance & Security** — No issues, best practices followed
6. **Documentation** — Clear, up-to-date

**Review Levels:**
- 🔴 **Critical** — Must fix (functionality/security broken)
- 🟠 **Major** — Strongly recommended (quality/design issues)
- 🟡 **Minor** — Consider (style, optimization)
- ⚫ **Informational** — FYI (patterns, suggestions)

---

## Skill Organization

Each skill follows a consistent structure:

```
.github/skills/<skill-name>/
├── SKILL.md                    # Main skill definition
├── references/                 # Detailed guides and patterns
│   ├── principle-1.md
│   ├── principle-2.md
│   └── ...
├── assets/                     # Templates and checklists
│   ├── template-1.md
│   ├── template-2.md
│   └── ...
└── scripts/                    # Automation tools
    ├── tool-1.py
    └── tool-2.py
```

## SDLC Phase Integration

These skills map to the standard development lifecycle:

```
┌─────────────────────────────────────────────────────────┐
│  PLANNING & REQUIREMENTS                                │
│  (Architect shapes direction)                           │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  DESIGN                                                 │
│  (Architect defines modular design)                     │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  IMPLEMENTATION                                         │
│  (Developer writes code following best practices)       │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  TESTING                                                │
│  (Tester creates specs and validates coverage)          │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  REVIEW                                                 │
│  (Reviewer assesses quality & architecture)             │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  RELEASE & MAINTENANCE                                  │
└─────────────────────────────────────────────────────────┘
```

## Quick Start

1. **For Architects:**
   ```bash
   /architect
   # or
   Open .github/skills/architect/SKILL.md
   ```

2. **For Developers:**
   ```bash
   /developer
   # or
   Open .github/skills/developer/SKILL.md
   ```

3. **For Testers:**
   ```bash
   /tester
   # or
   Open .github/skills/tester/SKILL.md
   ```

4. **For Reviewers:**
   ```bash
   /reviewer
   # or
   Open .github/skills/reviewer/SKILL.md
   ```

## Accessing Skills

### Slash Commands
Type `/` in Copilot Chat and select from available skills.

### Direct Access
Open the `.github/skills/<skill-name>/SKILL.md` file and use Copilot to discuss.

### Running Scripts
```bash
# Analyze architecture
python .github/skills/architect/scripts/validate-architecture.py

# Check code complexity
python .github/skills/developer/scripts/complexity-analyzer.py

# Run tests with coverage
python .github/skills/tester/scripts/test-runner.py

# Analyze test gaps
python .github/skills/tester/scripts/gap-analysis.py
```

## Skill Interaction

Skills complement each other in the development workflow:

- **Architect** defines structure → **Developer** implements following that structure
- **Developer** writes testable code → **Tester** creates comprehensive tests
- **Tester** validates quality → **Reviewer** confirms architecture and code quality
- **Reviewer** feedback → **Developer** improves based on findings

## Best Practices

1. **Use in Phase Order**: Follow SDLC phases (design before code, test before review)
2. **Reference Templates**: Use provided templates for consistency
3. **Run Scripts**: Automate analysis with provided tools
4. **Check References**: Detailed guides provide pattern examples
5. **Iterate**: Skills support continuous improvement

## Contributing

To add to or improve skills:

1. Follow existing structure
2. Update relevant `.md` files
3. Add/improve scripts
4. Test templates with real scenarios
5. Document patterns and examples

---

**Last Updated**: October 2026  
**Status**: Active for Telemetry Demo Development
