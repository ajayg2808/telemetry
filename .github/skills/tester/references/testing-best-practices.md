# Testing Best Practices

## Test Characteristics (F.I.R.S.T.)

### Fast
- Tests should run quickly
- Avoid sleep/delays when possible
- Mock external dependencies
- Use in-memory databases for tests
- Aim for full suite to run in < 1 minute

### Independent
- No test should depend on another test's output
- Tests can run in any order
- No shared state between tests
- Clean up after yourself (teardown)

### Repeatable
- Same test should produce same result every time
- No flaky tests that fail randomly
- Don't depend on external services
- Use fixed seeds for random data

### Self-Checking
- Tests should have clear pass/fail criteria
- No manual verification needed
- Assertions are specific, not generic
- Error messages are helpful

### Timely
- Write tests before or alongside code
- Don't add tests after code is done (too tempting to skip)
- Tests guide design and reveal issues early

## Test Organization

### Directory Structure
```
project/
├── src/
│   ├── user_service.py
│   ├── user_repository.py
│   └── models/
│       └── user.py
└── tests/
    ├── unit/
    │   ├── test_user_service.py
    │   ├── test_user_repository.py
    │   └── models/
    │       └── test_user.py
    ├── integration/
    │   └── test_user_workflow.py
    └── conftest.py  # Shared fixtures
```

### Test File Naming
- Name: `test_*.py` or `*_test.py` (pytest convention)
- Match source file structure
- One test class per source module typically

### Test Method Naming
- Be descriptive: `test_should_return_user_when_id_valid()`
- Include scenario: `test_raises_error_when_user_not_found()`
- Show expected outcome: `test_increases_count_by_one()`

Good names:
- `test_should_return_user_when_id_exists()`
- `test_raises_value_error_when_email_invalid()`
- `test_returns_empty_list_when_no_results()`

Bad names:
- `test1()`, `test2()`
- `test_user()`
- `test_works()`

## Assertion Best Practices

### Use Specific Assertions

```python
# Good: Clear what failed
assert result == expected
assert user.name == "John"
assert len(users) == 5

# Bad: Vague
assert result
assert user
assert users
```

### Use Assertion Libraries

```python
# With pytest
assert user.age > 18, f"Expected age > 18, got {user.age}"

# Use clear comparison
assert user.status in ["active", "pending"]
assert user.email.endswith("@company.com")
```

### Test One Thing Per Test

```python
# Good: Single assertion (or single concept)
def test_creates_user_with_name():
    user = create_user("John")
    assert user.name == "John"

def test_creates_user_with_email():
    user = create_user(email="john@example.com")
    assert user.email == "john@example.com"

# Bad: Multiple concepts
def test_creates_user():
    user = create_user("John", "john@example.com")
    assert user.name == "John"
    assert user.email == "john@example.com"
    assert user.created_at is not None
    assert user.id is not None
```

## Test Patterns

### Arrange-Act-Assert (AAA)
```python
def test_should_calculate_total_price():
    # Arrange: Set up test data
    item1 = Item(price=10.0, quantity=2)
    item2 = Item(price=20.0, quantity=1)
    cart = Cart([item1, item2])
    
    # Act: Perform the action
    total = cart.calculate_total()
    
    # Assert: Verify results
    assert total == 40.0
```

### Given-When-Then
```python
def test_user_can_borrow_book_when_account_active():
    # Given: User has active account
    user = create_user_with_active_account()
    
    # When: User borrows book
    result = user.borrow_book(book)
    
    # Then: Book is added to user's borrowed items
    assert book in user.borrowed_items
    assert result is True
```

## Mocking & Stubbing

### Mock External Dependencies

```python
# Bad: Depends on real database
def test_get_user():
    user = UserService().get_user(123)
    assert user.name == "John"

# Good: Mock the repository
from unittest.mock import Mock

def test_get_user():
    mock_repo = Mock()
    mock_repo.get_by_id.return_value = User(id=123, name="John")
    
    service = UserService(mock_repo)
    user = service.get_user(123)
    
    assert user.name == "John"
    mock_repo.get_by_id.assert_called_once_with(123)
```

### When to Mock
- External APIs and services
- Databases and file systems
- Time-dependent operations
- Random number generation
- Network operations

### When NOT to Mock
- Core business logic
- Repository pattern (if testing service)
- Configuration loading
- In-memory data structures

## Test Data Management

### Use Factories & Fixtures

```python
# Good: Factory for test data
def user_factory(name="John", email="john@example.com", age=25):
    return User(name=name, email=email, age=age)

def test_adult_user():
    user = user_factory(age=30)
    assert user.is_adult()

# With pytest fixtures
@pytest.fixture
def sample_user():
    return User(name="John", email="john@example.com")

def test_with_fixture(sample_user):
    assert sample_user.name == "John"
```

### Use Realistic Data
- Use actual formats (email addresses, phone numbers)
- Use realistic lengths
- Don't use obviously fake data except when needed

## Common Anti-Patterns

### Test Interdependence
```python
# Bad: Tests depend on execution order
def test_1_create_user(self):
    self.user = User(name="John")

def test_2_get_user(self):
    result = get_user(self.user.id)  # Depends on test_1
```

### Overly Generic Assertions
```python
# Bad: Not checking specific behavior
def test_update_user():
    result = update_user(user)
    assert result  # What does True mean?

# Good: Specific verification
def test_update_user():
    updated_user = update_user(user)
    assert updated_user.email == "new@example.com"
```

### Testing Implementation, Not Behavior
```python
# Bad: Tests implementation details
def test_user_class():
    user = User()
    assert hasattr(user, '_name')  # Testing private attribute

# Good: Tests behavior
def test_user_name():
    user = User(name="John")
    assert user.get_name() == "John"
```

## Coverage Targets

- **Critical paths**: 90-100% coverage
- **Core business logic**: 80-90% coverage
- **Integration points**: 70-80% coverage
- **UI/Presentation**: 40-60% coverage (harder to test)
- **Utilities/Helpers**: 80%+ coverage

Remember: High coverage doesn't guarantee quality. Focus on testing behavior, not just lines of code.
