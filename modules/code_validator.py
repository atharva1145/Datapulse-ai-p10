"""
Module: AST-Based Code Validator
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Strict Abstract Syntax Tree (AST) validation for LLM-generated Python code.
Enforces an allowlist of permitted Pandas operations and blocks:
- Imports (import, from ... import)
- Filesystem access (open, Path, etc.)
- Network / subprocess access (os, sys, subprocess, socket)
- Arbitrary code execution (eval, exec, __import__, compile)
- Private / dunder attribute access (__class__, __subclasses__)
"""

import ast
from typing import Tuple, List, Set, Optional

# Strictly approved Pandas / NumPy / Python builtin functions and methods
ALLOWED_FUNCTIONS: Set[str] = {
    # Builtins
    "len", "range", "round", "min", "max", "sum", "abs", "int", "float", "str", "bool", "list", "dict", "tuple", "set", "print",
    # Pandas / Series / DataFrame safe methods
    "head", "tail", "describe", "mean", "median", "std", "var", "quantile",
    "sum", "count", "nunique", "value_counts", "isnull", "isna", "notnull", "notna",
    "dropna", "fillna", "sort_values", "sort_index", "groupby", "agg", "aggregate",
    "reset_index", "set_index", "select_dtypes", "corr", "cov", "nlargest", "nsmallest",
    "unique", "astype", "isin", "between", "copy", "to_dict", "to_frame",
    "min", "max", "clip", "idxmin", "idxmax", "loc", "iloc", "query", "filter", "shape", "dtypes", "columns", "index",
    # NumPy safe operations
    "array", "sqrt", "log", "exp", "round_", "mean", "median", "std"
}

# Forbidden modules and functions that present security or sandbox breakout risks
FORBIDDEN_IDENTIFIERS: Set[str] = {
    "os", "sys", "subprocess", "socket", "requests", "urllib", "http", "shutil",
    "pathlib", "importlib", "__import__", "eval", "exec", "compile", "globals",
    "locals", "vars", "input", "open", "file", "breakpoint", "getattr", "setattr",
    "delattr", "hasattr", "__subclasses__", "__bases__", "__class__", "__code__"
}

class SecurityVisitor(ast.NodeVisitor):
    """Walks the AST and records any unauthorized syntax elements or forbidden calls."""

    def __init__(self):
        self.violations: List[str] = []

    def visit_Import(self, node: ast.Import):
        names = [alias.name for alias in node.names]
        self.violations.append(f"Security Alert: Import statement forbidden -> 'import {', '.join(names)}'")
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        mod = node.module or ""
        self.violations.append(f"Security Alert: From-import forbidden -> 'from {mod} import ...'")
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        # Check direct function call: e.g., open('file'), eval('...')
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            if func_name in FORBIDDEN_IDENTIFIERS:
                self.violations.append(f"Security Alert: Forbidden function call -> '{func_name}()'")
            elif func_name not in ALLOWED_FUNCTIONS:
                self.violations.append(f"Security Alert: Unapproved function call -> '{func_name}()'")
        
        # Check method calls: e.g., df.to_csv(), os.system()
        elif isinstance(node.func, ast.Attribute):
            attr_name = node.func.attr
            if attr_name.startswith("__") or attr_name in FORBIDDEN_IDENTIFIERS:
                self.violations.append(f"Security Alert: Forbidden attribute/method call -> '.{attr_name}()'")
            elif attr_name in {"to_csv", "to_sql", "to_parquet", "to_pickle", "to_excel"}:
                self.violations.append(f"Security Alert: Disk write method forbidden -> '.{attr_name}()'")

        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute):
        if node.attr.startswith("__") and node.attr.endswith("__"):
            self.violations.append(f"Security Alert: Dunder attribute access forbidden -> '{node.attr}'")
        elif node.attr in FORBIDDEN_IDENTIFIERS:
            self.violations.append(f"Security Alert: Forbidden attribute access -> '{node.attr}'")
        self.generic_visit(node)

    def visit_Delete(self, node: ast.Delete):
        self.violations.append("Security Alert: 'del' statements are forbidden.")
        self.generic_visit(node)

def validate_python_code(code: str) -> Tuple[bool, List[str], Optional[ast.AST]]:
    """
    Parses and inspects code string via AST.
    Returns:
        (is_valid: bool, violations: List[str], parsed_ast)
    """
    if not code or not code.strip():
        return False, ["Code string is empty."], None

    # 1. Syntax Tree Compilation
    try:
        tree = ast.parse(code)
    except SyntaxError as se:
        return False, [f"Python Syntax Error: {se.msg} at line {se.lineno}"], None
    except Exception as e:
        return False, [f"AST parsing failed: {str(e)}"], None

    # 2. Walk AST to detect forbidden nodes
    visitor = SecurityVisitor()
    visitor.visit(tree)

    if visitor.violations:
        return False, visitor.violations, None

    return True, [], tree
