# MODEL & DATASET CARD: CSV INSIGHT AI (P10)
**Project Title:** CSV Dataset Insight & Task Recommender  
**Student:** Atharva Shelar (Roll No: 10)  
**Academic Subject:** Generative AI  
**Repository:** `csv-dataset-insight-p10`  
**Date:** November 2026  

---

## 1. Model Details

### 1.1 Core Generative AI Models Integrated

| Model Name | Developer / Source | Architecture Type | Parameters / Size | Primary Role in Project | License |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Gemini 2.5 Flash** | Google DeepMind | Decoder-Only Transformer (Multimodal) | Proprietary (API) | Natural language dataset query translation, Pandas code synthesis, plain-English output explanation, and visual chart interpretation. | Google API Terms of Service |
| **Sentence-BERT (`all-MiniLM-L6-v2`)** | Hugging Face / UKPLab | Bidirectional Transformer Encoder | 22.7M params (384-dim, ~80MB) | Enriched column description embeddings and semantic cosine similarity clustering. | Apache 2.0 |
| **CTGAN** | SDV / MIT Data to AI Lab | Conditional GAN (PyTorch) | Generator: (128, 128), Discriminator: (128, 128) | Synthetic tabular record generation with continuous variational Gaussian Mixture modeling. | MIT License |
| **GPT-2 Baseline** | OpenAI / Hugging Face | Autoregressive Causal Decoder | 124M params | Educational contrast against bidirectional BERT models in Unit III syllabus. | Modified MIT |

---

## 2. Intended Use

### 2.1 Primary Intended Uses
- Automated profiling and data quality scoring for tabular CSV datasets.
- Deterministic heuristic recommendation of appropriate machine learning tasks (Supervised Classification/Regression, Unsupervised Clustering/PCA) and 10-stage ML lifecycles.
- Safe natural-language interrogation of tabular datasets via AST-validated Pandas execution.
- Automated semantic grouping of dataset attributes to identify potential multicollinearity, redundant features, or schema alignment targets.
- Privacy-conscious synthetic tabular data generation for data sharing and software testing.

### 2.2 Out-of-Scope & Prohibited Uses
- Executing unvalidated or arbitrary shell/operating system commands.
- Sending unmasked protected health information (PHI) or classified government records to external cloud APIs.
- Relying on synthetic tabular data as proof of mathematical differential privacy without additional epsilon-delta guarantees.
- Autonomous automated decision-making in high-stakes domains (e.g. credit denial, medical diagnosis) without human-in-the-loop review.

---

## 3. Reference Datasets & Provenance

The system is evaluated and benchmarked on three verified public datasets:

| Dataset Name | Source / Creator | Records & Columns | Task Formulation | License / Terms |
| :--- | :--- | :--- | :--- | :--- |
| **Iris Flower Dataset** | R.A. Fisher / UCI ML Repository | 150 rows, 5 features | Multiclass Classification (3 species) / Clustering | Public Domain (CC0) |
| **Titanic Survival Dataset** | Kaggle / Encyclopedia Titanica | 891 rows, 12 features | Binary Imbalanced Classification / PII Audit | Open Database / Public |
| **Wine Quality (Red)** | P. Cortez et al. / UCI ML Repository | 1,599 rows, 12 features | Continuous Regression / Quality Ranking | Creative Commons Attribution 4.0 |

---

## 4. Factors, Biases & Ethical Considerations

### 4.1 Identified Risks & Biases
- **Class Imbalance Distortion (The Accuracy Paradox):** In datasets where one class severely dominates (e.g. non-survivors in Titanic or rare wine quality scores), raw classification accuracy can create false confidence. The system flags this condition and mandates PR-AUC and Macro-F1 evaluation.
- **Sensitive Column Exposure (PII):** Raw tabular datasets frequently contain personal names, email addresses, phone numbers, or demographic indicators. The system implements regex and heuristic scanning to alert users before model training.
- **Membership Inference in Tabular GANs:** While CTGAN generates synthetic records rather than copying real ones, conditional GANs trained for high epochs on tiny datasets risk mode collapse or memorizing outlier clusters. The system enforces conservative epoch controls and provides Kolmogorov-Smirnov distribution comparison.

---

## 5. Security & Safety Guardrails

1. **AST Syntax Tree Filter:** Multi-tier AST visitor parses all LLM-generated code prior to runtime. Strictly blocks `import`, disk I/O, `eval`, `exec`, and network sockets.
2. **Restricted Local Execution:** Code executes inside an isolated scope containing only an immutable copy of the DataFrame, Pandas, NumPy, and safe math primitives.
3. **Execution Timeout:** Thread-based timeout (5 seconds) prevents infinite loops or CPU exhaustion.
4. **Context Sanitization:** Prompts sent to external LLMs contain only column names, data types, and truncated sample values; raw private tables are never transmitted.

---

## 6. Evaluation Metrics & Benchmark Standards

- **Tabular Distribution Fidelity:** Two-sample Kolmogorov-Smirnov (KS) test ($D_{\text{KS}} \le 0.20$ represents high fidelity) and Jensen-Shannon (JS) divergence.
- **Code Execution Safety:** 100% AST interception rate on adversarial injection queries.
- **Query Correctness:** Tested against standardized ground-truth mathematical questions (row count, column count, missing value totals).

---

## 7. Model Card Authors & Contact

- **Student Author:** Atharva Shelar (Roll No: 10, Class: AIA-3 [LY])
- **Course:** Generative AI Continuous Assessment (P10)
- **Institution:** MIT ADT University, Pune
