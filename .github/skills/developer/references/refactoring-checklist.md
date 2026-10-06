# Refactoring Checklist

Use this checklist to ensure your refactoring maintains code quality and doesn't introduce bugs.

## Pre-Refactoring

- [ ] Tests are passing and comprehensive
- [ ] Code coverage is measured
- [ ] You have a clear understanding of what needs to change
- [ ] You can articulate the reason for refactoring (performance, clarity, maintainability, etc.)
- [ ] Changes are scoped to a single, clear goal

## During Refactoring

- [ ] Keep changes focused and small
- [ ] Refactor only code directly related to the goal
- [ ] Do not add new features during refactoring
- [ ] Maintain the same behavior (black-box refactoring)
- [ ] Run tests frequently (after each small change)
- [ ] Do not change multiple things simultaneously

### Code Quality Improvements

- [ ] Function length reduced (if applicable)
- [ ] Cyclomatic complexity reduced
- [ ] Naming improved (variables, methods, classes)
- [ ] Code duplication reduced
- [ ] Magic numbers extracted to named constants
- [ ] Comments are still accurate or removed if code is self-explanatory

### Architecture Improvements

- [ ] Responsibilities better separated
- [ ] Dependencies reduced or clarified
- [ ] Interfaces simplified
- [ ] Coupling reduced
- [ ] Cohesion improved

## Post-Refactoring

- [ ] All tests pass
- [ ] Code coverage remains the same or improves
- [ ] New code follows project conventions
- [ ] No performance regressions (verify if performance-critical)
- [ ] Changes reviewed for correctness
- [ ] Commit message clearly explains what changed and why

## Common Refactoring Patterns

### Extract Method
```python
# Before
def calculate_total(items):
    subtotal = sum(item.price * item.quantity for item in items)
    tax = subtotal * 0.1
    shipping = 10.0 if subtotal < 100 else 0
    return subtotal + tax + shipping

# After
def calculate_total(items):
    subtotal = calculate_subtotal(items)
    tax = calculate_tax(subtotal)
    shipping = calculate_shipping(subtotal)
    return subtotal + tax + shipping

def calculate_subtotal(items):
    return sum(item.price * item.quantity for item in items)
```

### Extract Variable
```python
# Before
return (customer.age > 18) and (customer.credit_score > 650) and (customer.income > 30000)

# After
is_adult = customer.age > 18
has_good_credit = customer.credit_score > 650
has_sufficient_income = customer.income > 30000
return is_adult and has_good_credit and has_sufficient_income
```

### Replace Magic Numbers with Constants
```python
# Before
if user.age >= 18 and balance > 100:
    pass

# After
LEGAL_AGE = 18
MINIMUM_BALANCE = 100.0
if user.age >= LEGAL_AGE and balance > MINIMUM_BALANCE:
    pass
```

### Introduce Interface
```python
# Before
class UserServiceSQL:
    def get_user(self, id): pass

class UserServiceMongo:
    def get_user(self, id): pass

# After
class IUserRepository:
    def get_user(self, id): pass

class UserServiceSQL(IUserRepository):
    def get_user(self, id): pass

class UserServiceMongo(IUserRepository):
    def get_user(self, id): pass
```

## Things to Avoid

- [ ] Don't refactor untested code
- [ ] Don't combine refactoring with feature changes
- [ ] Don't ignore failing tests
- [ ] Don't make stylistic changes just because you disagree with existing style
- [ ] Don't refactor other people's code without understanding intent
- [ ] Don't skip code review for "just refactoring"

## Testing During Refactoring

- [ ] Run unit tests after each change
- [ ] Run integration tests before committing
- [ ] Run full test suite before push
- [ ] Check that new code is tested
- [ ] Verify edge cases still work
