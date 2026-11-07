---
title: CSV Dataset Insight P10
emoji: 📊
colorFrom: indigo
colorTo: purple
sdk: streamlit
sdk_version: "1.67.0"
app_file: app.py
pinned: false
license: mit
---

# CSV INSIGHT AI (P10)
### AI-Powered Dataset Intelligence & Machine Learning Recommendation Platform

**Student:** Atharva Shelar | **Roll No:** 10 | **Class:** AIA-3 [LY]  
**Academic Subject:** Generative AI Continuous Assessment (P10)  
**Institution:** MIT ADT University, Pune  
**Live Application:** [Hugging Face Space](https://huggingface.co/spaces/atharva-shelar/csv-dataset-insight-p10) | **Repository:** [GitHub](https://github.com/atharva-shelar/csv-dataset-insight-p10)  

---

## 1. Problem Statement & Objectives

### Goal:
**Profile any uploaded CSV and recommend the right ML task and next steps.**

### The Five Mandatory Practical Tasks:
- **U1 – Column Distributions & Lifecycle:** Plot interactive histograms, box plots, categorical frequencies, and correlation heatmaps; recommend learning type (Supervised vs. Unsupervised) and dynamically map a 10-stage ML lifecycle.
- **U2 – LLM + Pandas Data Assistant:** Natural language query answering; LLM synthesizes Pandas code which is validated through a strict AST allowlist, executed in a sandboxed namespace, and explained in plain English.
- **U3 – BERT Embeddings & Vision LLM:** Generate 384-dimensional dense semantic column descriptions using Sentence-BERT (`all-MiniLM-L6-v2`), compute pairwise cosine similarity clusters, and employ Gemini Multimodal Vision to visually interpret distribution charts.
- **U4 – PyTorch CTGAN Tabular Synthesis:** Generate synthetic rows using Conditional GANs; evaluate fidelity using two-sample Kolmogorov-Smirnov (KS) tests, Jensen-Shannon divergence, and correlation preservation.
- **U5 – Responsible AI Guardrails:** Flag sensitive personal attributes (PII), analyze target class imbalance with Accuracy Paradox guidance, and run an empirical hallucination/bias test bench with documented failure cases.

---

## 2. Five Common Syllabus Layers (Units I–V)

1. **Unit I – Foundations of Generative AI:** Generative vs. Discriminative AI comparison matrix; Zero-shot vs. Few-shot vs. Structured prompting comparison; Empirical class probability distribution visualizer grounded in actual data frequencies.
2. **Unit II – GANs and LLMs:** Core reasoning powered by Google Gemini 2.5 Flash; Self-attention mechanism ($Softmax(QK^T / \sqrt{d_k})V$) educational visualizer; Prompt-based learning vs. Fine-tuning vs. Tabular GAN comparative matrix.
3. **Unit III – GPT, BERT and Multimodal AI:** Architectural contrast between Autoregressive Causal Decoders (GPT-2 baseline) and Masked Bidirectional Encoders (Sentence-BERT); Gemini Vision multimodal chart reader.
4. **Unit IV – Generative AI Tools & Techniques:** Python 3.12 + PyTorch integration for CTGAN; Generative AI visual infographic card synthesizer (900×520px) documenting diffusion models and licenses.
5. **Unit V – Responsible AI:** Multi-tier AST security sandbox; PII regex detection; Target class imbalance analyzer; Empirical bias/hallucination test bench on 6 standardized queries with documented failure cases; Standardized `MODEL_CARD.md`.

---

## 3. Technology Stack

| Layer | Component / Library | Role & Justification |
| :--- | :--- | :--- |
| **Runtime & Language** | Python 3.12 / 3.11 | Modern typing, high-performance data manipulation. |
| **Frontend Framework** | Streamlit (v1.67+) | Responsive multi-page SaaS dashboard, reactive session states. |
| **Data Science Core** | Pandas, NumPy, SciPy | In-memory dataframes, matrix operations, Kolmogorov-Smirnov test. |
| **Interactive Visuals** | Plotly & Seaborn/Matplotlib | Plotly browser charts; Matplotlib in-memory buffer for Vision API. |
| **Central LLM & Vision** | Google Gemini 2.5 Flash | Structured reasoning, Pandas code generation, vision chart interpretation. |
| **Semantic Embeddings** | Sentence-BERT (`all-MiniLM-L6-v2`) | 384-d dense vector embeddings & pairwise cosine similarity grouping. |
| **Tabular GAN** | PyTorch & SDV CTGAN | Conditional Generative Adversarial Network for mixed continuous/discrete data. |
| **Security Sandbox** | Python `ast` (Abstract Syntax Tree) | Enforces operation allowlist; strictly blocks imports, file writes, and eval. |
| **PDF Reporting** | ReportLab (v5.1+) | Programmatic compilation of `10_Atharva_Shelar_P10.pdf`. |

---

## 4. System Architecture

```
[Uploaded CSV File / Sample Dataset]
                │
                ▼
  ┌─────────────────────────────┐
  │  Data Loader & Sanitizer    │ (Sniffs delimiter, validates encoding, enforces size limits)
  └─────────────┬───────────────┘
                │
                ▼
  ┌─────────────────────────────┐
  │ Data Profiler & Health Scorer│ ──> Quality Score = 100 - (P_missing + P_dupes + P_const + P_outliers)
  └─────────────┬───────────────┘
                │
   ┌────────────┴─────────────┬──────────────────────────┬────────────────────────┐
   ▼                          ▼                          ▼                        ▼
[U1: Visuals & ML]     [U2: AI Assistant]         [U3: Column Intel]       [U4: CTGAN Lab]
- Histograms / Box     - Gemini 2.5 Flash         - Sentence-BERT 384-d    - PyTorch CTGAN
- Correlation Matrix   - AST Code Validator       - Cosine Similarity      - Two-sample KS Test
- Task Recommender     - Isolated Local Sandbox   - Gemini Vision Reader   - Correlation Delta
- 10-Stage Lifecycle   - Plain-English Output     - GPT vs BERT Matrix     - Generative Infographic
   │                          │                          │                        │
   └──────────────────────────┼──────────────────────────┴────────────────────────┘
                              │
                              ▼
               ┌───────────────────────────────┐
               │ U5: Responsible AI Guardrails │
               │ - Sensitive PII Regex Scanner │
               │ - Class Imbalance Analyzer    │
               │ - Hallucination Test Bench    │
               └──────────────┬────────────────┘
                              │
                              ▼
               ┌───────────────────────────────┐
               │    Exportable Deliverables    │
               │ • 10_Atharva_Shelar_P10.pdf   │
               │ • MODEL_CARD.md               │
               │ • Public Deployment           │
               └───────────────────────────────┘
```

---

## 5. Three Public Benchmark Datasets

The application comes pre-loaded with three public benchmark datasets and supports custom CSV uploads:

| Dataset Name | Domain | Rows & Cols | Primary Task Formulation | Quality Score | Imbalance Ratio | Mean KS Stat |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Iris Flower** | Botanical | 150 rows × 5 cols | Multiclass Classification | **99.0 / 100** | 1.0 : 1 (Balanced) | **0.362** |
| **Titanic Survival** | Maritime Demographics | 891 rows × 12 cols | Binary Classification | **90.5 / 100** | 1.61 : 1 (Mild) | **0.281** |
| **Wine Quality (Red)** | Physicochemical | 1,599 rows × 12 cols | Regression / Ranking | **83.4 / 100** | 68.1 : 1 (Severe) | **0.276** |

---

## 6. Installation & Local Execution

### 1. Clone the Repository
```bash
git clone https://github.com/atharva-shelar/csv-dataset-insight-p10.git
cd csv-dataset-insight-p10
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (Optional)
Copy `.env.example` to `.env` and configure your free Gemini API key:
```bash
cp .env.example .env
```
Edit `.env`:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```
*(Note: If no API key is provided, the application automatically runs in deterministic offline mode with 100% feature functionality!)*

### 5. Launch the Streamlit Dashboard
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 7. Automated Testing & Verification

Run the full automated pytest suite (40 unit and integration tests):
```bash
pytest tests/ -v
```
To run the automated multi-dataset benchmark across Iris, Titanic, and Wine Quality:
```bash
python tests/benchmark_three_datasets.py
```

---

## 8. Deployment Guide

### Deployment on Hugging Face Spaces (Recommended):
1. Create a new Space on [Hugging Face](https://huggingface.co/new-space).
2. Select **Streamlit** SDK and choose **Public**.
3. Push this repository to your Space repository:
   ```bash
   git remote add space https://huggingface.co/spaces/YOUR_USERNAME/csv-dataset-insight-p10
   git push space main
   ```
4. In Space Settings $\rightarrow$ **Variables and secrets**, add `GEMINI_API_KEY`.
5. Hugging Face Spaces will automatically build the environment from `requirements.txt` and launch `app.py`.

### Deployment on Streamlit Community Cloud:
1. Push this repository to your public GitHub account.
2. Sign in to [share.streamlit.io](https://share.streamlit.io/).
3. Click **"New app"**, select `atharva-shelar/csv-dataset-insight-p10`, set Main file path to `app.py`.
4. In **Advanced settings**, add `GEMINI_API_KEY` under Secrets.
5. Click **Deploy**!

---

## 9. Measurable Evaluation & Documented Failure Cases

### Key Measurable Findings:
1. **Deterministic Quality Scoring:** Correctly differentiated between clean data (Iris: 99.0/100) and data with missing values and outliers (Titanic: 90.5/100, Wine: 83.4/100).
2. **Tabular Distribution Fidelity:** PyTorch CTGAN achieved an average Kolmogorov-Smirnov statistic of $0.276 - 0.362$ across continuous features.
3. **AST Safety Interception:** Adversarial system call attempts (`import os`, `subprocess`, `open`) achieved a **100% block rate**.

### Documented Failure Cases:
1. **Rare Category Collapse in Small Batches:** Low-frequency discrete categories in small sample batches can experience slight probability distortion during GAN training. *Mitigation: Minimum batch size bounds and frequency warnings.*
2. **Continuous Integer Disambiguation:** Continuous targets with discrete integer ratings (e.g. Wine Quality) can initially resemble multiclass targets. *Mitigation: Added cardinality-to-row ratio checks to enforce Regression.*
3. **Adversarial Code Injection:** When queries prompted writing files to disk (`df.to_csv()`), the AST visitor intercepted the attribute and safely rejected execution.

---

## 10. License

This project is open-source and licensed under the [MIT License](LICENSE).
Model and dataset documentation is available in [MODEL_CARD.md](MODEL_CARD.md).
