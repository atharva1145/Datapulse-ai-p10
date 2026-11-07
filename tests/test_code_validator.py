"""
Unit tests for modules/code_validator.py and modules/safe_executor.py
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)
"""

import pytest
import pandas as pd
from modules.code_validator import validate_python_code
from modules.safe_executor import execute_code_safely

def test_valid_pandas_operations():
    valid_snippets = [
        "result = df.describe()",
        "result = df['col1'].mean()",
        "result = df.sort_values(by='col1', ascending=False).head(5)",
        "result = df.groupby('col2')['col1'].agg(['mean', 'count'])",
        "result = df.isnull().sum()",
        "result = df.corr()"
    ]
    for code in valid_snippets:
        is_valid, violations, _ = validate_python_code(code)
        assert is_valid is True, f"Valid code incorrectly flagged: {code} -> {violations}"

def test_blocks_import_statements():
    malicious_snippets = [
        "import os\nresult = os.listdir('.')",
        "import sys\nresult = sys.version",
        "from subprocess import Popen\nresult = Popen(['ls'])",
        "import requests\nresult = requests.get('http://google.com')"
    ]
    for code in malicious_snippets:
        is_valid, violations, _ = validate_python_code(code)
        assert is_valid is False
        assert any("import" in v.lower() for v in violations)

def test_blocks_file_and_eval_access():
    forbidden_calls = [
        "result = open('sensitive.txt', 'r').read()",
        "result = eval('df.head()')",
        "result = exec('print(123)')",
        "result = __import__('os').system('ls')"
    ]
    for code in forbidden_calls:
        is_valid, violations, _ = validate_python_code(code)
        assert is_valid is False
        assert len(violations) > 0

def test_blocks_dunder_and_disk_writes():
    exploits = [
        "result = df.__class__.__subclasses__()",
        "df.to_csv('stolen_data.csv')",
        "df.to_pickle('stolen.pkl')"
    ]
    for code in exploits:
        is_valid, violations, _ = validate_python_code(code)
        assert is_valid is False

def test_safe_executor_success():
    df = pd.DataFrame({"col1": [10, 20, 30], "col2": ["A", "B", "A"]})
    code = "result = df['col1'].sum()"
    
    is_valid, violations, _ = validate_python_code(code)
    assert is_valid is True
    
    ok, raw_res, out_text, err = execute_code_safely(code, df)
    assert ok is True
    assert raw_res == 60
    assert err is None

def test_safe_executor_runtime_error_handled():
    df = pd.DataFrame({"col1": [10, 20, 30]})
    # Non-existent column raises KeyError
    code = "result = df['non_existent_column'].mean()"
    
    ok, raw_res, out_text, err = execute_code_safely(code, df)
    assert ok is False
    assert "KeyError" in err
