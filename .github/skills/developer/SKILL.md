---
name: developer
description: 'Implement code following best practices, design patterns, and coding standards. Use when writing features, refactoring code, establishing code conventions, ensuring code quality, and following SOLID principles.'
argument-hint: 'Describe the feature to implement, existing codebase patterns, and any constraints'
user-invocable: true
---

# Developer Skill

## When to Use

- Implementing new features and functionality
- Refactoring code for clarity and maintainability
- Writing code that follows established patterns
- Establishing coding standards and conventions
- Applying SOLID principles
- Writing clean, idiomatic code
- Setting up project structure and boilerplate

## Core Principles

1. **SOLID Principles** – Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
2. **DRY (Don't Repeat Yourself)** – Eliminate code duplication
3. **KISS (Keep It Simple, Stupid)** – Favor clarity over cleverness
4. **Code Readability** – Clear naming, minimal complexity
5. **Best Practices** – Follow language and framework conventions
6. **Testing** – Write testable, maintainable code

## Procedure

### 1. Understand Requirements
- Review feature specification
- Check [coding-standards](./references/coding-standards.md) for your language
- Identify relevant design patterns

### 2. Plan Implementation
- Sketch module/class structure
- Review [design-patterns guide](./references/design-patterns.md)
- Check for existing similar implementations

### 3. Code with Standards
- Follow [language-specific conventions](./references/language-conventions.md)
- Use [code-templates](./assets/code-templates/) for boilerplate
- Apply SOLID principles at each step

### 4. Implement Incrementally
- Build in small, testable pieces
- Write self-documenting code
- Use meaningful naming conventions

### 5. Refactor for Clarity
- Extract methods and functions
- Reduce cyclomatic complexity
- Remove code duplication using [refactoring checklist](./references/refactoring-checklist.md)

### 6. Code Review Readiness
- Ensure code follows standards
- Add necessary documentation
- Verify testability

## Best Practices

### Naming
- Use clear, descriptive names for variables, functions, classes
- Follow language conventions (snake_case for Python, camelCase for JS, PascalCase for classes)
- Avoid abbreviations except widely-accepted ones

### Functions/Methods
- Keep functions focused and small (single responsibility)
- Prefer pure functions with minimal side effects
- Use consistent parameter patterns

### Classes/Modules
- One concept per class/module
- Clear public interface, private implementation details
- Favor composition over inheritance

### Code Structure
- Group related code together
- Consistent formatting and indentation
- Clear separation between concerns

### Error Handling
- Use specific exception types
- Provide meaningful error messages
- Fail fast and loudly
- Handle recoverable errors gracefully

### Comments and Documentation
- Write self-documenting code first
- Comments explain "why," not "what"
- Keep documentation in sync with code

## Language-Specific Resources

See detailed guides for your language:
- [Python Conventions](./references/python-conventions.md)
- [JavaScript/TypeScript Conventions](./references/js-conventions.md)
- [General Coding Standards](./references/coding-standards.md)

## Assets

Use these templates and boilerplate to accelerate development:
- [Code Templates](./assets/code-templates/)
- [Project Structure Template](./assets/project-structure-template.md)
- [Module Template](./assets/module-template.md)

## Scripts

Run these tools to check code quality:
- [check-style.py](./scripts/check-style.py) – Verify code style compliance
- [complexity-analyzer.py](./scripts/complexity-analyzer.py) – Identify overly complex functions
- [duplication-detector.py](./scripts/duplication-detector.py) – Find code duplication
- [dependency-checker.py](./scripts/dependency-checker.py) – Validate module dependencies
