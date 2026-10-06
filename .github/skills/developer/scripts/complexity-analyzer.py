#!/usr/bin/env python3
"""
Complexity Analyzer Script

Analyzes cyclomatic complexity and code metrics to identify overly complex functions.
"""

import os
import sys
import re
from pathlib import Path
from collections import defaultdict


def calculate_cyclomatic_complexity(code):
    """
    Calculate cyclomatic complexity by counting decision points.
    CC = number of decisions + 1
    """
    # Count decision keywords
    decisions = len(re.findall(r'\b(if|elif|for|while|and|or|except|case)\b', code))
    return decisions + 1


def analyze_function(func_code, func_name, file_path, line_num):
    """Analyze a single function."""
    complexity = calculate_cyclomatic_complexity(func_code)
    lines = len(func_code.split('\n'))
    
    return {
        'name': func_name,
        'file': file_path,
        'line': line_num,
        'complexity': complexity,
        'lines': lines,
        'status': 'LOW' if complexity < 5 else 'MEDIUM' if complexity < 10 else 'HIGH'
    }


def extract_functions(file_path):
    """Extract all functions/methods from a Python file."""
    functions = []
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.split('\n')
        
        # Find function definitions
        in_function = False
        func_start = 0
        func_name = ""
        indent_level = 0
        func_content = []
        
        for i, line in enumerate(lines):
            # Check for function definition
            match = re.match(r'^(\s*)def\s+(\w+)\s*\(', line)
            if match:
                # Save previous function if any
                if in_function and func_content:
                    func_code = '\n'.join(func_content)
                    func_analysis = analyze_function(func_code, func_name, file_path, func_start + 1)
                    functions.append(func_analysis)
                
                # Start new function
                in_function = True
                indent_level = len(match.group(1))
                func_start = i
                func_name = match.group(2)
                func_content = [line]
            
            elif in_function:
                # Check if we're still in the function (indentation check)
                if line.strip() and not line.startswith(' ' * (indent_level + 1)) and line.strip() != '':
                    # End of function
                    func_code = '\n'.join(func_content)
                    func_analysis = analyze_function(func_code, func_name, file_path, func_start + 1)
                    functions.append(func_analysis)
                    in_function = False
                    func_content = []
                else:
                    func_content.append(line)
        
        # Don't forget last function
        if in_function and func_content:
            func_code = '\n'.join(func_content)
            func_analysis = analyze_function(func_code, func_name, file_path, func_start + 1)
            functions.append(func_analysis)
    
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}", file=sys.stderr)
    
    return functions


def analyze_project(root_path="."):
    """Analyze entire project for complexity."""
    print("Analyzing code complexity...")
    print(f"Root path: {root_path}\n")
    
    all_functions = []
    file_count = 0
    
    # Find all Python files
    for root, dirs, files in os.walk(root_path):
        # Skip common directories
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.venv', 'venv', 'tests', 'test']]
        
        for file in files:
            if file.endswith('.py') and not file.startswith('test_'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, root_path)
                
                functions = extract_functions(file_path)
                all_functions.extend(functions)
                file_count += 1
    
    print(f"Found {file_count} Python files, {len(all_functions)} functions\n")
    
    # Complexity distribution
    print("=" * 70)
    print("COMPLEXITY ANALYSIS")
    print("=" * 70)
    
    low = [f for f in all_functions if f['status'] == 'LOW']
    medium = [f for f in all_functions if f['status'] == 'MEDIUM']
    high = [f for f in all_functions if f['status'] == 'HIGH']
    
    print(f"\n✓ LOW complexity (CC 1-4):      {len(low):3} functions")
    print(f"⚠ MEDIUM complexity (CC 5-9):  {len(medium):3} functions")
    print(f"✗ HIGH complexity (CC 10+):    {len(high):3} functions")
    
    print(f"\nAverage complexity: {sum(f['complexity'] for f in all_functions) / len(all_functions) if all_functions else 0:.1f}")
    
    # Show high complexity functions
    if high:
        print("\n" + "=" * 70)
        print("HIGH COMPLEXITY FUNCTIONS (Review & Refactor)")
        print("=" * 70)
        
        sorted_high = sorted(high, key=lambda x: -x['complexity'])
        for func in sorted_high[:10]:  # Show top 10
            print(f"\n{func['file']}:{func['line']}")
            print(f"  Function: {func['name']}")
            print(f"  Complexity: {func['complexity']} | Lines: {func['lines']}")
            print(f"  Action: Consider breaking into smaller functions")
    
    # Show medium complexity functions
    if medium:
        print("\n" + "=" * 70)
        print(f"MEDIUM COMPLEXITY FUNCTIONS (Monitor - showing first 10)")
        print("=" * 70)
        
        sorted_medium = sorted(medium, key=lambda x: -x['complexity'])
        for func in sorted_medium[:10]:
            print(f"{func['file']}:{func['line']} - {func['name']} (CC={func['complexity']})")
    
    # Statistics
    print("\n" + "=" * 70)
    print("STATISTICS")
    print("=" * 70)
    
    complexities = [f['complexity'] for f in all_functions]
    if complexities:
        print(f"Min complexity:     {min(complexities)}")
        print(f"Max complexity:     {max(complexities)}")
        print(f"Average complexity: {sum(complexities) / len(complexities):.1f}")
        print(f"Median complexity:  {sorted(complexities)[len(complexities)//2]}")
    
    # Recommendations
    print("\n" + "=" * 70)
    print("RECOMMENDATIONS")
    print("=" * 70)
    
    if high:
        print(f"\n⚠️  REFACTOR: {len(high)} functions have high complexity (CC >= 10)")
        print("   These functions are difficult to test and maintain.")
        print("   Consider breaking them into smaller functions.")
        print("\n   Refactoring suggestions:")
        print("   - Extract helper functions")
        print("   - Use guard clauses to reduce nesting")
        print("   - Consider strategy pattern for complex logic")
    else:
        print("\n✓ All functions have reasonable complexity")
    
    if medium:
        print(f"\n⚠️  MONITOR: {len(medium)} functions have medium complexity (5 <= CC < 10)")
        print("   These functions should be reviewed during code reviews.")
        print("   Consider refactoring if they become any more complex.")
    
    print(f"\n✓ GOOD: {len(low)} functions have low complexity (CC <= 4)")


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    analyze_project(root)
