---
name: architect
description: 'Design modular and loosely coupled architecture. Use when creating system architecture, designing components, defining interfaces, establishing separation of concerns, and ensuring scalability and maintainability.'
argument-hint: 'Describe the system or component you need to design, scope, and constraints'
user-invocable: true
---

# Architect Skill

## When to Use

- Designing system architecture and component structure
- Defining module boundaries and interfaces
- Planning separation of concerns
- Establishing patterns for loose coupling
- Reviewing architectural decisions
- Designing data flow and integration points
- Planning for scalability and maintainability

## Core Principles

1. **Modularity** – Components have single, well-defined responsibilities
2. **Loose Coupling** – Modules depend on abstractions, not concrete implementations
3. **High Cohesion** – Related functionality grouped logically
4. **Testability** – Modules designed to be independently testable
5. **Extensibility** – Easy to add features without modifying existing code

## Procedure

### 1. Understand Requirements
- Gather functional and non-functional requirements
- Identify key use cases and user workflows
- Document constraints (performance, security, scale)

### 2. Define Module Boundaries
- Identify distinct responsibilities
- Group related functionality
- Use [component-design template](./assets/component-design-template.md)

### 3. Design Interfaces
- Define clear contracts between modules
- Use [interface-definition checklist](./references/interface-design-patterns.md)
- Plan dependency injection points

### 4. Plan Data Flow
- Map data movement between modules
- Document transformation points
- Identify message contracts

### 5. Review Against Principles
- Run [architectural validation checklist](./references/architecture-checklist.md)
- Identify coupling risks
- Verify single responsibility per module

### 6. Document Design
- Update [architecture document](./assets/architecture-template.md)
- Create visual diagrams
- Record rationale for key decisions

## Key Patterns

- **Dependency Injection** – Pass dependencies rather than creating them
- **Interface Segregation** – Clients depend on minimal interfaces
- **Strategy Pattern** – Encapsulate varying algorithms
- **Factory Pattern** – Centralize object creation
- **Adapter Pattern** – Bridge incompatible interfaces
- **Observer Pattern** – Decouple event producers from consumers

## References

See the following guides for detailed patterns and best practices:
- [Interface Design Patterns](./references/interface-design-patterns.md)
- [Architecture Checklist](./references/architecture-checklist.md)
- [Module Design Guidelines](./references/module-design.md)
- [Coupling and Cohesion Analysis](./references/coupling-analysis.md)

## Assets

Use these templates to document and communicate architectural decisions:
- [Architecture Template](./assets/architecture-template.md)
- [Component Design Template](./assets/component-design-template.md)
- [Dependency Matrix Template](./assets/dependency-matrix-template.md)

## Scripts

Run these tools to validate and analyze your architecture:
- [validate-architecture.py](./scripts/validate-architecture.py) – Check for circular dependencies and tight coupling
- [dependency-analysis.py](./scripts/dependency-analysis.py) – Generate dependency graphs
- [modularity-score.py](./scripts/modularity-score.py) – Measure cohesion and coupling metrics
