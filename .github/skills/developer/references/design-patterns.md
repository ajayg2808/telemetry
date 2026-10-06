# Design Patterns Guide

## Architectural Design Patterns

### Repository Pattern
Abstracts data access logic, allowing business logic to remain independent of data source.

**When to use:**
- Need to switch between different data sources (SQL, NoSQL, file system)
- Want to test business logic without database
- Want consistent data access interface

**Structure:**
```python
class IUserRepository:
    def get_by_id(self, id: str) -> User: pass
    def save(self, user: User) -> str: pass
    def delete(self, id: str) -> bool: pass

class SqlUserRepository(IUserRepository):
    def get_by_id(self, id: str) -> User:
        # SQL implementation
        pass

class UserService:
    def __init__(self, repository: IUserRepository):
        self.repository = repository
    
    def get_user(self, id: str) -> User:
        return self.repository.get_by_id(id)
```

### Dependency Injection Pattern
Provide dependencies to objects rather than having objects create them.

**Benefits:**
- Easier to test (inject mocks)
- Reduces coupling
- Improves flexibility

**Types:**
1. **Constructor Injection** (preferred):
```python
class UserService:
    def __init__(self, repository: IUserRepository):
        self.repository = repository
```

2. **Setter Injection**:
```python
class UserService:
    def set_repository(self, repository: IUserRepository):
        self.repository = repository
```

3. **Interface/Method Injection**:
```python
def process_user(user_id: str, repository: IUserRepository) -> User:
    return repository.get_by_id(user_id)
```

### Factory Pattern
Create objects without specifying exact classes.

**Use when:**
- Object creation is complex
- Need to create different types based on configuration
- Want to defer object creation

**Example:**
```python
class DataSourceFactory:
    @staticmethod
    def create(type: str) -> IDataSource:
        if type == "sql":
            return SqlDataSource()
        elif type == "mongodb":
            return MongoDataSource()
        else:
            raise ValueError(f"Unknown type: {type}")

# Usage
source = DataSourceFactory.create("sql")
```

### Observer Pattern
Notify multiple objects about state changes without tight coupling.

**Use when:**
- Multiple objects need to know about state changes
- Don't want direct coupling between objects
- Want loose coupling for event handling

**Example:**
```python
class IEventListener:
    def on_event(self, event: Event) -> None: pass

class EventPublisher:
    def __init__(self):
        self.listeners: List[IEventListener] = []
    
    def subscribe(self, listener: IEventListener):
        self.listeners.append(listener)
    
    def publish(self, event: Event):
        for listener in self.listeners:
            listener.on_event(event)

class Logger(IEventListener):
    def on_event(self, event: Event):
        print(f"Event: {event}")
```

### Strategy Pattern
Define interchangeable algorithms/strategies.

**Use when:**
- Multiple ways to solve a problem
- Want runtime selection of algorithm
- Want to avoid conditional logic

**Example:**
```python
class ISortStrategy:
    def sort(self, data: List) -> List: pass

class QuickSort(ISortStrategy):
    def sort(self, data: List) -> List:
        # Implementation
        pass

class Sorter:
    def __init__(self, strategy: ISortStrategy):
        self.strategy = strategy
    
    def sort(self, data: List) -> List:
        return self.strategy.sort(data)

# Usage
sorter = Sorter(QuickSort())
result = sorter.sort([3, 1, 2])
```

### Adapter Pattern
Convert interface of one class to another clients expect.

**Use when:**
- Need to use a class with incompatible interface
- Want to bridge different systems
- Need to wrap external libraries

**Example:**
```python
class LegacyPaymentSystem:
    def process_payment(self, amount_in_cents: int) -> bool:
        # Old interface
        pass

class IPaymentProcessor:
    def process(self, amount: float) -> bool: pass

class LegacyPaymentAdapter(IPaymentProcessor):
    def __init__(self, legacy_system: LegacyPaymentSystem):
        self.legacy = legacy_system
    
    def process(self, amount: float) -> bool:
        # Adapt interface
        amount_in_cents = int(amount * 100)
        return self.legacy.process_payment(amount_in_cents)

# Usage
processor = LegacyPaymentAdapter(legacy_system)
processor.process(19.99)
```

### Template Method Pattern
Define algorithm skeleton, let subclasses override steps.

**Use when:**
- Multiple similar algorithms with different implementations
- Want to avoid code duplication
- Want to enforce algorithm structure

**Example:**
```python
class IDataProcessor:
    def process(self, data):
        # Template method
        validated_data = self.validate(data)
        transformed_data = self.transform(validated_data)
        return self.persist(transformed_data)
    
    def validate(self, data): pass
    def transform(self, data): pass
    def persist(self, data): pass

class UserDataProcessor(IDataProcessor):
    def validate(self, data):
        # Validate user data
        return data
    
    def transform(self, data):
        # Transform for database
        return data
    
    def persist(self, data):
        # Save to database
        return True
```

## Code Quality Patterns

### Guard Clauses
Return early to reduce nesting and improve readability.

**Before:**
```python
def process_user(user):
    if user is not None:
        if user.is_active:
            if user.balance > 0:
                # Process
                return True
    return False
```

**After:**
```python
def process_user(user):
    if user is None:
        return False
    if not user.is_active:
        return False
    if user.balance <= 0:
        return False
    # Process
    return True
```

### Extract Method
Break large methods into smaller, focused ones.

**Before:**
```python
def calculate_invoice_total(items, tax_rate, discount):
    subtotal = sum(item.price * item.quantity for item in items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    if total > 1000:
        total -= total * discount
    return total
```

**After:**
```python
def calculate_invoice_total(items, tax_rate, discount):
    subtotal = calculate_subtotal(items)
    tax = calculate_tax(subtotal, tax_rate)
    total = subtotal + tax
    return apply_bulk_discount(total, discount)

def calculate_subtotal(items):
    return sum(item.price * item.quantity for item in items)

def calculate_tax(subtotal, rate):
    return subtotal * rate

def apply_bulk_discount(total, discount_rate):
    return total * (1 - discount_rate) if total > 1000 else total
```

### Extract Variable
Use variables to clarify complex expressions.

**Before:**
```python
if customer.age > 18 and customer.credit_score > 650 and customer.income > 30000:
    grant_credit_line()
```

**After:**
```python
is_adult = customer.age > 18
has_good_credit = customer.credit_score > 650
has_sufficient_income = customer.income > 30000

if is_adult and has_good_credit and has_sufficient_income:
    grant_credit_line()
```

## References

- [SOLID Principles](../references/coding-standards.md)
- [Code Quality Checklist](../references/coding-standards.md)
