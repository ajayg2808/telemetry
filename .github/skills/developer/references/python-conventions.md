# Python Coding Standards

## Style Guide

We follow PEP 8 with these specific conventions:

### Naming Conventions

- **Modules/Files**: `lowercase_with_underscores.py`
- **Classes**: `PascalCase` (e.g., `UserService`, `DataValidator`)
- **Functions/Methods**: `lowercase_with_underscores()` (e.g., `get_user_by_id()`)
- **Constants**: `UPPERCASE_WITH_UNDERSCORES` (e.g., `MAX_RETRY_COUNT`)
- **Private Methods/Attributes**: prefix with `_` (e.g., `_internal_method()`)
- **Protected Methods/Attributes**: prefix with `_` as well
- **Variables**: `lowercase_with_underscores` (e.g., `user_count`, `max_retries`)

### Formatting

```python
# Line length: Max 100 characters (Ruff default)
# Indentation: 4 spaces (never tabs)
# Imports: Organized in order
#   1. Standard library
#   2. Third-party
#   3. Local imports
# Then: Blank line between each group

import sys
import os
from pathlib import Path

import pandas as pd
import numpy as np

from .models import User
from .validators import validate_email
```

### Documentation

```python
def calculate_average(values: list[float]) -> float:
    """
    Calculate the average of a list of numbers.
    
    Args:
        values: List of numeric values to average
        
    Returns:
        The arithmetic mean of the values
        
    Raises:
        ValueError: If values list is empty
        TypeError: If values contain non-numeric items
        
    Example:
        >>> calculate_average([1.0, 2.0, 3.0])
        2.0
    """
    if not values:
        raise ValueError("Cannot average empty list")
    return sum(values) / len(values)
```

### Type Hints

Always use type hints:

```python
# Good
def get_user(user_id: str) -> User | None:
    pass

def process_data(data: list[dict]) -> pd.DataFrame:
    pass

def cache_result(func: Callable, ttl: int = 3600) -> Callable:
    pass

# Bad
def get_user(user_id):  # No types
    pass
```

### Error Handling

```python
# Good: Specific exception handling
try:
    result = database.get_user(user_id)
except DatabaseConnectionError as e:
    logger.error(f"Failed to connect to database: {e}")
    raise
except ValueError as e:
    logger.warning(f"Invalid user ID: {e}")
    return None

# Bad: Too broad
try:
    result = database.get_user(user_id)
except Exception:  # Catches everything
    pass
```

## SOLID Principles

### Single Responsibility Principle (S)
Each class should have only one reason to change.

```python
# Good: Separated concerns
class UserRepository:
    def get_user(self, id: str) -> User: pass

class UserValidator:
    def validate_email(self, email: str) -> bool: pass

# Bad: Multiple responsibilities
class User:
    def save(self): pass  # Persistence
    def validate(self): pass  # Validation
    def send_email(self): pass  # Communication
```

### Open/Closed Principle (O)
Open for extension, closed for modification.

```python
# Good: Can extend without modifying
class ReportExporter:
    def export(self, format: str, data: any):
        exporter = self.get_exporter(format)  # Strategy pattern
        return exporter.export(data)

# Bad: Modify class to add format
class ReportExporter:
    def export_csv(self, data): pass
    def export_json(self, data): pass
    def export_pdf(self, data): pass  # Add for each format
```

### Liskov Substitution Principle (L)
Subclasses should be substitutable for parent classes.

```python
# Good: Dog is correctly a subclass of Animal
class Animal:
    def make_sound(self) -> str: pass

class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof"

# Bad: Rectangle violates Square contract
class Rectangle:
    def set_width(self, w): self.width = w
    def set_height(self, h): self.height = h

class Square(Rectangle):
    def set_width(self, w):
        self.width = w
        self.height = w  # Violates Rectangle behavior
```

### Interface Segregation Principle (I)
Clients should depend on narrow, focused interfaces.

```python
# Good: Focused interfaces
class IReadable:
    def read(self) -> any: pass

class IWritable:
    def write(self, data: any) -> None: pass

# Bad: Fat interface
class IDataAccess:
    def read(self): pass
    def write(self, data): pass
    def delete(self): pass
    def backup(self): pass
    def encrypt(self): pass
```

### Dependency Inversion Principle (D)
Depend on abstractions, not concrete implementations.

```python
# Good: Depends on interface
class UserService:
    def __init__(self, repository: IUserRepository):
        self.repository = repository

# Bad: Depends on concrete class
class UserService:
    def __init__(self):
        self.repository = MySQLUserRepository()
```

## Code Quality Practices

### Keep Functions Small
- Single responsibility
- Aim for <20 lines typically
- Max 3-4 parameters

### Avoid Code Duplication
- Extract common code to utilities
- Use composition over inheritance for reuse
- Create helper functions

### Minimize Complexity
- Keep cyclomatic complexity < 10
- Avoid deep nesting (max 2-3 levels)
- Use early returns to reduce nesting

### Use Meaningful Names
- Variable names should be clear
- Avoid single letters except in loops (for x in...)
- Method names should describe what they do

### Handle Errors Explicitly
- Don't silently fail
- Provide context in error messages
- Log appropriately (debug, info, warning, error)

### Make Code Testable
- Inject dependencies
- Avoid global state
- Keep functions pure when possible
- Separate side effects from logic
