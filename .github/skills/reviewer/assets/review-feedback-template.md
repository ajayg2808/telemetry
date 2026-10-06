# Review Feedback Template

Use this template to provide constructive code review feedback.

## Review Header

- **PR/Commit**: [PR #123 or Commit ID]
- **Reviewed By**: [Your name]
- **Review Date**: [Date]
- **Files Changed**: [Number]
- **Lines Changed**: [+X, -Y]

---

## Overall Assessment

### Scope & Completeness
- [ ] Feature is fully implemented
- [ ] Feature matches requirements
- [ ] All acceptance criteria met
- [ ] No incomplete work committed

### Code Quality
- [ ] Code follows project standards
- [ ] Adequate test coverage
- [ ] Well-documented
- [ ] Minimal technical debt

### Architecture
- [ ] Follows established patterns
- [ ] Maintains modularity
- [ ] No concerning dependencies
- [ ] Scalable design

---

## Detailed Feedback

### Critical Issues (Must Fix Before Merge)

#### Issue 1: [Issue Title]
**File**: [path/to/file.py]  
**Line**: [Line number]  
**Severity**: 🔴 Critical  
**Category**: [Functionality/Security/Performance/Architecture]

**Current Code**:
```python
# Paste the problematic code here
def handle_user_data(user_id):
    data = get_user_data(user_id)
    save_to_database(data)  # No error handling
```

**Problem**:
[Explain what the issue is and why it's problematic]

This code doesn't handle cases where `get_user_data()` fails or returns None. This could cause silent failures and data corruption.

**Suggested Fix**:
```python
def handle_user_data(user_id: str) -> bool:
    try:
        data = get_user_data(user_id)
        if data is None:
            logger.error(f"No user data for ID: {user_id}")
            return False
        save_to_database(data)
        return True
    except DatabaseError as e:
        logger.error(f"Failed to save user data: {e}")
        return False
```

**Reference**: [Link to coding standard or pattern]

---

### Major Issues (Strongly Recommended Fixes)

#### Issue 1: [Issue Title]
**File**: [path/to/file.py]  
**Line**: [Line number]  
**Severity**: 🟠 Major  
**Category**: [Code Quality/Testing/Architecture]

**Current Code**:
```python
# Code snippet
def process_items(items):
    for item in items:
        for sub_item in item.children:
            for detail in sub_item.details:
                # Deep nesting
                if detail.active:
                    # ...
```

**Problem**:
[Explain the issue]

The nested loops create high cyclomatic complexity and make the code hard to test and maintain.

**Suggested Improvement**:
[Show a better approach]

```python
def process_items(items):
    for active_detail in get_active_details(items):
        handle_detail(active_detail)

def get_active_details(items):
    for item in items:
        for sub_item in item.children:
            yield from (d for d in sub_item.details if d.active)
```

---

### Minor Issues & Suggestions

#### Suggestion 1: Improve Naming
**File**: [path/to/file.py]  
**Line**: [Line number]  
**Severity**: 🟡 Minor

**Current**: `d = calc_val(x, y)`  
**Suggested**: `discount = calculate_final_price(base_price, percentage)`

Descriptive names make code more readable.

#### Suggestion 2: Add Type Hints
**File**: [path/to/file.py]  
**Line**: [Line number]

Consider adding type hints to improve code clarity:
```python
def process_data(items):  # Current
def process_data(items: list[dict]) -> list[dict]:  # Suggested
```

#### Suggestion 3: Refactoring Opportunity
**File**: [path/to/file.py]  
**Lines**: [X-Y]

This logic is duplicated with code in `other_file.py`. Consider extracting to a shared utility.

---

## Positive Feedback

### What You Did Well ✓

1. **Clear Test Coverage**
   - Tests cover happy path and edge cases
   - Good use of fixtures for test data
   - Tests are independent and fast

2. **Good Documentation**
   - Docstrings explain complex logic
   - Examples provided for public APIs
   - Type hints improve clarity

3. **Thoughtful Architecture**
   - Good separation of concerns
   - Interfaces are well-designed
   - Easy to extend without modification

---

## Questions & Clarifications

1. **Question**: In `handle_payment()`, why use `synchronous` instead of `asynchronous` processing?
   **Context**: This could be a performance bottleneck under load
   **Suggestion**: Consider async approach or explain why sync is preferred

2. **Question**: Database migration - will this work with existing data?
   **Context**: Migration adds NOT NULL constraint to existing column
   **Suggestion**: Show migration script or explain data handling strategy

---

## Test Coverage Review

### Test Status
- [ ] All tests passing
- [ ] Coverage adequate (target: 80%+)
- [ ] Edge cases tested
- [ ] Error scenarios tested

### Coverage Observations
- **Good**: Database layer is well-tested (92% coverage)
- **Needs work**: Error handling paths could use more testing
- **Gap**: Concurrent access scenarios not covered

### Test Suggestions
```python
# Add test for concurrent access
def test_handles_concurrent_writes():
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(update_user, user_id) 
                   for user_id in range(100)]
        results = [f.result() for f in futures]
    assert all(r.success for r in results)
```

---

## Security & Performance Review

### Security Observations
- [ ] No hardcoded secrets ✓
- [ ] Input validation present ✓
- [ ] SQL injection risk identified ⚠️
  - **Issue**: User input not parameterized in query
  - **Fix**: Use prepared statements

### Performance Observations
- [ ] No N+1 query issues detected ✓
- [ ] Algorithm complexity reasonable ✓
- [ ] Potential issue: Large memory allocation
  - **Line**: [X]
  - **Issue**: Loading entire dataset into memory
  - **Suggestion**: Use streaming/pagination

---

## Decision

### Review Verdict

- [ ] **APPROVED** ✓
  - Code is ready to merge
  - No blockers identified
  
- [ ] **APPROVED WITH COMMENTS** ⚠️
  - Minor issues noted, but don't block merge
  - Consider addressing before release
  
- [ ] **REQUEST CHANGES** 🔴
  - One or more critical/major issues must be addressed
  - Please resubmit for review after fixes
  
- [ ] **BLOCKED** ⛔
  - Critical security or architectural issues
  - Do not merge

### Summary by Issue Severity

| Severity | Count | Decision Impact |
|---|---|---|
| Critical 🔴 | 1 | **Must Fix** |
| Major 🟠 | 1 | **Strongly Recommend** |
| Minor 🟡 | 3 | **Consider** |

---

## Next Steps

1. **For Approved PRs**:
   - [ ] Address any "strongly recommended" feedback
   - [ ] Merge when ready
   - [ ] Deploy to staging for integration testing

2. **For PRs Requesting Changes**:
   - [ ] Fix critical issues (all 🔴)
   - [ ] Address major issues (🟠) or explain decision
   - [ ] Resubmit for review
   - [ ] Respond to each comment

3. **For Blocked PRs**:
   - [ ] Schedule discussion with code author
   - [ ] Document architectural/security decision
   - [ ] Resubmit with changes

---

## Resources & References

- [Python Coding Standards](../references/python-conventions.md)
- [Architecture Guidelines](../references/architectural-principles.md)
- [Test Best Practices](../references/testing-best-practices.md)
- [Security Checklist](../assets/security-checklist.md)

---

## Reviewer Notes

[Additional observations or context about this review]

---

**Reviewed By**: [Name]  
**Review Date**: [Date]  
**Time Spent**: [X minutes]  
**Review Status**: [Draft / Submitted / Complete]
