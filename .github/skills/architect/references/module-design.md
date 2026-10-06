# Module Design Guidelines

## Module Characteristics

### Clear Responsibility
Each module should have ONE primary responsibility. Ask:
- What problem does this module solve?
- What would force this module to change?
- Could this be split into multiple focused modules?

### Cohesion
Related functionality should be grouped together:
- Functions that operate on the same data
- Functions that are called together
- Functions that implement related behaviors

### Complexity Limits
- Keep module complexity manageable (aim for < 200 lines per file)
- Avoid deeply nested dependencies
- Limit the number of exports (public items)

## Module Structure Template

```
module/
├── __init__.py           # Public interface
├── _core.py              # Core implementation
├── _models.py            # Data models/types
├── _validators.py        # Input validation
├── _exceptions.py        # Module-specific exceptions
└── _helpers.py           # Private utilities
```

## Public vs Private

### Public Interface
- Documented and stable
- Versioned if breaking changes may occur
- Used by other modules
- Include in `__init__.py` or similar

### Private Implementation
- Prefixed with `_` (Python convention)
- Can change between versions
- Only for internal use
- Not exported or documented

## Naming Conventions

- **Modules**: lowercase, descriptive (`user_service`, `data_validator`)
- **Classes**: PascalCase (`UserService`, `DataValidator`)
- **Functions**: snake_case (`get_user_by_id`, `validate_email`)
- **Constants**: UPPER_SNAKE_CASE (`MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT`)
- **Private**: prefix with `_` (`_internal_helper`)

## Dependency Management

### Import Patterns

**Good:**
```python
from user_repository import IUserRepository  # Depend on interface
from .models import User  # Import from same package
```

**Bad:**
```python
from user_service.user_repository import MySQLUserRepository  # Concrete class
import entire_module_with_side_effects  # Side effects on import
```

### Circular Dependencies
- Never have two modules import each other
- Use interfaces/abstractions to break cycles
- Consider moving shared code to a common module

### External Dependencies
- Document all external dependencies
- Use dependency injection or factories to manage them
- Consider wrapping external libraries in adapters

## Testing Module Design

Good module design facilitates testing:

```python
# Good: Dependencies injected
class UserService:
    def __init__(self, repository: IUserRepository):
        self.repository = repository
    
    def get_user(self, id: str) -> User:
        return self.repository.get(id)

# Easy to test with mock repository
class MockRepository:
    def get(self, id: str) -> User:
        return User(id=id, name="Test")
```

## Evolution Guidelines

### Adding New Functionality
- Does it fit in existing module? Yes → Add it
- Is it related to module responsibility? No → Create new module
- Would adding it make the module too large? → Consider splitting

### Breaking Changes
- Version the interface if public
- Provide deprecation warnings
- Support old interface alongside new for transition period

### Refactoring
- Small, incremental changes
- Keep tests passing throughout
- Separate refactoring commits from feature commits
