# Code Review Checklist

Use this checklist to conduct thorough, consistent code reviews.

## Pre-Review

- [ ] I understand the feature/requirements being implemented
- [ ] I have the PR description and associated requirements
- [ ] I understand the architectural constraints
- [ ] I'm familiar with the codebase conventions

## Functionality & Correctness

- [ ] Code implements the feature as described
- [ ] All acceptance criteria are met
- [ ] Test cases verify the expected behavior
- [ ] Edge cases are handled appropriately
- [ ] Error scenarios are handled
- [ ] No obvious bugs or logic errors
- [ ] Function signatures are correct and clear
- [ ] Return values are correct and complete
- [ ] No off-by-one errors (if applicable)
- [ ] Null/empty input handling is correct
- [ ] All tests pass

## Code Quality

### Naming & Readability
- [ ] Variable names are clear and meaningful
- [ ] Function/method names describe what they do
- [ ] Class names are nouns, method names are verbs
- [ ] No misleading or cryptic names
- [ ] Naming follows project conventions (camelCase, snake_case, etc.)

### Complexity & Structure
- [ ] Functions are appropriately sized (not too large)
- [ ] Cyclomatic complexity is reasonable (< 10)
- [ ] No deeply nested code (max 3 levels)
- [ ] Logic is easy to follow
- [ ] Code duplication is minimized
- [ ] Early returns used to reduce nesting

### Documentation & Comments
- [ ] Complex logic is commented
- [ ] Comments explain "why," not "what"
- [ ] Public APIs have docstrings
- [ ] Comments are accurate and up-to-date
- [ ] No dead code or commented-out code

## Architecture & Design

- [ ] Changes follow project architecture patterns
- [ ] No circular dependencies introduced
- [ ] Modularity and loose coupling maintained
- [ ] SOLID principles are followed
- [ ] Appropriate design patterns used
- [ ] No God objects or over-sized classes
- [ ] Separation of concerns is clear
- [ ] Public/private visibility is appropriate

### Dependencies
- [ ] External dependencies are justified
- [ ] Dependency versions are pinned appropriately
- [ ] No unnecessary dependencies added
- [ ] Dependency tree is not bloated

## Testing

- [ ] Test coverage is adequate
- [ ] Tests are meaningful and not trivial
- [ ] Tests check behavior, not implementation
- [ ] Edge cases are tested
- [ ] Error scenarios are tested
- [ ] Tests are independent (no test order dependency)
- [ ] Test names clearly describe what they test
- [ ] Mocks/stubs are used appropriately
- [ ] No hardcoded test data (use fixtures)
- [ ] Tests are isolated and repeatable

## Performance & Scalability

- [ ] No obvious performance issues
- [ ] Algorithm complexity is reasonable
- [ ] No N+1 queries or loops
- [ ] Resource cleanup (file handles, connections)
- [ ] No memory leaks
- [ ] Scalability concerns are addressed

## Security

- [ ] No hardcoded secrets or credentials
- [ ] Input validation is present
- [ ] Output encoding is appropriate
- [ ] Authentication/authorization checks are correct
- [ ] Sensitive data is protected
- [ ] SQL injection vulnerabilities are prevented
- [ ] No dangerous functions used unsafely

## Error Handling & Logging

- [ ] Errors are handled explicitly
- [ ] Exception types are specific, not generic
- [ ] Error messages provide useful context
- [ ] Appropriate logging levels used
- [ ] No sensitive data in logs
- [ ] Stack traces are logged for debugging

## Standards & Conventions

- [ ] Code follows project style guide
- [ ] Formatting is consistent
- [ ] No linting errors
- [ ] Imports are organized
- [ ] No unused imports or variables
- [ ] Type hints are present (if applicable)
- [ ] Follows language idioms and best practices

## Configuration & Deployment

- [ ] Configuration is externalized
- [ ] No environment-specific hardcoding
- [ ] Migration scripts are present (if needed)
- [ ] Database schema changes are documented
- [ ] Backward compatibility is maintained
- [ ] Deployment instructions are clear

## Documentation & Communication

- [ ] README updated (if applicable)
- [ ] API documentation updated
- [ ] CHANGELOG entry added
- [ ] Commit messages are clear and descriptive
- [ ] PR description is complete
- [ ] Breaking changes are documented
- [ ] Migration guide provided (if needed)

## Version Control

- [ ] Commits are logical and atomic
- [ ] Commit messages follow conventions
- [ ] No merge conflicts
- [ ] Branch is up-to-date with main
- [ ] No unnecessary whitespace changes
- [ ] No debug code committed

## Review Decision

| Category | Status |
|---|---|
| Functionality | ✓ / ✗ / ? |
| Code Quality | ✓ / ✗ / ? |
| Tests | ✓ / ✗ / ? |
| Architecture | ✓ / ✗ / ? |
| Security | ✓ / ✗ / ? |
| Documentation | ✓ / ✗ / ? |

### Overall Decision
- [ ] **APPROVED** – Ready to merge
- [ ] **APPROVED WITH COMMENTS** – Minor issues, can merge after addressing
- [ ] **REQUEST CHANGES** – Address issues before merging
- [ ] **BLOCKED** – Critical issues, do not merge

### Summary Comments
[General observations about the code]

### Critical Issues
- [Issue 1]
- [Issue 2]

### Major Issues
- [Issue 1]
- [Issue 2]

### Minor Issues/Suggestions
- [Issue 1]
- [Issue 2]

---

**Reviewed By**: [Name]  
**Date**: [Date]  
**Time Spent**: [Minutes]
