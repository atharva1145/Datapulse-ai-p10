# System Architecture Blueprint: DataPulse AI (P10)
**Project Title:** CSV Dataset Insight & Task Recommender  
**Student:** Atharva Shelar (Roll No: 10)  
**Subject:** Generative AI  

---

## 1. High-Level System Architecture

```
[User Browser]
      │
      ▼
[Streamlit Frontend (app.py + pages/)]
      │
      ├───────────────────┬───────────────────┬───────────────────┐
      ▼                   ▼                   ▼                   ▼
[Data Ingestion]    [Analytics Engine]  [Generative AI]     [Responsible AI]
- Encoding Sniff    - Data Profiler     - Gemini 2.5 API    - PII Regex Scanner
- Delimiter Detect  - Health Scorer     - Sentence-BERT     - Imbalance Engine
- Size Limits       - Heuristic Recomm. - PyTorch CTGAN     - AST Code Sandbox
- Sample Data       - Plotly / Matplot  - Visual Infographic- Benchmarking
```

---

## 2. Component Directory Specification

```
CSV-Dataset-Insight-P10/
├── app.py                         # Streamlit multi-page controller
├── requirements.txt               # Pinned dependencies
├── README.md                      # Academic documentation & deployment guide
├── MODEL_CARD.md                  # Standardized model card
├── LICENSE                        # MIT Open Source License
├── .gitignore                     # Git exclusions (.env, caches)
├── .env.example                   # Environment variable template
│
├── config/
│   └── settings.py                # Centralized configurations, limits & models
│
├── modules/
│   ├── data_loader.py             # Delimiter sniffing, encoding fallbacks, size checks
│   ├── data_profiler.py           # Descriptive stats, missingness & quality scoring
│   ├── visualization.py           # Plotly interactive & Matplotlib static buffers
│   ├── ml_recommender.py          # Deterministic ML task & algorithm heuristics
│   ├── lifecycle.py               # 10-stage ML lifecycle guide & GenAI comparison
│   ├── llm_assistant.py           # Gemini LLM bridge, prompting benchmarks, attention
│   ├── code_validator.py          # AST syntax visitor allowlist & exploit blocker
│   ├── safe_executor.py           # Sandboxed code execution with timeout
│   ├── embeddings.py              # Sentence-BERT embeddings & cosine clustering
│   ├── vision_analyzer.py         # Multimodal Gemini Vision chart interpreter
│   ├── ctgan_generator.py         # PyTorch CTGAN tabular synthesizer
│   ├── synthetic_evaluator.py     # Real vs. synthetic KS-test, JS-div, correlation MAE
│   ├── image_generator.py         # Generative AI visual infographic card synthesis
│   ├── responsible_ai.py          # PII scanner, imbalance analyzer, hallucination bench
│   └── report_generator.py        # PDF compiler for 10_Atharva_Shelar_P10.pdf
│
├── pages/
│   ├── 1_Dashboard.py             # KPIs, Quality Score gauge, missing value chart
│   ├── 2_Visual_Analytics.py      # Univariate & bivariate distributions, heatmaps
│   ├── 3_ML_Recommendations.py   # Task recommendations & 10-stage lifecycle
│   ├── 4_AI_Data_Assistant.py     # Natural language query, code generation, AST check
│   ├── 5_Column_Intelligence.py   # S-BERT clustering & Gemini Vision chart reader
│   ├── 6_Synthetic_Data_Lab.py    # CTGAN tabular synthesis & KS evaluation
│   ├── 7_Responsible_AI.py        # PII audit, class imbalance, test bench
│   └── 8_Final_Report.py          # Cross-dataset summary & PDF export
│
├── datasets/sample_data/
│   ├── iris.csv                   # Public Dataset 1 (Multiclass Classification)
│   ├── titanic.csv                # Public Dataset 2 (Binary Imbalance Classification)
│   └── winequality_red.csv        # Public Dataset 3 (Continuous Regression)
│
├── tests/                         # Comprehensive pytest regression suite (40+ tests)
└── docs/
    ├── architecture.md            # System blueprint
    ├── evaluation.md              # Cross-dataset empirical benchmark records
    └── demo_script.md             # 2-3 minute timed presentation script
```

---

## 3. Defense-in-Depth Security Protocol

```
[LLM Code Output]
       │
       ▼
[AST Syntax Visitor (code_validator.py)]
       │
       ├── Disallowed node detected? (import, open, eval, exec, socket, to_csv)
       │         └── YES ──> [Reject Code + Output Violation Message]
       │
       └── NO (Passes allowlist)
                 │
                 ▼
[Restricted Local Execution (safe_executor.py)]
       │
       ├── Immutable df copy in isolated dict
       ├── Strict thread timeout (5 seconds)
       └── Stdout buffer capture
```
