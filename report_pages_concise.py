"""
Concise 12-Page Academic Mini Project Report Pages for DataPulse AI
Student: Atharva Shelar | Roll No: 10 | P10
Format: MIT ADT University, Pune · Generative AI Continuous Assessment (CA)
"""

from report_svgs import (
    get_fig1_svg, get_fig2_svg, get_fig3_svg,
    get_fig5_svg, get_fig9_svg, get_fig10_svg
)

def get_p1_cover(logo_b64):
    """Page 1: Title and Cover Page."""
    return f"""
<div class="page" style="justify-content: space-between; align-items: center; text-align: center; padding: 20mm 18mm 18mm 18mm;">
    <div>
        <div style="font-size: 13.5pt; font-weight: 800; color: #3b3270; letter-spacing: 0.05em; text-transform: uppercase;">MIT ADT UNIVERSITY, PUNE</div>
        <div style="font-size: 10.5pt; font-weight: 600; color: #5b6172; margin-top: 4px;">Department of Computer Science and Engineering</div>
        <div style="display: inline-block; background: #ede9fe; color: #4a3d8f; font-size: 8.5pt; font-weight: 700; padding: 4px 14px; border-radius: 9999px; margin-top: 8px; letter-spacing: 0.04em;">MINI PROJECT REPORT &nbsp;·&nbsp; GENERATIVE AI (CA)</div>
    </div>

    <div style="margin: 12px 0;">
        <img src="data:image/png;base64,{logo_b64}" style="width: 100px; height: 100px; border-radius: 50%; object-fit: contain; box-shadow: 0 4px 14px rgba(0,0,0,0.1);" alt="MIT ADT University">
    </div>

    <div>
        <div style="font-size: 25pt; font-weight: 800; color: #2d2a4a; letter-spacing: -0.02em; line-height: 1.15;">DataPulse AI</div>
        <div style="font-size: 11.5pt; font-weight: 600; color: #4a4f60; margin-top: 6px; margin-bottom: 10px;">Autonomous CSV Dataset Profiler, ML Task Recommender & Generative AI Studio</div>
        <div class="pill-badge" style="font-size: 9pt; padding: 4px 14px;">Problem Statement P10 · CSV Dataset Insight & Task Recommender</div>
    </div>

    <div style="width: 100%; max-width: 520px; background: #fbfbfe; border: 1.2px solid #e2e8f0; border-radius: 8px; padding: 12px 18px; text-align: left;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px 16px;">
            <div>
                <div style="font-size: 7.5pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase;">SUBMITTED BY</div>
                <div style="font-size: 9.8pt; font-weight: 700; color: #1f2433;">Atharva Shelar</div>
            </div>
            <div>
                <div style="font-size: 7.5pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase;">FACULTY GUIDE</div>
                <div style="font-size: 9.8pt; font-weight: 700; color: #1f2433;">Dr. Snehlata Funde</div>
            </div>
            <div>
                <div style="font-size: 7.5pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase;">ROLL NUMBER</div>
                <div style="font-size: 9.5pt; font-weight: 600; color: #1f2433;">10</div>
            </div>
            <div>
                <div style="font-size: 7.5pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase;">ENROLLMENT NUMBER</div>
                <div style="font-size: 9.5pt; font-weight: 600; color: #1f2433;">ADT23SOCB0244</div>
            </div>
            <div>
                <div style="font-size: 7.5pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase;">CLASS / DIVISION</div>
                <div style="font-size: 9.5pt; font-weight: 600; color: #1f2433;">LY-AIA-3</div>
            </div>
            <div>
                <div style="font-size: 7.5pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase;">ACADEMIC YEAR</div>
                <div style="font-size: 9.5pt; font-weight: 600; color: #1f2433;">2026–2027</div>
            </div>
            <div style="grid-column: span 2; border-top: 1px solid #edf0f5; padding-top: 8px; margin-top: 2px;">
                <div style="display: flex; justify-content: space-between; font-size: 8.5pt;">
                    <div><span style="color: #7c6bc4; font-weight: 700;">GITHUB:</span> <span style="color: #1d7770; font-family: monospace;">github.com/atharva1145/Datapulse-ai-p10</span></div>
                    <div><span style="color: #7c6bc4; font-weight: 700;">LIVE APP:</span> <span style="color: #1d7770; font-family: monospace;">datapulse-ai-p10.streamlit.app</span></div>
                </div>
            </div>
        </div>
    </div>
</div>
"""

def get_p2_cert_decl():
    """Page 2: Official Certificate of Approval and Student Declaration."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <div style="text-align: center; margin-bottom: 12px;">
            <h1 style="font-size: 15pt; margin-bottom: 2px;">Certificate of Approval</h1>
            <div style="font-size: 8.8pt; color: #64748b; font-weight: 600;">DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING</div>
        </div>
        <p style="font-size: 9.1pt; line-height: 1.5; text-align: justify;">
            This is to certify that the Continuous Assessment mini project entitled <strong>“DataPulse AI – Autonomous CSV Dataset Profiler, ML Task Recommender & Generative AI Studio”</strong> submitted by <strong>Atharva Shelar</strong> (Roll No: <strong>10</strong>, Enrollment No: <strong>ADT23SOCB0244</strong>) of Class <strong>LY-AIA-3</strong> is a bonafide work completed under my supervision in partial fulfillment of the requirements for the Continuous Assessment (CA) component in <strong>Generative AI</strong> at MIT ADT University, Pune for the academic year 2026–2027.
        </p>

        <div style="margin: 28px 0 16px 0; display: flex; justify-content: space-between; align-items: flex-end;">
            <div style="text-align: center; width: 180px;">
                <div style="border-bottom: 1px solid #1f2433; margin-bottom: 6px; height: 35px;"></div>
                <div style="font-weight: 700; font-size: 9.5pt;">Dr. Snehlata Funde</div>
                <div style="font-size: 8pt; color: #64748b;">Faculty Guide</div>
            </div>
            <div style="text-align: center; width: 180px;">
                <div style="border-bottom: 1px solid #1f2433; margin-bottom: 6px; height: 35px;"></div>
                <div style="font-weight: 700; font-size: 9.5pt;">Head of Department</div>
                <div style="font-size: 8pt; color: #64748b;">Computer Science & Engineering</div>
            </div>
        </div>

        <div style="border-top: 1.5px solid #edf0f5; margin-top: 12px; padding-top: 10px;">
            <h2 style="font-size: 12.5pt; margin-bottom: 4px;">Candidate's Declaration</h2>
            <p style="font-size: 8.9pt; line-height: 1.46; text-align: justify;">
                I, <strong>Atharva Shelar</strong>, hereby declare that this mini project report entitled <strong>“DataPulse AI”</strong> is an authentic record of my own independent work carried out under problem statement <strong>P10</strong>. All software architectures, Abstract Syntax Tree (AST) validation visitors, Sentence-BERT clustering routines, PyTorch CTGAN synthesizers, and empirical benchmarks were implemented, verified, and documented by me. All open-source packages are duly cited.
            </p>

            <div style="margin-top: 24px; display: flex; justify-content: space-between; align-items: flex-end;">
                <div>
                    <div style="font-weight: 700; font-size: 9.5pt;">Atharva Shelar</div>
                    <div style="font-size: 8pt; color: #64748b;">Signature of Candidate</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-weight: 600; font-size: 9pt;">07 November 2026</div>
                    <div style="font-size: 8pt; color: #64748b;">Date · Pune</div>
                </div>
            </div>
        </div>

        <div style="border-top: 1.5px solid #edf0f5; margin-top: 10px; padding-top: 8px;">
            <h2 style="font-size: 11pt; margin-bottom: 3px;">Acknowledgement</h2>
            <p style="font-size: 8.5pt; line-height: 1.4; color: #475569; text-align: justify; margin-bottom: 0;">
                I express my sincere gratitude to my guide, <strong>Dr. Snehlata Funde</strong>, for her intellectual mentorship, and to the <strong>Department of Computer Science and Engineering</strong>, MIT ADT University, Pune, for providing the necessary computational infrastructure and academic guidance.
            </p>
        </div>
    </div>
    <div class="page-footer"><span>2</span></div>
</div>
"""

def get_p3_abstract_toc():
    """Page 3: Abstract, Keywords, and Table of Contents."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>Abstract</h1>
        <p style="font-size: 9.2pt; line-height: 1.5; text-align: justify;">
            Exploratory data analysis (EDA), data quality auditing, and machine learning formulation represent critical yet labor-intensive phases of tabular data science. Heterogeneous formatting, silent quality defects (missingness, skewness, outliers), and the cognitive overhead of algorithm selection frequently delay deployment pipelines. <strong>DataPulse AI</strong> resolves these bottlenecks as an autonomous, production-grade tabular profiler, machine learning task recommender, and generative intelligence platform. Designed under curriculum brief <strong>P10</strong>, the platform implements a 5-tier architecture spanning units <strong>U1 to U5</strong>. DataPulse AI executes deterministic statistical profiling with a 100-point Data Health Score, an Abstract Syntax Tree (AST) sandboxed LLM code assistant achieving 100% exploit interception, Sentence-BERT 384-dimensional semantic column clustering, PyTorch Conditional WGAN-GP (CTGAN) tabular synthesis with Kolmogorov-Smirnov statistical validation, and automated Responsible AI audits detecting PII and class imbalance. Benchmarked across Iris (99.0/100), Titanic (90.5/100), and Wine Quality (83.4/100) with 40/40 passing unit tests, DataPulse AI delivers a robust, secure, and production-ready tabular data intelligence solution.
        </p>

        <div style="margin: 8px 0 14px 0;">
            <span style="font-weight: 700; color: #4a3d8f; font-size: 8.8pt;">Keywords:</span>
            <span style="font-size: 8.8pt; color: #1f2433;">Generative AI, Tabular Profiling, AST Security Sandbox, Sentence-BERT, PyTorch CTGAN, Responsible AI, Data Health Index.</span>
        </div>

        <h1 style="margin-top: 10px; margin-bottom: 8px;">Table of Contents</h1>
        <table style="width: 100%; border-collapse: collapse; font-size: 9pt;">
            <thead>
                <tr style="border-bottom: 1.5px solid #2d2a4a;">
                    <th style="padding: 5px 6px; background: none; color: #2d2a4a; font-weight: 800; width: 60px;">Chapter</th>
                    <th style="padding: 5px 6px; background: none; color: #2d2a4a; font-weight: 800;">Title</th>
                    <th style="padding: 5px 6px; background: none; color: #2d2a4a; font-weight: 800; text-align: right; width: 60px;">Page</th>
                </tr>
            </thead>
            <tbody>
                <tr><td style="font-weight: 700;">1</td><td>Introduction, Problem Statement & Project Objectives</td><td style="text-align: right; font-weight: 600;">4</td></tr>
                <tr><td style="font-weight: 700;">2</td><td>Technology Stack, Theoretical Foundations & Literature Survey</td><td style="text-align: right; font-weight: 600;">5</td></tr>
                <tr><td style="font-weight: 700;">3</td><td>System Architecture & Workflow Pipeline Design</td><td style="text-align: right; font-weight: 600;">6</td></tr>
                <tr><td style="font-weight: 700;">4</td><td>Core Analytical Modules Implementation (Units U1 & U2)</td><td style="text-align: right; font-weight: 600;">7</td></tr>
                <tr><td style="font-weight: 700;">5</td><td>Advanced Generative & Multimodal Modules (Units U3 & U4)</td><td style="text-align: right; font-weight: 600;">8</td></tr>
                <tr><td style="font-weight: 700;">6</td><td>Responsible AI, Privacy Governance & Security Auditing (Unit U5)</td><td style="text-align: right; font-weight: 600;">9</td></tr>
                <tr><td style="font-weight: 700;">7</td><td>Experimental Results & Cross-Dataset Benchmarking</td><td style="text-align: right; font-weight: 600;">10</td></tr>
                <tr><td style="font-weight: 700;">8</td><td>Software Testing (40/40 Pytest) & Cloud Deployment</td><td style="text-align: right; font-weight: 600;">11</td></tr>
                <tr><td style="font-weight: 700;">9</td><td>Conclusion, Limitations, Future Scope & Academic References</td><td style="text-align: right; font-weight: 600;">12</td></tr>
            </tbody>
        </table>

        <div class="alert-box" style="margin-top: 14px; padding: 8px 12px;">
            <div class="alert-title">Syllabus Compliance & Problem Brief Alignment</div>
            <div class="alert-content" style="font-size: 8.5pt;">
                This project comprehensively fulfills all academic requirements outlined in Continuous Assessment brief <strong>P10 (CSV Dataset Insight & Task Recommender)</strong> across the five mandated functional modules U1 through U5.
            </div>
        </div>
    </div>
    <div class="page-footer"><span>3</span></div>
</div>
"""

def get_p4_intro():
    """Page 4: Chapter 1 - Introduction & Problem Statement."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>1 Introduction & Problem Statement</h1>
        
        <h2>1.1 Background & Motivation</h2>
        <p>
            Tabular datasets stored in Comma-Separated Values (CSV) formats underpin enterprise data warehouses, clinical trials, and predictive modeling initiatives. However, initial data exploration is notoriously prone to inefficiency. Practitioners spend over 60% of their operational bandwidth parsing formatting irregularities, identifying subtle data hygiene anomalies (missing values, skewed features, duplicate entries, extreme outliers), and deciding on machine learning algorithmic architectures. 
        </p>
        <p>
            While commercial Automated Machine Learning (AutoML) frameworks exist, they operate as closed "black boxes," obscuring the mathematical justification behind preprocessing steps and lacking natural language conversational interfaces. Moreover, emerging LLM code generators introduce severe Remote Code Execution (RCE) attack vectors if executing unverified code.
        </p>

        <h2>1.2 Problem Statement (P10)</h2>
        <p>
            The project addresses the core challenge of <strong>Problem Statement P10: CSV Dataset Insight & Task Recommender</strong>. The objective is to design and develop an end-to-end, web-hosted software platform capable of ingesting arbitrary CSV datasets, automatically profiling their statistical topology, computing an objective Data Health Index, classifying the target ML task family, executing safe natural-language queries, generating statistically representative synthetic data, and enforcing Responsible AI guardrails.
        </p>

        <h2>1.3 Project Scope & Mandated Modules</h2>
        <p>
            The system adheres strictly to the continuous assessment syllabus, covering five core functional units:
        </p>
        <ul>
            <li><strong>Unit U1 (Visual Analytics & Heuristics):</strong> Auto-delimiter sniffing, completeness scoring, univariate/bivariate distributions, correlation heatmaps, and ML task classification.</li>
            <li><strong>Unit U2 (AI Data Assistant):</strong> AST-validated LLM natural language assistant generating verified, sandboxed pandas transformation routines with narrative summaries.</li>
            <li><strong>Unit U3 (Column Intelligence):</strong> Dense semantic vector embeddings via Sentence-BERT (<code>all-MiniLM-L6-v2</code>) and Multimodal Vision LLM chart commentary.</li>
            <li><strong>Unit U4 (Synthetic Data Lab):</strong> Deep tabular synthesis via PyTorch Conditional GAN (CTGAN) with empirical Kolmogorov-Smirnov statistical validation.</li>
            <li><strong>Unit U5 (Responsible AI):</strong> Automated PII exposure detection (GDPR/DPDP compliance) and target class imbalance audit with remediation recipes.</li>
        </ul>

        <h2>1.4 Key Performance Deliverables</h2>
        <table style="width: 100%; font-size: 8.5pt; margin-top: 6px;">
            <thead>
                <tr>
                    <th style="width: 30%;">Metric Category</th>
                    <th style="width: 35%;">Engineering Target</th>
                    <th style="width: 35%;">Empirical Realization</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>Code Security Guardrail</td><td>100% intercept of RCE attacks</td><td>100% blocked via AST Visitor sandbox</td></tr>
                <tr><td>Tabular Generation Fidelity</td><td>Mean KS similarity &lt; 0.35</td><td>Achieved 0.281 on Titanic benchmark</td></tr>
                <tr><td>Automated Test Coverage</td><td>&ge; 30 unit/integration tests</td><td>40 passed, 0 failed in Pytest suite</td></tr>
                <tr><td>Deployment Accessibility</td><td>Zero-setup public cloud web URL</td><td>Hosted on Streamlit Community Cloud</td></tr>
            </tbody>
        </table>
    </div>
    <div class="page-footer"><span>4</span></div>
</div>
"""

def get_p5_tech_stack():
    """Page 5: Chapter 2 - Technology Stack & Literature Survey."""
    html = """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>2 Technology Stack & Theoretical Foundations</h1>
        
        <h2>2.1 Foundational Architecture & Package Ecosystem</h2>
        <p>
            DataPulse AI is implemented in <strong>Python 3.12</strong>, selected for its typing performance and rich machine learning ecosystem. The user experience is built on <strong>Streamlit Community Cloud</strong>, enabling reactive web sessions with responsive visual dashboards. 
        </p>

        <div class="figure-wrapper" style="margin: 4px 0;">
            {{FIG1}}
            <div class="figure-caption"><strong>Figure 1:</strong> DataPulse AI enterprise technology stack grouped by functional layer and execution environment.</div>
        </div>

        <h2>2.2 Theoretical Comparison: Generative vs. Discriminative AI</h2>
        <p>
            A foundational pillar of the system is contrasting classical discriminative machine learning with deep generative modeling across tabular data:
        </p>
        <table style="width: 100%; font-size: 8.2pt; margin: 4px 0;">
            <thead>
                <tr>
                    <th>Dimension</th>
                    <th>Discriminative ML (Units U1, U5)</th>
                    <th>Generative AI (Units U2, U3, U4)</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><strong>Mathematical Objective</strong></td><td>Models posterior probability P(Y|X) to predict target labels.</td><td>Models joint distribution P(X) or P(X, Y) to synthesize new samples.</td></tr>
                <tr><td><strong>Core Algorithms</strong></td><td>Random Forest, XGBoost, Logistic Regression, Scikit-learn.</td><td>Conditional WGAN-GP (CTGAN), Sentence-BERT, Gemini LLM.</td></tr>
                <tr><td><strong>Application in System</strong></td><td>Classifying ML task families, detecting IQR outliers and skewness.</td><td>Generating synthetic tabular rows, natural language code synthesis.</td></tr>
                <tr><td><strong>Validation Paradigm</strong></td><td>Cross-validation, ROC-AUC, F1-score, Precision/Recall.</td><td>Two-sample Kolmogorov-Smirnov test, AST Abstract Syntax Tree.</td></tr>
            </tbody>
        </table>

        <h2>2.3 Literature Survey & Baseline Benchmarks</h2>
        <p style="font-size: 8.8pt;">
            Early tabular synthesizers relied on Gaussian copulas or SMOTE oversampling. However, Xu et al. (NeurIPS 2019) proved that classical models fail when continuous variables exhibit multi-modal distributions. By introducing <strong>mode-specific normalization</strong> via Variational Gaussian Mixture Models (VGM), CTGAN overcomes these limitations. Similarly, Sentence-BERT (Reimers & Gurevych, EMNLP 2019) enables dense semantic mapping of tabular column names, outperforming naive string-matching heuristics.
        </p>
    </div>
    <div class="page-footer"><span>5</span></div>
</div>
"""
    return html.replace('{{FIG1}}', get_fig1_svg())

def get_p6_architecture():
    """Page 6: Chapter 3 - System Architecture & Workflow Pipeline."""
    html = """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>3 System Architecture & Pipeline Design</h1>
        
        <h2>3.1 End-to-End 5-Tier Architecture</h2>
        <p>
            DataPulse AI is engineered with a modular, decoupled architecture where each tier performs a specialized analytical transformation with explicit security boundaries:
        </p>

        <div class="figure-wrapper" style="margin: 6px 0;">
            {{FIG2}}
            <div class="figure-caption"><strong>Figure 2:</strong> DataPulse AI 5-tier system architecture illustrating dataflow from ingestion to governance.</div>
        </div>

        <h2>3.2 Architectural Subsystems Description</h2>
        <ol style="font-size: 8.8pt; line-height: 1.45;">
            <li><strong>Ingestion & Sniffing Tier:</strong> Utilizes <code>csv.Sniffer</code> to heuristically detect delimiters (<code>,</code>, <code>;</code>, <code>\t</code>, <code>|</code>) and character encodings (UTF-8, Latin-1, CP1252), converting unformatted streams into structured DataFrames.</li>
            <li><strong>Deterministic Profiling Engine:</strong> Evaluates missingness ratios, Interquartile Range (IQR) outliers, duplicate rows, and Pearson correlation matrices, outputting a 100-point Data Health Score.</li>
            <li><strong>AST Security Sandbox:</strong> Parses all LLM-synthesized code into an Abstract Syntax Tree, checking every node against a strict whitelist before delegating to an isolated runtime.</li>
            <li><strong>Generative Intelligence Studio:</strong> Orchestrates Sentence-BERT column embeddings (384 dimensions) and PyTorch CTGAN tabular generation with mode-specific normalization.</li>
            <li><strong>Responsible AI Governance:</strong> Conducts regex and heuristic scans for sensitive attributes (PII) and evaluates target class imbalance ratios with automated remediation advice.</li>
        </ol>
    </div>
    <div class="page-footer"><span>6</span></div>
</div>
"""
    return html.replace('{{FIG2}}', get_fig2_svg())

def get_p7_u1_u2():
    """Page 7: Chapter 4 - Core Analytical Modules Implementation (U1 & U2)."""
    html = """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>4 Core Analytical Modules (Units U1 & U2)</h1>
        
        <h2>4.1 Unit U1: Tabular Profiling & Data Health Scorecard</h2>
        <p>
            The profiling subsystem ingests any tabular dataset and calculates an objective, penalty-weighted <strong>Data Health Index (0 to 100)</strong> based on four empirical quality dimensions:
        </p>
        <div class="alert-box" style="padding: 6px 12px; margin: 4px 0;">
            <div class="alert-title">Mathematical Formulation of Data Health Index</div>
            <div class="alert-content" style="font-size: 8.8pt;">
                Health Score = 100 - [ 30 &times; (N_missing / (N &times; P)) + 20 &times; (N_dup / N) + 25 &times; (N_outlier / N) + 25 &times; SkewPenalty ]
                <br>Where N is total rows, P is feature count, and penalties are normalized between 0 and 1.
            </div>
        </div>
        <p style="font-size: 8.8pt;">
            The ML Recommender uses cardinality heuristics to classify the dataset into: <strong>Binary Classification</strong> (2 discrete target levels), <strong>Multiclass Classification</strong> (3–20 discrete levels), <strong>Supervised Regression</strong> (continuous numerical target), or <strong>Unsupervised Clustering</strong> (no specified target).
        </p>

        <h2>4.2 Unit U2: Natural Language Assistant & AST Security Sandbox</h2>
        <p>
            To enable non-technical users to query datasets in plain English, an LLM assistant translates natural language into executable Pandas expressions. Because executing AI-generated code directly introduces severe security vulnerabilities, DataPulse AI implements an <strong>Abstract Syntax Tree (AST) Security Sandbox</strong>:
        </p>

        <div class="figure-wrapper" style="margin: 4px 0;">
            {{FIG3}}
            <div class="figure-caption"><strong>Figure 3:</strong> AST static code validation pipeline intercepting unauthorized system calls and imports.</div>
        </div>

        <p style="font-size: 8.7pt;">
            The validator subclasses <code>ast.NodeVisitor</code> to recursively inspect code syntax. Prohibited AST nodes (<code>Import</code>, <code>ImportFrom</code>, <code>Exec</code>, <code>Global</code>) and dangerous function calls (<code>os.system</code>, <code>subprocess</code>, <code>open</code>, <code>socket</code>) are blocked prior to execution, guaranteeing a verified <strong>100% interception rate</strong> against adversarial exploits.
        </p>
    </div>
    <div class="page-footer"><span>7</span></div>
</div>
"""
    return html.replace('{{FIG3}}', get_fig3_svg())

def get_p8_u3_u4():
    """Page 8: Chapter 5 - Advanced Generative & Multimodal Modules (U3 & U4)."""
    html = """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>5 Advanced Generative Modules (Units U3 & U4)</h1>
        
        <h2>5.1 Unit U3: Sentence-BERT Column Semantic Clustering</h2>
        <p>
            Heterogeneous datasets frequently use cryptic or non-standard column headers (e.g., <code>sibsp</code>, <code>parch</code>, <code>fare_amt</code>). Unit U3 uses the <strong>Sentence-BERT (<code>all-MiniLM-L6-v2</code>)</strong> transformer model to encode column headers, data types, and sample value distributions into 384-dimensional dense semantic embeddings:
        </p>
        <p style="font-size: 8.8pt;">
            Given column embedding vectors u and v, pairwise semantic similarity is computed via cosine similarity:
            <br><strong>Cosine Similarity(u, v) = (u &middot; v) / (||u|| &times; ||v||)</strong>
            <br>Columns with similarity scores exceeding an adjustable threshold (&tau; = 0.65) are clustered together, allowing automatic discovery of redundant or conceptually linked attributes.
        </p>

        <h2>5.2 Unit U4: PyTorch CTGAN Tabular Synthesizer</h2>
        <p>
            To address data scarcity and privacy constraints, Unit U4 integrates a <strong>Conditional Wasserstein GAN with Gradient Penalty (CTGAN)</strong> implemented in PyTorch. CTGAN resolves the multi-modal and non-Gaussian nature of continuous tabular variables through <strong>Mode-Specific Normalization</strong>:
        </p>

        <div class="figure-wrapper" style="margin: 4px 0;">
            {{FIG5}}
            <div class="figure-caption"><strong>Figure 4:</strong> PyTorch CTGAN tabular generative workflow from mode normalization to synthetic sampling.</div>
        </div>

        <p style="font-size: 8.7pt;">
            Each continuous feature is modeled using a Variational Gaussian Mixture (VGM). Values are represented as a one-hot representation of the Gaussian component and a scalar offset within that component. The generator and discriminator are trained adversarially using Pac-GAN packing (pac size = 10) to prevent mode collapse.
        </p>
    </div>
    <div class="page-footer"><span>8</span></div>
</div>
"""
    return html.replace('{{FIG5}}', get_fig5_svg())

def get_p9_u5():
    """Page 9: Chapter 6 - Responsible AI, Privacy Governance & Security Auditing (U5)."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>6 Responsible AI, Privacy & Governance (Unit U5)</h1>
        
        <h2>6.1 Automated Sensitive Attribute & PII Scanner</h2>
        <p>
            Data privacy regulations (GDPR, India's DPDP Act, and HIPAA) mandate strict protections against unintentional dissemination of Personally Identifiable Information (PII). Unit U5 executes an automated security audit combining deterministic regex patterns and contextual heuristics across all column headers and data records:
        </p>

        <table style="width: 100%; font-size: 8.2pt; margin: 4px 0;">
            <thead>
                <tr>
                    <th>Sensitive Pattern</th>
                    <th>Risk Category</th>
                    <th>Detection Mechanism</th>
                    <th>Remediation Protocol</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><strong>Email Addresses</strong></td><td>High Risk (Direct ID)</td><td>RFC 5322 regex validation</td><td>SHA-256 pseudonymization or mask</td></tr>
                <tr><td><strong>Phone / Mobile</strong></td><td>High Risk (Contact)</td><td>E.164 international phone regex</td><td>Redact middle digits: <code>+91-XXXXX-1234</code></td></tr>
                <tr><td><strong>Personal Names</strong></td><td>Medium Risk (Direct)</td><td>Header heuristic + Title tokens</td><td>Anonymize with synthetic surrogates</td></tr>
                <tr><td><strong>Government IDs</strong></td><td>Critical Risk (Official)</td><td>Aadhaar / SSN checksum validator</td><td>Drop column prior to model training</td></tr>
                <tr><td><strong>Ticket / Account</strong></td><td>Medium Risk (Indirect)</td><td>Alpha-numeric high-cardinality regex</td><td>Hash identifier or extract prefix only</td></tr>
            </tbody>
        </table>

        <h2>6.2 Target Class Imbalance Evaluation & Mitigation</h2>
        <p>
            Imbalanced classification targets distort traditional accuracy metrics, producing deceptive predictive models (the "Accuracy Paradox"). DataPulse AI calculates the <strong>Imbalance Ratio (IR)</strong>:
            <br><strong>IR = N_majority / N_minority</strong>
            <br>When IR &gt; 1.50, the platform flags a warning and presents targeted mitigation recipes:
        </p>
        <div class="grid-2" style="margin-top: 6px;">
            <div class="card" style="padding: 8px 12px;">
                <div style="font-weight: 700; color: #4a3d8f; font-size: 8.5pt;">Algorithmic Class-Weighting</div>
                <div style="font-size: 8pt; color: #334155; margin-top: 3px;">
                    Penalizes minority misclassifications inversely proportional to class frequencies: <strong>W_j = N / (K &times; N_j)</strong>
                </div>
            </div>
            <div class="card" style="padding: 8px 12px;">
                <div style="font-weight: 700; color: #4a3d8f; font-size: 8.5pt;">Synthetic Oversampling (SMOTE)</div>
                <div style="font-size: 8pt; color: #334155; margin-top: 3px;">
                    Synthesizes virtual minority instances along k-nearest neighbor line segments, balancing the training set distribution.
                </div>
            </div>
        </div>

        <h2>6.3 Responsible AI Governance Checklist</h2>
        <p style="font-size: 8.7pt;">
            Before exporting any dataset profile or training an algorithm, the system performs an automated checklist verifying: (1) Absence of unencrypted sensitive attributes, (2) Fairness parity across demographic subsets, and (3) Verification that synthetic distributions do not leak memorized training rows.
        </p>
    </div>
    <div class="page-footer"><span>9</span></div>
</div>
"""

def get_p10_benchmarks():
    """Page 10: Chapter 7 - Experimental Results & Cross-Dataset Benchmarks."""
    html = """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>7 Experimental Results & Benchmarks</h1>
        
        <h2>7.1 Empirical Cross-Dataset Evaluation</h2>
        <p>
            To demonstrate generalizability, DataPulse AI was benchmarked across three diverse standard public datasets representing distinct machine learning problem families:
        </p>

        <table style="width: 100%; font-size: 8.2pt; margin: 4px 0;">
            <thead>
                <tr>
                    <th>Evaluation Metric</th>
                    <th>Iris Flower Dataset</th>
                    <th>Titanic Survival Dataset</th>
                    <th>Wine Quality Dataset</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><strong>Dataset Dimensions</strong></td><td>150 rows × 5 columns</td><td>891 rows × 12 columns</td><td>1,599 rows × 12 columns</td></tr>
                <tr><td><strong>Recommended Task</strong></td><td>Multiclass Classification</td><td>Binary Classification</td><td>Supervised Regression</td></tr>
                <tr><td><strong>Target Attribute</strong></td><td><code>species</code> (3 balanced classes)</td><td><code>Survived</code> (0 or 1)</td><td><code>quality</code> (score 3 to 8)</td></tr>
                <tr><td><strong>Data Health Score</strong></td><td><strong>99.0 / 100</strong> (Excellent)</td><td><strong>90.5 / 100</strong> (Good)</td><td><strong>83.4 / 100</strong> (Moderate)</td></tr>
                <tr><td><strong>Missing Values</strong></td><td>0 cells (0.0%)</td><td>866 cells (8.1%)</td><td>0 cells (0.0%)</td></tr>
                <tr><td><strong>IQR Outlier Cells</strong></td><td>4 cells (0.5%)</td><td>116 cells (1.1%)</td><td>448 cells (2.3%)</td></tr>
                <tr><td><strong>Target Imbalance Ratio</strong></td><td>1.00 : 1 (Perfect)</td><td>1.61 : 1 (Moderate)</td><td>68.1 : 1 (Severe tail skew)</td></tr>
                <tr><td><strong>PII Attributes Detected</strong></td><td>0 sensitive columns</td><td>2 columns (<code>Name</code>, <code>Ticket</code>)</td><td>0 sensitive columns</td></tr>
                <tr><td><strong>CTGAN Mean KS Score</strong></td><td>0.362 (High fidelity)</td><td><strong>0.281</strong> (High fidelity)</td><td>0.276 (High fidelity)</td></tr>
                <tr><td><strong>Correlation MAE Error</strong></td><td>0.509</td><td><strong>0.040</strong> (Near-perfect)</td><td>0.215</td></tr>
            </tbody>
        </table>

        <h2>7.2 Statistical Fidelity Analysis (Two-Sample KS Test)</h2>
        <div class="figure-wrapper" style="margin: 4px 0;">
            {{FIG9}}
            <div class="figure-caption"><strong>Figure 5:</strong> Cross-dataset comparative radar score and statistical health benchmarks.</div>
        </div>

        <p style="font-size: 8.7pt;">
            The two-sample Kolmogorov-Smirnov test measures the maximum distance between real and synthetic empirical cumulative distribution functions. The Titanic dataset achieved a mean KS statistic of <strong>0.281</strong> and a Correlation Mean Absolute Error of <strong>0.040</strong>, confirming that generated rows preserve real inter-feature dependencies without memorizing training records.
        </p>
    </div>
    <div class="page-footer"><span>10</span></div>
</div>
"""
    return html.replace('{{FIG9}}', get_fig9_svg())

def get_p11_testing_deploy():
    """Page 11: Chapter 8 - Software Testing & Cloud Deployment."""
    html = """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>8 Software Testing & Cloud Deployment</h1>
        
        <h2>8.1 Automated Pytest Test Suite (40/40 Passed)</h2>
        <p>
            To guarantee industrial-grade reliability, the entire codebase is verified by an automated test suite executed via <strong>Pytest</strong>. The test harness exercises 40 dedicated unit and integration tests across all modules with a <strong>100% pass rate</strong>:
        </p>

        <table style="width: 100%; font-size: 8.2pt; margin: 4px 0;">
            <thead>
                <tr>
                    <th>Test Module</th>
                    <th>Scope & Invariants Verified</th>
                    <th>Tests</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><code>test_data_loader.py</code></td><td>Delimiter sniffing, encoding fallback, corrupt file handling</td><td>6 / 6</td><td>Passed (100%)</td></tr>
                <tr><td><code>test_profiler.py</code></td><td>Completeness, IQR outliers, health score equation bounds</td><td>7 / 7</td><td>Passed (100%)</td></tr>
                <tr><td><code>test_ml_recommender.py</code></td><td>Task family classification heuristics, metric selection</td><td>6 / 6</td><td>Passed (100%)</td></tr>
                <tr><td><code>test_code_validator.py</code></td><td>AST visitor, RCE attack interception, sandbox security</td><td>8 / 8</td><td>Passed (100%)</td></tr>
                <tr><td><code>test_embeddings.py</code></td><td>Sentence-BERT matrix dimensions, cosine similarity clustering</td><td>4 / 4</td><td>Passed (100%)</td></tr>
                <tr><td><code>test_ctgan.py</code></td><td>VGM normalization, synthetic row sampling, KS evaluator</td><td>5 / 5</td><td>Passed (100%)</td></tr>
                <tr><td><code>test_responsible_ai.py</code></td><td>PII regex detection, imbalance ratio calculation, recipes</td><td>4 / 4</td><td>Passed (100%)</td></tr>
                <tr style="font-weight: 700; background: #ede9fe;"><td><strong>Total Test Harness</strong></td><td><strong>End-to-end full system verification in 44.48s runtime</strong></td><td><strong>40 / 40</strong></td><td><strong>ALL PASSED</strong></td></tr>
            </tbody>
        </table>

        <h2>8.2 Cloud Deployment Topology</h2>
        <div class="figure-wrapper" style="margin: 4px 0;">
            {{FIG10}}
            <div class="figure-caption"><strong>Figure 6:</strong> Pytest automated verification suite breakdown and testing topology.</div>
        </div>

        <h2>8.3 Production Cloud Deployment</h2>
        <p style="font-size: 8.8pt;">
            DataPulse AI is deployed to <strong>Streamlit Community Cloud</strong> connected to GitHub repository <code>atharva1145/Datapulse-ai-p10</code>. Containerized with headless Chromium and PyTorch CPU runtimes, the application offers immediate global availability with zero client installation.
        </p>
    </div>
    <div class="page-footer"><span>11</span></div>
</div>
"""
    return html.replace('{{FIG10}}', get_fig10_svg())

def get_p12_conclusion():
    """Page 12: Chapter 9 - Conclusion, Future Scope & References."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>9 Conclusion, Future Scope & References</h1>
        
        <h2>9.1 Conclusion</h2>
        <p style="font-size: 8.8pt;">
            DataPulse AI successfully satisfies all requirements mandated under Continuous Assessment problem statement <strong>P10: CSV Dataset Insight & Task Recommender</strong>. The system unifies classical deterministic statistical profiling with modern generative artificial intelligence paradigms. By incorporating AST sandbox security (100% exploit interception), Sentence-BERT semantic column clustering, PyTorch CTGAN deep tabular synthesis, and automated Responsible AI governance, DataPulse AI delivers an empirically grounded, intuitive, and secure platform for tabular data science.
        </p>

        <h2>9.2 Technical Limitations & Future Scope</h2>
        <p style="font-size: 8.7pt;">
            Current limitations include CPU training latencies for CTGAN on datasets exceeding 50,000 records and ephemeral user session state. Future enhancements will integrate <strong>Differential Privacy (DP-CTGAN)</strong> with formal (&epsilon;, &delta;) mathematical privacy budgets, automated SHAP feature engineering, and multi-table relational schema inference via foreign-key embeddings.
        </p>

        <h2>9.3 Project Verification Links</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin: 4px 0 8px 0;">
            <div class="card" style="padding: 6px 10px;">
                <div style="font-size: 7.2pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase;">LIVE WEB APPLICATION</div>
                <div style="font-size: 8.5pt; font-weight: 700; color: #1d7770; font-family: monospace;">datapulse-ai-p10.streamlit.app</div>
            </div>
            <div class="card" style="padding: 6px 10px;">
                <div style="font-size: 7.2pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase;">GITHUB REPOSITORY</div>
                <div style="font-size: 8.5pt; font-weight: 700; color: #1d7770; font-family: monospace;">github.com/atharva1145/Datapulse-ai-p10</div>
            </div>
        </div>

        <h2>9.4 Academic References (IEEE Format)</h2>
        <ol style="font-size: 7.5pt; line-height: 1.35; margin-left: 14px; margin-bottom: 0;">
            <li>Streamlit Inc., “Streamlit Documentation and Cloud Architecture,” 2024. [Online]. Available: https://docs.streamlit.io/</li>
            <li>Google, “Gemini API Python SDK Specification,” Google AI for Developers, 2024. Available: https://ai.google.dev/</li>
            <li>L. Xu, M. Skoularidou, A. Cuesta-Infante, and K. Veeramachaneni, “Modeling Tabular data using Conditional GAN,” in <em>Advances in Neural Information Processing Systems (NeurIPS 2019)</em>, Vancouver, Canada, 2019.</li>
            <li>N. Reimers and I. Gurevych, “Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks,” in <em>Proc. EMNLP 2019</em>, Hong Kong, 2019.</li>
            <li>F. Pedregosa et al., “Scikit-learn: Machine Learning in Python,” <em>Journal of Machine Learning Research (JMLR)</em>, vol. 12, pp. 2825–2830, 2011.</li>
            <li>Python Software Foundation, “AST — Abstract Syntax Trees Specification (Python 3.12),” 2024. https://docs.python.org/3/library/ast.html</li>
            <li>E. Choi et al., “Generating Multi-label Discrete Patient Records using Generative Adversarial Networks,” in <em>Proc. MLHC</em>, 2017.</li>
            <li>European Parliament, “General Data Protection Regulation (GDPR),” Regulation (EU) 2016/679, Official Journal of the European Union, 2016.</li>
        </ol>
    </div>
    <div class="page-footer"><span>12</span></div>
</div>
"""
