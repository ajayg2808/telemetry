# Test Case Design Guide

## Test Case Structure

Every test case should follow the **AAA Pattern** (Arrange-Act-Assert):

```python
def test_should_calculate_total_with_valid_items():
    # ARRANGE: Set up initial conditions
    cart = Cart()
    item1 = Item(name="Widget", price=10.0)
    item2 = Item(name="Gadget", price=20.0)
    cart.add_item(item1)
    cart.add_item(item2)
    
    # ACT: Perform the action being tested
    total = cart.calculate_total()
    
    # ASSERT: Verify the outcome
    assert total == 30.0
```

## Test Case Naming

Good test names describe what is being tested and expected outcome:

| Pattern | Example | Benefit |
|---------|---------|---------|
| test_should_[behavior]_when_[condition] | test_should_return_user_when_id_exists | Very clear |
| test_[action]_with_[scenario] | test_create_order_with_valid_items | Clear |
| test_[function]_[expected_outcome] | test_calculate_total_returns_sum | Straightforward |

**Avoid:**
- `test_foo()` - Unclear what's being tested
- `test_1()`, `test_2()` - No meaning
- `test_works()` - Not specific about behavior

## Test Case Categories

### 1. Positive Test Cases (Happy Path)

Test normal, valid scenarios:

```python
def test_should_create_user_with_valid_data():
    """User can be created with valid information"""
    user = create_user(name="John", email="john@example.com")
    assert user.name == "John"
    assert user.email == "john@example.com"
```

**Guidelines:**
- Test typical/expected inputs
- Verify success path
- Check correct outputs
- One assertion per concept

### 2. Negative Test Cases (Error Handling)

Test invalid scenarios and error conditions:

```python
def test_should_raise_error_when_email_invalid():
    """Creating user with invalid email raises ValueError"""
    with pytest.raises(ValueError) as exc_info:
        create_user(name="John", email="invalid-email")
    
    assert "email" in str(exc_info.value).lower()
```

**Guidelines:**
- Test invalid inputs
- Verify error is raised
- Check error message is helpful
- Verify state doesn't change on error

### 3. Boundary Test Cases (Edge Cases)

Test limits and boundary conditions:

```python
def test_should_handle_empty_list():
    """Function handles empty input correctly"""
    result = calculate_average([])
    assert result == 0

def test_should_handle_single_item():
    """Function handles single item"""
    result = calculate_average([5.0])
    assert result == 5.0

def test_should_handle_large_values():
    """Function handles large numbers"""
    result = calculate_average([1000000, 2000000])
    assert result == 1500000
```

**Common Boundaries:**
- Empty collections
- Single item
- Maximum values
- Minimum values
- Zero
- Null/None
- Empty strings

### 4. Integration Test Cases

Test interaction between components:

```python
def test_should_save_and_retrieve_user():
    """User can be saved and retrieved from database"""
    # Create and save user
    user = create_user(name="John")
    user_id = repository.save(user)
    
    # Retrieve and verify
    retrieved = repository.get(user_id)
    assert retrieved.name == "John"
```

## Test Data Patterns

### Use Test Fixtures

```python
@pytest.fixture
def sample_user():
    return User(name="John", email="john@example.com", age=30)

def test_is_adult(sample_user):
    assert sample_user.is_adult()
```

### Use Factories for Flexibility

```python
class UserFactory:
    @staticmethod
    def create(name="John", email="john@example.com", **kwargs):
        return User(name=name, email=email, **kwargs)

def test_with_custom_age():
    user = UserFactory.create(age=17)
    assert not user.is_adult()
```

### Parametrized Tests

```python
@pytest.mark.parametrize("input,expected", [
    ([], 0),
    ([1], 1),
    ([1, 2, 3], 2),  # average
    ([10, 20], 15),
])
def test_calculate_average(input, expected):
    assert calculate_average(input) == expected
```

## Mocking & Stubbing

### Mock External Dependencies

```python
from unittest.mock import Mock, patch

def test_should_fetch_user_from_database():
    # Create mock
    mock_db = Mock()
    mock_db.get_user.return_value = User(id=1, name="John")
    
    # Test with mock
    service = UserService(mock_db)
    user = service.get_user(1)
    
    # Verify
    assert user.name == "John"
    mock_db.get_user.assert_called_once_with(1)
```

### When to Mock
- ✓ External APIs
- ✓ Databases
- ✓ File systems
- ✓ Time-dependent operations
- ✗ Core business logic
- ✗ In-memory data structures

## Assertion Patterns

### Specific Assertions

```python
# Good: Clear what's being verified
assert user.age == 25
assert len(users) == 3
assert "error" in error_message.lower()

# Bad: Vague
assert user  # What about user?
assert users  # Just checking it exists?
assert result  # What should result be?
```

### Multiple Assertions

```python
# Good: Related assertions
def test_should_create_user():
    user = create_user("John", "john@example.com")
    assert user.name == "John"
    assert user.email == "john@example.com"
    assert user.created_at is not None

# Bad: Unrelated assertions
def test_should_work():
    user = create_user("John")
    cart = create_cart()
    order = create_order()
    assert user and cart and order
```

## Test Quality Checklist

For each test case:

- [ ] Has clear, descriptive name
- [ ] Tests ONE concept or behavior
- [ ] Uses AAA pattern (Arrange-Act-Assert)
- [ ] Uses appropriate assertions
- [ ] Independent (doesn't depend on other tests)
- [ ] Repeatable (same result every time)
- [ ] Fast (runs quickly)
- [ ] Uses test data appropriately
- [ ] Has meaningful error messages
- [ ] Includes docstring explaining what it tests

## Common Anti-Patterns to Avoid

### Testing Implementation, Not Behavior

```python
# Bad: Tests private/internal details
def test_user_internal_state():
    user = User()
    assert user._data is not None  # Testing private attribute

# Good: Tests public behavior
def test_user_name():
    user = User(name="John")
    assert user.get_name() == "John"
```

### Test Interdependence

```python
# Bad: Tests depend on execution order
def test_1_create_user():
    User.create_instance("John")

def test_2_get_user():
    user = User.get_instance()  # Depends on test_1

# Good: Tests are independent
def test_create_user():
    user = User.create_instance("John")
    assert user.name == "John"

def test_get_user():
    user = create_test_user()  # Creates fresh data
    assert user.name == "John"
```

### Over-Mocking

```python
# Bad: Mocking too much, not testing real behavior
def test_service():
    mock_repository = Mock()
    mock_logger = Mock()
    mock_validator = Mock()
    service = Service(mock_repository, mock_logger, mock_validator)
    # Mocking everything - not testing real interactions

# Good: Mock only external dependencies
def test_service():
    mock_db = Mock()
    mock_db.save.return_value = True
    service = Service(mock_db)
    result = service.save_user(user)
    assert result is True
```
