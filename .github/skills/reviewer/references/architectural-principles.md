# Architectural Principles for Review

## Core Review Focus Areas for Architecture

### 1. Modularity
**Definition**: System can be decomposed into independent, replaceable modules

**Review Questions**:
- Can each module be understood independently?
- Can modules be developed and tested in isolation?
- Are module responsibilities clearly defined?
- Can a module be replaced without affecting others?

**What to Look For**:
- ✓ Clear module boundaries
- ✓ Minimal inter-module dependencies
- ✗ Circular dependencies
- ✗ Tight coupling between modules
- ✗ Hidden dependencies

### 2. Loose Coupling
**Definition**: Modules depend on abstractions, not concrete implementations

**Review Questions**:
- Are dependencies injected rather than created internally?
- Do modules depend on interfaces or concrete classes?
- Can dependencies be easily replaced/mocked?
- Are external dependencies minimized?

**What to Look For**:
- ✓ Dependency injection used
- ✓ Interface-based contracts
- ✓ Adapter patterns for external services
- ✗ Direct instantiation of dependencies
- ✗ Hard-coded external service references
- ✗ Multiple modules importing from same implementation

### 3. High Cohesion
**Definition**: Related functionality grouped together; unrelated functionality separated

**Review Questions**:
- Do all items in a module share a common purpose?
- Would splitting this module make it more focused?
- Are related operations grouped together?
- Is there a logical grouping of methods/functions?

**What to Look For**:
- ✓ Methods in a class work on same data
- ✓ Related functions in same module
- ✓ Clear purpose for each module
- ✗ Unrelated functionality mixed together
- ✗ God objects with many responsibilities
- ✗ Utility dumps mixing unrelated helpers

### 4. Extensibility
**Definition**: Easy to add new features without modifying existing code

**Review Questions**:
- Can new functionality be added in a new module/class?
- Are extension points clearly identified?
- Would new features require changing existing modules?
- Is configuration separate from logic?

**What to Look For**:
- ✓ Plugin/extension points designed
- ✓ Abstract base classes for extension
- ✓ Configuration externalized
- ✗ Hard-coded behaviors
- ✗ Rigid class hierarchies
- ✗ Switch statements enumerating all types

### 5. Dependency Direction
**Definition**: Dependencies flow in one direction through layers; no back-dependencies

**Review Questions**:
- Do high-level modules depend on low-level modules?
- Do circular dependencies exist?
- Is the dependency graph acyclic?
- Can you draw the architecture layers?

**Expected Dependency Flow**:
```
Presentation Layer
        ↓
Application Layer
        ↓
Business Logic Layer
        ↓
Data Access Layer
        ↓
External Services
```

**What to Look For**:
- ✓ Clear layer boundaries
- ✓ Dependencies only flow downward
- ✗ Back-dependencies to higher layers
- ✗ Circular imports
- ✗ Skipping layers

## Review Checklist

### Architecture Review

- [ ] **Modularity**: Clear separation of concerns
  - [ ] Each module has single responsibility
  - [ ] Module boundaries are clear
  - [ ] Size is appropriate (not God object, not fragmented)

- [ ] **Coupling**: Low external dependencies
  - [ ] Dependencies are injected
  - [ ] Interfaces used, not concrete classes
  - [ ] External dependencies minimized
  - [ ] No circular dependencies

- [ ] **Cohesion**: Related items grouped together
  - [ ] Methods work on related data
  - [ ] Functions logically grouped
  - [ ] Purpose of each module is clear

- [ ] **Extensibility**: Easy to add features
  - [ ] New features can be added without modifying existing
  - [ ] Extension points are clear
  - [ ] Configuration separated from logic

- [ ] **Testability**: Easy to test independently
  - [ ] Dependencies can be mocked
  - [ ] Modules have clear contracts
  - [ ] No hidden dependencies

### Pattern Usage

- [ ] **Appropriate patterns used**:
  - [ ] Design patterns applied correctly
  - [ ] Patterns solve actual problems (not over-engineered)
  - [ ] Implementation matches well-known pattern

- [ ] **Consistent patterns**:
  - [ ] Similar problems use similar solutions
  - [ ] Project conventions are followed
  - [ ] No conflicting patterns in same codebase

### Design Decisions

- [ ] **Decisions are justified**:
  - [ ] Rationale is understandable
  - [ ] Trade-offs are considered
  - [ ] Alternatives were evaluated

- [ ] **Decisions support requirements**:
  - [ ] Architecture meets performance needs
  - [ ] Architecture supports scalability
  - [ ] Architecture enables security requirements

## Red Flags 🚩

Watch for these architectural anti-patterns:

1. **God Object**: Single class with too many responsibilities
   - Often > 500 lines
   - Has multiple reasons to change
   - Hard to test and understand

2. **Feature Envy**: Methods more interested in other object's data
   - Indicates method in wrong class
   - Consider moving to class with the data

3. **Circular Dependencies**: Module A depends on B, B depends on A
   - Prevents independent testing
   - Causes hard-to-trace bugs
   - Break with interfaces/abstractions

4. **Leaky Abstraction**: Implementation details visible through interface
   - Clients depend on internal details
   - Changes to implementation break clients
   - Fix: Hide implementation behind abstraction

5. **Tight Coupling**: Modules directly depend on concrete classes
   - Hard to test with mocks
   - Hard to replace implementations
   - Difficult to extend

6. **Divergent Change**: Multiple reasons to change a single module
   - Violates Single Responsibility Principle
   - Consider splitting into focused modules

7. **Rigid Hierarchy**: Deep, inflexible class inheritance
   - Hard to extend
   - Base classes change frequently
   - Favor composition over inheritance

## Architectural Patterns to Support

### Layered Architecture
```
UI Layer (presentation)
Business Logic Layer
Persistence Layer
```

### Repository Pattern
- Abstracts data access
- Enables switching data sources
- Facilitates testing with mock repositories

### Dependency Injection
- Dependencies passed in, not created internally
- Enables testing and flexibility
- Supports configuration-based behavior

### Strategy Pattern
- Encapsulates related algorithms
- Enables runtime algorithm selection
- Supports extension without modification

### Observer Pattern
- Decouples event publishers from subscribers
- Enables loose coupling
- Supports pub/sub messaging

## Questions to Ask During Review

1. **Responsibility**: What is this module/class responsible for? Could it be expressed in one sentence?

2. **Dependencies**: What does this depend on? Can those dependencies be mocked for testing?

3. **Alternatives**: Would the code be more maintainable with [different approach]?

4. **Future**: How would adding [new feature] affect this design? Would it require changing existing code?

5. **Reusability**: Could this logic be reused in other parts of the system?

6. **Clarity**: Can a new team member understand how this module fits into the system?
