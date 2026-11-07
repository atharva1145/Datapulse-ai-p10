"""
Centralized Configuration and Settings for CSV INSIGHT AI (P10)
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env if present
load_dotenv()

# Base Paths
BASE_DIR = Path(__file__).resolve().parent.parent
SAMPLE_DATA_DIR = BASE_DIR / "datasets" / "sample_data"
ASSETS_DIR = BASE_DIR / "assets"
DOCS_DIR = BASE_DIR / "docs"

# Application Metadata
APP_NAME = "CSV INSIGHT AI"
APP_SUBTITLE = "AI-Powered Dataset Intelligence & Machine Learning Recommendation Platform"
STUDENT_NAME = "Atharva Shelar"
ROLL_NUMBER = "10"
COURSE_NAME = "Generative AI"
ACADEMIC_YEAR = "2026-2027"

# Gemini LLM Settings
# Centralized model references so upgrading models never breaks individual modules
GEMINI_MODEL_TEXT = os.getenv("GEMINI_MODEL_TEXT", "gemini-2.5-flash")
GEMINI_MODEL_VISION = os.getenv("GEMINI_MODEL_VISION", "gemini-2.5-flash")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Embedding Settings
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
DEFAULT_SIMILARITY_THRESHOLD = 0.65

# CTGAN & Resource Limits
MAX_UPLOAD_SIZE_MB = 15
DEFAULT_CTGAN_EPOCHS = 20
MAX_CTGAN_TRAINING_ROWS = 600  # Cap training slice on CPU to ensure sub-minute synthesis

# Safe Execution Sandbox Limits
EXECUTION_TIMEOUT_SECONDS = 5
MAX_OUTPUT_ROWS = 50
MAX_OUTPUT_CHARS = 4000

# Supported Public Benchmark Datasets
SAMPLE_DATASETS = {
    "Iris Flower Dataset": {
        "filename": "iris.csv",
        "description": "Multiclass classification benchmark (150 records, 4 features, 3 species)",
        "task_type": "Multiclass Classification / Clustering"
    },
    "Titanic Survival Dataset": {
        "filename": "titanic.csv",
        "description": "Mixed numerical/categorical with missing values and class imbalance (891 records)",
        "task_type": "Binary Classification / Imbalanced Learning"
    },
    "Wine Quality Dataset": {
        "filename": "winequality_red.csv",
        "description": "Continuous physicochemical properties predicting wine quality (1599 records)",
        "task_type": "Regression / Continuous Ranking"
    }
}
