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
- Creating visual architecture diagrams

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

### 5. Create Visual Diagrams
- Use Mermaid diagrams to illustrate architecture
- Refer to [Mermaid Diagrams Guide](./references/mermaid-diagrams.md) for syntax and best practices
- Copy-paste ready examples available in [diagram examples](./assets/mermaid-diagram-examples.md)
- Use [diagram generator script](./scripts/generate-architecture-diagrams.py) for automated diagram creation

### 6. Review Against Principles
- Run [architectural validation checklist](./references/architecture-checklist.md)
- Identify coupling risks
- Verify single responsibility per module

### 7. Document Design
- Update [architecture document](./assets/architecture-template.md)
- Include visual diagrams
- Record rationale for key decisions

## Diagram Types

### Class Diagrams
Visualize static structure and relationships between classes or modules:
- Show inheritance hierarchies
- Illustrate interfaces and implementations
- Display associations and dependencies
- Document multiplicity relationships

### Flowcharts
Illustrate processes and control flow:
- Data processing workflows
- Decision trees and branching logic
- System operation sequences
- Algorithm steps

### Sequence Diagrams
Show temporal interactions between components:
- Method call sequences
- Message passing between modules
- Timing and dependencies
- Protocol interactions

### Entity Relationship Diagrams (ERD)
Model data structures and relationships:
- Database schema design
- Data entity relationships
- Cardinality and constraints
- Data transformation pipelines

### State Diagrams
Model state transitions and behaviors:
- System state machines
- Component lifecycles
- Event-driven transitions
- Mode changes

See [Mermaid Diagrams Guide](./references/mermaid-diagrams.md) for comprehensive examples and syntax details.

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
- [Mermaid Diagrams Guide](./references/mermaid-diagrams.md)

## Assets

Use these templates to document and communicate architectural decisions:
- [Architecture Template](./assets/architecture-template.md)
- [Component Design Template](./assets/component-design-template.md)
- [Dependency Matrix Template](./assets/dependency-matrix-template.md)
- [Mermaid Diagram Examples](./assets/mermaid-diagram-examples.md)

## Scripts

Run these tools to validate and analyze your architecture:
- [validate-architecture.py](./scripts/validate-architecture.py) – Check for circular dependencies and tight coupling
- [dependency-analysis.py](./scripts/dependency-analysis.py) – Generate dependency graphs
- [modularity-score.py](./scripts/modularity-score.py) – Measure cohesion and coupling metrics
- [generate-architecture-diagrams.py](./scripts/generate-architecture-diagrams.py) – Generate Mermaid diagram syntax from architecture descriptions
