"""
Module: Safe Code Execution Engine
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Executes AST-approved Pandas code in a strictly isolated local namespace
with timeouts, output-size bounds, and stdout redirection.
"""

import sys
import io
import threading
from typing import Tuple, Any, Optional, Dict
import pandas as pd
import numpy as np
from config.settings import EXECUTION_TIMEOUT_SECONDS, MAX_OUTPUT_ROWS, MAX_OUTPUT_CHARS

# Safe builtins dictionary without disk/network/exec capabilities
SAFE_BUILTINS: Dict[str, Any] = {
    "len": len,
    "range": range,
    "round": round,
    "min": min,
    "max": max,
    "sum": sum,
    "abs": abs,
    "int": int,
    "float": float,
    "str": str,
    "bool": bool,
    "list": list,
    "dict": dict,
    "tuple": tuple,
    "set": set,
    "print": print,
    "enumerate": enumerate,
    "zip": zip,
    "sorted": sorted,
    "True": True,
    "False": False,
    "None": None
}

def execute_code_safely(
    code_str: str,
    df: pd.DataFrame,
    timeout_seconds: int = EXECUTION_TIMEOUT_SECONDS
) -> Tuple[bool, Any, str, Optional[str]]:
    """
    Executes AST-validated code against a copy of the DataFrame within a restricted namespace.
    
    Returns:
        (success: bool, raw_result: Any, formatted_output: str, error_message: Optional[str])
    """
    if df is None:
        return False, None, "", "Execution error: No active DataFrame provided."

    # Prepare isolated environment
    # Use copy of df to preserve immutability of session state
    df_sandbox = df.copy()

    local_scope: Dict[str, Any] = {
        "df": df_sandbox,
        "pd": pd,
        "np": np,
        "result": None
    }
    global_scope: Dict[str, Any] = {
        "__builtins__": SAFE_BUILTINS
    }

    stdout_capture = io.StringIO()
    exception_holder = [None]
    exec_finished = threading.Event()

    def target_runner():
        old_stdout = sys.stdout
        try:
            sys.stdout = stdout_capture
            # Execute compiled code object
            exec(code_str, global_scope, local_scope)
        except Exception as ex:
            exception_holder[0] = ex
        finally:
            sys.stdout = old_stdout
            exec_finished.set()

    thread = threading.Thread(target=target_runner, daemon=True)
    thread.start()

    # Wait for completion or timeout
    finished = exec_finished.wait(timeout=timeout_seconds)

    if not finished:
        return False, None, "", f"Execution Timeout: Code exceeded maximum allowed run time ({timeout_seconds}s)."

    if exception_holder[0] is not None:
        err = exception_holder[0]
        return False, None, "", f"Runtime {type(err).__name__}: {str(err)}"

    # Retrieve output
    captured_stdout = stdout_capture.getvalue()
    raw_result = local_scope.get("result")

    # If 'result' was not explicitly assigned, check if stdout has output or fallback to last expression
    if raw_result is None and captured_stdout.strip():
        raw_result = captured_stdout.strip()

    # Format result for UI presentation
    formatted_output = ""
    if isinstance(raw_result, (pd.DataFrame, pd.Series)):
        if isinstance(raw_result, pd.Series):
            df_res = raw_result.to_frame()
        else:
            df_res = raw_result
        if len(df_res) > MAX_OUTPUT_ROWS:
            formatted_output = f"Displaying first {MAX_OUTPUT_ROWS} rows of {len(df_res):,} total rows:\n" + df_res.head(MAX_OUTPUT_ROWS).to_string()
        else:
            formatted_output = df_res.to_string()
    elif raw_result is not None:
        formatted_output = str(raw_result)
    elif captured_stdout:
        formatted_output = captured_stdout
    else:
        formatted_output = "Code executed successfully with no return value."

    # Truncate if output text is excessively large
    if len(formatted_output) > MAX_OUTPUT_CHARS:
        formatted_output = formatted_output[:MAX_OUTPUT_CHARS] + "\n... [Output truncated due to size limit]"

    return True, raw_result, formatted_output, None
