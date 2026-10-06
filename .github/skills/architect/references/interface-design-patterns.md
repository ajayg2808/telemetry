# Interface Design Patterns

## Design Principles

### 1. Interface Segregation Principle
- Clients should depend on interfaces specific to their needs
- Avoid "fat" interfaces with methods clients don't use
- Create multiple focused interfaces instead of one monolithic interface

Example:
```
BAD: IDataAccess (with Read, Write, Delete, Backup, Encrypt, Log)
GOOD: IReadable, IWritable, IDeletable
```

### 2. Dependency Inversion
- Depend on abstractions (interfaces), not concrete implementations
- High-level modules shouldn't depend on low-level modules
- Both should depend on abstractions

Example:
```
BAD: 
UserService depends on MySQLUserRepository

GOOD:
UserService depends on IUserRepository (interface)
MySQLUserRepository implements IUserRepository
```

### 3. Contract-Based Design
- Interfaces define explicit contracts
- Contracts include behavior, input requirements, and output guarantees
- Document pre-conditions and post-conditions
- Specify exception behavior

## Common Interface Patterns

### Repository Pattern
```python
class IRepository:
    def create(self, entity) -> Entity
    def read(self, id) -> Entity
    def update(self, id, entity) -> bool
    def delete(self, id) -> bool
    def list(self, filter) -> List[Entity]
```

### Factory Pattern
```python
class IFactory:
    def create(self, type: str, params: Dict) -> Product
```

### Service Pattern
```python
class IUserService:
    def get_user(self, id: str) -> User
    def create_user(self, name: str, email: str) -> User
    def update_user(self, id: str, changes: Dict) -> User
```

### Observer/Listener Pattern
```python
class IEventListener:
    def on_event(self, event: Event) -> None

class IEventPublisher:
    def subscribe(self, listener: IEventListener) -> None
    def publish(self, event: Event) -> None
```

## Interface Design Checklist

- [ ] Interface has a single, clear purpose
- [ ] Method names clearly describe what they do
- [ ] No implementation details leak into the interface
- [ ] Interface is stable and versioned
- [ ] Dependencies are inverted (depend on interface, not implementation)
- [ ] Error conditions are documented
- [ ] Lifecycle and ownership are clear
- [ ] Thread-safety requirements are documented if applicable

## Design Patterns for Loose Coupling

### Dependency Injection
Pass dependencies through constructor or setter, rather than creating them internally.

### Adapter Pattern
Bridge incompatible interfaces by creating an adapter class.

### Strategy Pattern
Encapsulate algorithms in separate classes implementing a common interface.

### Template Method
Define algorithm skeleton in base class, let subclasses override steps.

### Bridge Pattern
Decouple abstraction from implementation so they can vary independently.

### Facade Pattern
Provide simplified interface to complex subsystem, decoupling clients from components.
