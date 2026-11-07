"""
Module: Data Loader & Sanitizer
Student: Atharva Shelar (Roll No: 10)
Handles robust CSV loading, encoding fallbacks, delimiter sniffing, and validation.
"""

import io
import os
from pathlib import Path
from typing import Tuple, Optional, Dict, Any, Union
import pandas as pd

def sniff_delimiter(sample_text: str) -> str:
    """Sniffs the most probable delimiter from a text sample."""
    delimiters = [',', ';', '\t', '|']
    counts = {d: sample_text.count(d) for d in delimiters}
    # Delimiter with highest frequency in first few lines
    best_delim = max(counts, key=counts.get)
    return best_delim if counts[best_delim] > 0 else ','

def load_csv(
    file_input: Union[str, Path, io.BytesIO, Any],
    delimiter: Optional[str] = None,
    encoding: Optional[str] = None,
    max_size_mb: int = 25
) -> Tuple[Optional[pd.DataFrame], Dict[str, Any], Optional[str]]:
    """
    Safely loads a CSV file with automatic delimiter sniffing and encoding fallbacks.
    
    Returns:
        (df, metadata_dict, error_message)
    """
    metadata: Dict[str, Any] = {
        "filename": "uploaded_data.csv",
        "file_size_kb": 0.0,
        "row_count": 0,
        "col_count": 0,
        "columns": [],
        "dtypes": {},
        "delimiter_used": ",",
        "encoding_used": "utf-8"
    }

    raw_bytes = None
    filename = "dataset.csv"

    # 1. Extract bytes and filename
    try:
        if isinstance(file_input, (str, Path)):
            path = Path(file_input)
            filename = path.name
            if not path.exists():
                return None, metadata, f"File does not exist: {path}"
            file_size = path.stat().st_size
            if file_size == 0:
                return None, metadata, "The provided CSV file is completely empty (0 bytes)."
            with open(path, "rb") as f:
                raw_bytes = f.read()
        elif hasattr(file_input, "read"):
            if hasattr(file_input, "name"):
                filename = file_input.name
            raw_bytes = file_input.read()
            # Reset seek position if seekable
            if hasattr(file_input, "seek"):
                file_input.seek(0)
            file_size = len(raw_bytes)
            if file_size == 0:
                return None, metadata, "The uploaded file is empty (0 bytes)."
        else:
            return None, metadata, "Unsupported input type for CSV loader."

        metadata["filename"] = filename
        metadata["file_size_kb"] = round(file_size / 1024, 2)

        # File size guardrail
        if (file_size / (1024 * 1024)) > max_size_mb:
            return None, metadata, f"File size ({metadata['file_size_kb']} KB) exceeds maximum limit of {max_size_mb} MB."

    except Exception as e:
        return None, metadata, f"Error reading file stream: {str(e)}"

    # 2. Encoding fallback sequence
    encodings_to_try = [encoding] if encoding else ["utf-8", "utf-8-sig", "latin1", "cp1252", "iso-8859-1"]
    decoded_text = None
    successful_encoding = None

    for enc in encodings_to_try:
        if not enc:
            continue
        try:
            decoded_text = raw_bytes.decode(enc)
            successful_encoding = enc
            break
        except (UnicodeDecodeError, LookupError):
            continue

    if decoded_text is None:
        return None, metadata, "Failed to decode CSV using UTF-8 or standard Latin fallbacks."

    metadata["encoding_used"] = successful_encoding

    # 3. Delimiter detection
    if not delimiter or delimiter == "auto":
        sample = "\n".join(decoded_text.splitlines()[:10])
        delimiter = sniff_delimiter(sample)

    metadata["delimiter_used"] = delimiter

    # 4. Parse DataFrame
    try:
        df = pd.read_csv(io.StringIO(decoded_text), sep=delimiter)
        
        if df.empty:
            return None, metadata, "CSV contains valid headers but zero data rows."

        # Clean column names (strip whitespace)
        df.columns = [str(c).strip() for c in df.columns]

        metadata["row_count"] = int(len(df))
        metadata["col_count"] = int(len(df.columns))
        metadata["columns"] = list(df.columns)
        metadata["dtypes"] = {col: str(dtype) for col, dtype in df.dtypes.items()}

        return df, metadata, None

    except pd.errors.EmptyDataError:
        return None, metadata, "CSV file contains no readable columns or rows."
    except pd.errors.ParserError as pe:
        return None, metadata, f"CSV parsing error: {str(pe)}. Check delimiter or malformed rows."
    except Exception as ex:
        return None, metadata, f"Unexpected error parsing CSV: {str(ex)}"
