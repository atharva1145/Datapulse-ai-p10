"""
Unit tests for modules/data_loader.py
Student: Atharva Shelar (Roll No: 10)
"""

import io
import pytest
from pathlib import Path
from modules.data_loader import load_csv, sniff_delimiter
from config.settings import SAMPLE_DATA_DIR

def test_sniff_delimiter():
    comma_sample = "id,name,age\n1,Alice,20\n2,Bob,25"
    semi_sample = "id;name;age\n1;Alice;20\n2;Bob;25"
    tab_sample = "id\tname\tage\n1\tAlice\t20"
    
    assert sniff_delimiter(comma_sample) == ","
    assert sniff_delimiter(semi_sample) == ";"
    assert sniff_delimiter(tab_sample) == "\t"

def test_load_sample_iris():
    iris_path = SAMPLE_DATA_DIR / "iris.csv"
    assert iris_path.exists(), "iris.csv should exist in sample_data directory"
    
    df, meta, err = load_csv(iris_path)
    assert err is None
    assert df is not None
    assert meta["row_count"] == 150
    assert meta["col_count"] == 5
    assert "species" in meta["columns"]

def test_load_sample_titanic():
    titanic_path = SAMPLE_DATA_DIR / "titanic.csv"
    assert titanic_path.exists(), "titanic.csv should exist in sample_data directory"
    
    df, meta, err = load_csv(titanic_path)
    assert err is None
    assert df is not None
    assert meta["row_count"] == 891
    assert "Survived" in meta["columns"]
    assert "Age" in meta["columns"]

def test_load_sample_wine():
    wine_path = SAMPLE_DATA_DIR / "winequality_red.csv"
    assert wine_path.exists(), "winequality_red.csv should exist in sample_data directory"
    
    df, meta, err = load_csv(wine_path)
    assert err is None
    assert df is not None
    assert meta["row_count"] == 1599
    assert meta["col_count"] == 12

def test_empty_csv():
    empty_stream = io.BytesIO(b"")
    df, meta, err = load_csv(empty_stream)
    assert df is None
    assert "empty" in err.lower()

def test_nonexistent_file():
    df, meta, err = load_csv("non_existent_file_xyz123.csv")
    assert df is None
    assert "does not exist" in err.lower()

def test_bytes_io_stream():
    csv_bytes = b"feature1,feature2,target\n1.2,3.4,A\n5.6,7.8,B"
    stream = io.BytesIO(csv_bytes)
    df, meta, err = load_csv(stream)
    assert err is None
    assert df is not None
    assert meta["row_count"] == 2
    assert meta["col_count"] == 3
