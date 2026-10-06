# Architecture Design Template

## Project/Feature Name
[Name of the system or feature being designed]

## Overview
[1-2 sentence summary of the system's purpose]

## Problem Statement
[What problem does this architecture solve?]

## Key Requirements
- [ ] [Requirement 1]
- [ ] [Requirement 2]
- [ ] [Requirement 3]

## High-Level Architecture

### Layered View
```
┌─────────────────────────────────────┐
│         Presentation Layer          │
├─────────────────────────────────────┤
│         Application Layer           │
├─────────────────────────────────────┤
│         Business Logic Layer        │
├─────────────────────────────────────┤
│         Data Access Layer           │
├─────────────────────────────────────┤
│         External Services           │
└─────────────────────────────────────┘
```

### Component Diagram
[Describe or insert diagram showing major components]

## Modules & Responsibilities

### Module 1: [Name]
**Responsibility:** [What does this module do?]

**Public Interface:**
- `method1()` - [Description]
- `method2()` - [Description]

**Dependencies:**
- [Dependency 1]
- [Dependency 2]

**Data Models:**
- [Model 1]
- [Model 2]

### Module 2: [Name]
[Repeat above structure]

## Data Flow

### [Use Case 1]: [Name]
```
Actor → Component A → Component B → Component C → Database
```

### [Use Case 2]: [Name]
[Describe data flow for this use case]

## Key Design Decisions

### Decision 1: [What decision?]
**Rationale:** [Why this approach?]
**Alternatives Considered:** [What other options were there?]
**Trade-offs:** [What are the downsides?]

### Decision 2: [What decision?]
[Repeat above structure]

## Separation of Concerns

| Concern | Responsibility | Module |
|---------|----------------|--------|
| User input | Validate and parse user requests | Presentation |
| Business logic | Apply business rules | Application |
| Data persistence | Store/retrieve data | Data Access |
| External integration | Call external services | Integration |

## Dependency Matrix

| Module A | Module B | Module C | Module D |
|----------|----------|----------|----------|
| | ✓ (Interface) | | ✗ (No dep) |
| | | ✓ (Injects) | |
| | | | |

Legend: ✓ = Depends on, ✗ = No dependency, (Note) = How/why

## Extensibility Points

- [Extension Point 1]: [How can this be extended?]
- [Extension Point 2]: [How can this be extended?]

## Known Constraints

- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

## Future Considerations

- [Potential enhancement 1]
- [Potential enhancement 2]
- [Potential evolution]

## Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| [Risk 1] | [High/Medium/Low] | [How to mitigate] |
| [Risk 2] | [High/Medium/Low] | [How to mitigate] |

## Approval & Sign-off

- **Architect:** [Name] - [Date]
- **Tech Lead:** [Name] - [Date]
- **Stakeholder:** [Name] - [Date]
