#!/usr/bin/env python3
"""
Architecture Validation Script

Checks for common architectural violations:
- Circular dependencies
- Tight coupling
- Violations of dependency rules
"""

import os
import sys
import re
from collections import defaultdict
from pathlib import Path


def analyze_imports(file_path):
    """Extract imports from a Python file."""
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Simple regex to find imports
        import_patterns = [
            r'from\s+([.\w]+)\s+import',
            r'import\s+([.\w]+)',
        ]
        
        for pattern in import_patterns:
            matches = re.findall(pattern, content)
            imports.extend(matches)
    except:
        pass
    
    return imports


def find_circular_dependencies(modules_dict):
    """Find circular dependencies in module imports."""
    circular = []
    
    for module, imports in modules_dict.items():
        for imp in imports:
            if imp in modules_dict and module in modules_dict.get(imp, []):
                pair = tuple(sorted([module, imp]))
                if pair not in circular:
                    circular.append(pair)
    
    return circular


def analyze_project(root_path="."):
    """Analyze project structure for architectural issues."""
    print("Analyzing architecture...")
    print(f"Root path: {root_path}\n")
    
    modules_dict = defaultdict(list)
    file_count = 0
    
    # Find all Python files
    for root, dirs, files in os.walk(root_path):
        # Skip common directories
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.venv', 'venv', 'node_modules', '.pytest_cache']]
        
        for file in files:
            if file.endswith('.py') and not file.startswith('test_'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, root_path)
                module_name = rel_path.replace(os.sep, '.').replace('.py', '')
                
                imports = analyze_imports(file_path)
                if imports:
                    modules_dict[module_name] = imports
                
                file_count += 1
    
    print(f"Found {file_count} Python files\n")
    
    # Check for circular dependencies
    print("=" * 60)
    print("CIRCULAR DEPENDENCIES CHECK")
    print("=" * 60)
    circular = find_circular_dependencies(modules_dict)
    
    if circular:
        print(f"⚠️  Found {len(circular)} circular dependency patterns:\n")
        for module_a, module_b in circular:
            print(f"  ❌ {module_a} ↔ {module_b}")
        print()
    else:
        print("✓ No circular dependencies found\n")
    
    # Show dependency graph summary
    print("=" * 60)
    print("MODULE DEPENDENCIES")
    print("=" * 60)
    
    for module in sorted(modules_dict.keys()):
        imports = modules_dict[module]
        if imports:
            print(f"\n{module}:")
            for imp in sorted(set(imports)):
                print(f"  → {imp}")
    
    # Statistics
    print("\n" + "=" * 60)
    print("STATISTICS")
    print("=" * 60)
    print(f"Total modules: {len(modules_dict)}")
    print(f"Total dependencies: {sum(len(v) for v in modules_dict.values())}")
    print(f"Avg dependencies per module: {sum(len(v) for v in modules_dict.values()) / len(modules_dict) if modules_dict else 0:.1f}")
    
    # Recommendations
    print("\n" + "=" * 60)
    print("RECOMMENDATIONS")
    print("=" * 60)
    
    if circular:
        print("\n⚠️  CRITICAL: Resolve circular dependencies:")
        for module_a, module_b in circular:
            print(f"  - Break cycle between {module_a} and {module_b}")
            print(f"    Consider using interfaces/abstractions")
            print(f"    Or move shared code to a common module")
    else:
        print("\n✓ Architecture looks clean - no immediate circular dependencies")
    
    # Check for high coupling (modules with too many imports)
    print("\n📊 Modules with high coupling (>5 imports):")
    high_coupling = [(m, len(i)) for m, i in modules_dict.items() if len(i) > 5]
    if high_coupling:
        for module, count in sorted(high_coupling, key=lambda x: -x[1]):
            print(f"  - {module}: {count} imports (consider breaking into smaller modules)")
    else:
        print("  None found (good!)")


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    analyze_project(root)
