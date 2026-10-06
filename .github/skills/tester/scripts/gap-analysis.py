#!/usr/bin/env python3
"""
Test Gap Analysis Script

Identifies gaps in test coverage and suggests test cases.
"""

import sys
import os
import re
from pathlib import Path
from collections import defaultdict


def extract_functions(file_path):
    """Extract function definitions from a Python file."""
    functions = []
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.split('\n')
        
        for i, line in enumerate(lines):
            # Find function definitions
            match = re.match(r'^\s*def\s+(\w+)\s*\(([^)]*)\)', line)
            if match and not line.strip().startswith('#'):
                func_name = match.group(1)
                params = match.group(2)
                
                # Skip private/protected functions and test functions
                if not func_name.startswith('_'):
                    functions.append({
                        'name': func_name,
                        'line': i + 1,
                        'params': len(params.split(',')) if params.strip() else 0
                    })
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}", file=sys.stderr)
    
    return functions


def extract_test_cases(test_file):
    """Extract test case definitions from a test file."""
    tests = []
    
    try:
        with open(test_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Find all test functions
        matches = re.findall(r'def\s+(test_\w+)\s*\(', content)
        tests.extend(matches)
    except:
        pass
    
    return tests


def find_untested_functions(source_file, test_file):
    """Find functions without tests."""
    source_functions = extract_functions(source_file)
    test_cases = extract_test_cases(test_file)
    
    # Extract function names from test case names
    tested_functions = set()
    for test_name in test_cases:
        # Extract function name from test
        # e.g., test_calculate_total -> calculate_total
        func_name = test_name.replace('test_', '').split('_when_')[0].split('_if_')[0]
        tested_functions.add(func_name)
    
    untested = []
    for func in source_functions:
        if func['name'] not in tested_functions:
            untested.append(func)
    
    return untested, tested_functions


def analyze_error_handling(file_path):
    """Identify error handling that might not be tested."""
    error_patterns = []
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines):
            # Look for exception handling
            if 'except' in line or 'raise' in line or 'try:' in line:
                error_patterns.append({
                    'line': i + 1,
                    'code': line.strip()
                })
    except:
        pass
    
    return error_patterns


def analyze_branches(file_path):
    """Identify conditional branches that might not be tested."""
    branches = []
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines):
            # Look for if/elif/else
            if re.search(r'\b(if|elif|else)\b', line):
                branches.append({
                    'line': i + 1,
                    'code': line.strip()
                })
    except:
        pass
    
    return branches


def main(project_root="."):
    """Analyze test gaps in project."""
    print("=" * 70)
    print("TEST GAP ANALYSIS")
    print("=" * 70)
    print()
    
    # Find Python source files
    source_dir = os.path.join(project_root, "src")
    test_dir = os.path.join(project_root, "tests")
    
    if not os.path.exists(source_dir):
        print(f"Source directory not found: {source_dir}")
        return 1
    
    if not os.path.exists(test_dir):
        print(f"Test directory not found: {test_dir}")
        print("Creating test structure...\n")
    
    # Analyze each source file
    total_functions = 0
    total_untested = 0
    gap_details = []
    
    for root, dirs, files in os.walk(source_dir):
        dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git']]
        
        for file in files:
            if file.endswith('.py') and not file.startswith('test_'):
                source_file = os.path.join(root, file)
                
                # Find corresponding test file
                rel_path = os.path.relpath(source_file, source_dir)
                test_file = os.path.join(test_dir, f"test_{rel_path}")
                
                # Analyze gap
                functions = extract_functions(source_file)
                total_functions += len(functions)
                
                if os.path.exists(test_file):
                    untested, tested = find_untested_functions(source_file, test_file)
                else:
                    untested = functions
                    tested = set()
                
                total_untested += len(untested)
                
                if untested:
                    gap_details.append({
                        'file': rel_path,
                        'tested': len(functions) - len(untested),
                        'untested': len(untested),
                        'functions': untested
                    })
    
    # Report
    print(f"Total Functions Analyzed: {total_functions}")
    print(f"Untested Functions: {total_untested}")
    
    if total_functions > 0:
        coverage_pct = ((total_functions - total_untested) / total_functions) * 100
        print(f"Function Coverage: {coverage_pct:.1f}%")
    
    print("\n" + "=" * 70)
    print("DETAILED GAP ANALYSIS")
    print("=" * 70)
    
    for gap in gap_details:
        print(f"\n{gap['file']}")
        print(f"  Tested: {gap['tested']}, Untested: {gap['untested']}")
        
        if gap['functions']:
            print(f"  Functions needing tests:")
            for func in gap['functions']:
                print(f"    - {func['name']} (line {func['line']}, {func['params']} params)")
    
    # Recommendations
    print("\n" + "=" * 70)
    print("RECOMMENDATIONS")
    print("=" * 70)
    print()
    
    if total_untested > 0:
        print(f"⚠️  {total_untested} functions lack test coverage")
        print("\nPriority areas to test:")
        
        # Sort by number of untested functions
        sorted_gaps = sorted(gap_details, key=lambda x: -x['untested'])
        for gap in sorted_gaps[:5]:
            print(f"\n{gap['file']}: {gap['untested']} untested functions")
            print("  Suggested test template:")
            print(f"    def test_{{function_name}}_{{scenario}}():")
            print(f"        # Arrange: Set up test data")
            print(f"        # Act: Call function")
            print(f"        # Assert: Verify results")
    else:
        print("✓ All functions have test coverage!")
    
    print("\n" + "=" * 70)
    print("TEST DEVELOPMENT SUGGESTIONS")
    print("=" * 70)
    print("""
For each untested function, consider these test scenarios:

1. Happy Path: Function works with valid inputs
   - test_function_name_returns_expected_value()

2. Edge Cases: Boundary values and special cases
   - test_function_name_with_empty_input()
   - test_function_name_with_maximum_value()
   - test_function_name_with_null_input()

3. Error Scenarios: Invalid inputs and error conditions
   - test_function_name_raises_error_with_invalid_input()
   - test_function_name_handles_missing_dependency()

4. Integration: Interaction with other components
   - test_function_name_calls_dependency_correctly()
   - test_function_name_handles_dependency_failure()

Example test structure:
```python
def test_calculate_total_with_valid_items():
    # Arrange
    items = [Item(10.0), Item(20.0)]
    
    # Act
    total = calculate_total(items)
    
    # Assert
    assert total == 30.0

def test_calculate_total_raises_error_with_empty_items():
    # Arrange
    items = []
    
    # Act & Assert
    with pytest.raises(ValueError):
        calculate_total(items)
```
    """)
    
    return 0 if total_untested == 0 else 1


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(main(root))
