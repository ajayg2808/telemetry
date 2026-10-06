# Architecture Checklist

Use this checklist to validate architectural decisions and ensure adherence to modularity and loose coupling principles.

## Module Design

- [ ] Each module has a single, well-defined responsibility
- [ ] Module purpose is clearly documented
- [ ] Module has a clear public interface
- [ ] Internal implementation details are hidden
- [ ] Module size is appropriate (not too large, not too small)
- [ ] Related functionality is grouped together

## Dependencies & Coupling

- [ ] No circular dependencies between modules
- [ ] Modules depend on abstractions (interfaces), not concrete implementations
- [ ] External dependencies are injected, not created internally
- [ ] Coupling is minimized and explicit
- [ ] Dependency direction follows architectural layers
- [ ] No skipping of layers in the architecture

## Interfaces & Contracts

- [ ] Public interfaces are well-defined and documented
- [ ] Interfaces are stable and unlikely to change
- [ ] Clients depend on the minimal interface they need
- [ ] Data contracts are explicit and versioned
- [ ] Error contracts are clear and consistent

## Extensibility

- [ ] New features can be added without modifying existing modules
- [ ] Variation points are identified and designed appropriately
- [ ] Plugin/extension mechanisms are clear
- [ ] Configuration is separated from logic

## Testability

- [ ] Each module can be tested independently
- [ ] External dependencies can be mocked
- [ ] No hidden or implicit dependencies
- [ ] Test seams are present for critical paths

## Documentation

- [ ] Architecture diagram is current and clear
- [ ] Rationale for key decisions is documented
- [ ] Module responsibilities are documented
- [ ] Data flow is documented
- [ ] Integration points are documented

## Performance & Scalability

- [ ] Architecture supports expected scale
- [ ] No single points of contention
- [ ] Communication patterns are efficient
- [ ] Resource usage is reasonable

## Anti-patterns to Avoid

- [ ] God objects (modules doing too much)
- [ ] Tight coupling (modules tightly bound together)
- [ ] Leaky abstractions (implementation details exposed)
- [ ] Circular dependencies
- [ ] Hidden dependencies
- [ ] Rigid architectures (difficult to extend)
