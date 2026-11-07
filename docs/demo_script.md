# 2–3 Minute Demonstration Video Script: DataPulse AI (P10)
**Project Title:** DataPulse AI – Autonomous CSV Dataset Insight & Task Recommender  
**Student Name:** Atharva Shelar  
**Roll Number:** 10 | **Class:** AIA-3 [LY]  
**Subject:** Generative AI Continuous Assessment  
**Target Duration:** 2 minutes 30 seconds (150 seconds)  

---

## 🎬 Recording Setup
- **Screen Resolution:** 1080p (Full Screen Browser on `http://localhost:8501`)
- **Recording Tool:** Windows Snipping Tool Screen Recorder (`Win + Shift + R`) or Xbox Game Bar (`Win + Alt + R`) or OBS Studio / Loom.
- **Audio:** Clear microphone audio.
- **Pre-flight Check:** Open `http://localhost:8501` in your browser with the default **Iris Flower Dataset** loaded.

---

## ⏱️ Timed Segment-by-Segment Script

### [0:00 – 0:15] Section 1: Introduction
- **What to Show on Screen:** Home page (`app.py`), showing the header: **DataPulse AI**, Problem P10.
- **What to Say:**
  > "Hello everyone, my name is Atharva Shelar, Roll Number 10. Today I am presenting DataPulse AI: an autonomous tabular dataset insight and machine learning recommendation platform for Continuous Assessment P10. The core objective of this application is to profile any uploaded tabular CSV dataset, recommend the appropriate machine learning task, and provide an enterprise-grade AI analytics pipeline covering all syllabus units."

---

### [0:15 – 0:35] Section 2: Dataset Upload & Profiling (Dashboard)
- **What to Show on Screen:** Navigate to **1_Dashboard**. Highlight the KPI cards (Rows, Columns, Missingness, Duplicates) and the **Data Quality Score** gauge (99.0/100).
- **What to Say:**
  > "Here on the Executive Dashboard, the system automatically computes dataset health metrics without any fabricated numbers. We see total records, attributes, and our transparent Data Quality Score formula, which evaluates missingness, duplicates, constant columns, and IQR outliers to provide a grounded health score of 99 out of 100 for the Iris dataset."

---

### [0:35 – 0:55] Section 3: Module U1 – Visual Analytics & ML Recommender
- **What to Show on Screen:** Navigate to **2_Visual_Analytics**, show the interactive histogram and correlation heatmap. Then switch to **3_ML_Recommendations** to show the suggested Multiclass Classification task and 10-stage ML Lifecycle.
- **What to Say:**
  > "In Module U1, we generate interactive Plotly histograms with marginal box plots and correlation heatmaps. In ML Recommendations, our deterministic heuristic engine identifies that the target column 'species' has three discrete categories, correctly recommending Supervised Multiclass Classification with algorithms like Random Forest and CatBoost, followed by a customized 10-stage machine learning lifecycle."

---

### [0:55 – 1:20] Section 4: Module U2 – AI Data Assistant & Safe Code Execution
- **What to Show on Screen:** Navigate to **4_AI_Data_Assistant**. Click the button **"Average of all columns"** and click **"Run AI Query"**. Highlight the generated Pandas code, the green **AST Security Check Passed** badge, the output table, and the plain-English explanation.
- **What to Say:**
  > "In Module U2, users can query their dataset in natural language. Powered by Gemini 2.5 Flash, the model synthesizes pure Pandas code. Crucially, before execution, the code passes through an Abstract Syntax Tree (AST) security validator that strictly blocks malicious imports, filesystem writes, and eval calls. The validated code runs inside a sandboxed namespace, and the LLM explains the analytical output in plain English."

---

### [1:20 – 1:40] Section 5: Module U3 – Sentence-BERT & Vision LLM
- **What to Show on Screen:** Navigate to **5_Column_Intelligence**. Adjust the **Cosine Similarity Threshold slider** on the S-BERT heatmap. Then click Tab 2 and click **"Analyze Chart with Vision LLM"**.
- **What to Say:**
  > "In Module U3, we use Sentence-BERT (`all-MiniLM-L6-v2`) to encode column names, data types, and non-sensitive sample values into 384-dimensional dense vectors to cluster semantically related columns. In Tab 2, our multimodal vision pipeline converts rendered distribution charts into memory buffers for Gemini Vision, which automatically identifies curve symmetry, central tendencies, and preprocessing advice."

---

### [1:40 – 2:00] Section 6: Module U4 – PyTorch CTGAN Synthetic Data Lab
- **What to Show on Screen:** Navigate to **6_Synthetic_Data_Lab**. Show the trained synthetic table, click Tab 2 to show the **Kolmogorov-Smirnov (KS) test** fidelity table and distribution overlay, and show the Generative Infographic in Tab 3.
- **What to Say:**
  > "In Module U4, we integrate PyTorch-compatible CTGAN for tabular synthetic data generation. Here we see our generated synthetic records and our empirical evaluation: Kolmogorov-Smirnov two-sample tests prove that synthetic continuous distributions closely match real data with low divergence. In Tab 3, we fulfill the Unit IV generative image requirement by synthesizing an illustrative dataset intelligence infographic card."

---

### [2:00 – 2:20] Section 7: Module U5 – Responsible AI Guardrails
- **What to Show on Screen:** In sidebar, switch dataset to **Titanic Survival Dataset**. Navigate to **7_Responsible_AI**. Show `Name` and `Sex` flagged as PII in Tab 1, and show the **Accuracy Paradox** imbalance ratio in Tab 2.
- **What to Say:**
  > "In Module U5, Responsible AI guardrails scan for sensitive personal information (PII). On the Titanic dataset, it immediately flags names and demographic attributes with anonymization recommendations. In Tab 2, it audits target class imbalance, alerting us to the 'Accuracy Paradox' where raw accuracy is misleading, mandating the use of Balanced Accuracy and Macro-F1 scores."

---

### [2:20 – 2:40] Section 8: Final Report & Conclusion
- **What to Show on Screen:** Navigate to **8_Final_Report**. Show the 3-dataset comparison table, click **"Download Official PDF Report"**, and show the downloaded `10_Atharva_Shelar_P10.pdf`.
- **What to Say:**
  > "Finally, in Module 8, we present our empirical cross-dataset comparison across Iris, Titanic, and Wine Quality, and compile our official 10-section academic PDF report directly from the live application. The project is completely open-source, tested with 40 automated unit tests, and ready for public cloud deployment. Thank you!"

---

## 💡 Quick Tips for Recording:
1. **Pacing:** Speak at a steady, confident pace. Don't rush.
2. **Cursor:** Use your mouse cursor deliberately to point at the key badges (e.g. AST Approved, Quality Score, KS Metric).
3. **Keep it under 3 minutes:** Following the script above will land your video right at approximately 2 minutes 20 seconds.
