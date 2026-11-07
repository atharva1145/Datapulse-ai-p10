"""
Front matter pages for DataPulse AI Mini Project Report (Pages 1 to 5).
Includes Cover Page, Declaration & Acknowledgement, Abstract & Keywords, Contents, List of Figures/Tables.
"""

def get_page_1_html(logo_b64):
    """Page 1: Cover Page."""
    return f"""
<div class="page" style="justify-content: space-between; align-items: center; text-align: center; padding: 22mm 20mm 20mm 20mm;">
    <div>
        <div style="font-size: 13pt; font-weight: 800; color: #3b3270; letter-spacing: 0.05em; text-transform: uppercase;">MIT ADT UNIVERSITY, PUNE</div>
        <div style="font-size: 10.5pt; font-weight: 500; color: #5b6172; margin-top: 4px;">Department of Computer Science and Engineering</div>
        <div style="display: inline-block; background: #ede9fe; color: #4a3d8f; font-size: 8.5pt; font-weight: 700; padding: 3px 12px; border-radius: 9999px; margin-top: 10px; letter-spacing: 0.04em;">MINI PROJECT REPORT &nbsp;·&nbsp; GENERATIVE AI</div>
    </div>

    <div style="margin: 15px 0;">
        <img src="data:image/png;base64,{logo_b64}" style="width: 100px; height: 100px; border-radius: 50%; object-fit: contain; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" alt="MIT ADT University">
    </div>

    <div>
        <div style="font-size: 26pt; font-weight: 800; color: #2d2a4a; letter-spacing: -0.02em; line-height: 1.15;">DataPulse AI</div>
        <div style="font-size: 12pt; font-weight: 500; color: #4a4f60; margin-top: 6px; margin-bottom: 12px;">Autonomous CSV Dataset Profiler, ML Task Recommender & Generative AI Studio</div>
        <div class="pill-badge" style="font-size: 9.5pt; padding: 5px 14px;">Problem Statement P10 · CSV Dataset Insight & Task Recommender</div>
    </div>

    <div style="width: 100%; max-width: 500px; background: #fbfbfe; border: 1px solid #e6e8f0; border-radius: 8px; padding: 14px 18px; margin-top: 10px; text-align: left;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px 16px;">
            <div>
                <div style="font-size: 7.8pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase; letter-spacing: 0.05em;">SUBMITTED BY</div>
                <div style="font-size: 9.8pt; font-weight: 600; color: #1f2433; margin-top: 2px;">Atharva Shelar</div>
            </div>
            <div>
                <div style="font-size: 7.8pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase; letter-spacing: 0.05em;">FACULTY GUIDE</div>
                <div style="font-size: 9.8pt; font-weight: 600; color: #1f2433; margin-top: 2px;">Dr. Snehlata Funde</div>
            </div>
            <div>
                <div style="font-size: 7.8pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase; letter-spacing: 0.05em;">ROLL NUMBER</div>
                <div style="font-size: 9.8pt; font-weight: 600; color: #1f2433; margin-top: 2px;">10</div>
            </div>
            <div>
                <div style="font-size: 7.8pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase; letter-spacing: 0.05em;">ENROLLMENT NUMBER</div>
                <div style="font-size: 9.8pt; font-weight: 600; color: #1f2433; margin-top: 2px;">ADT23SOCB0244</div>
            </div>
            <div>
                <div style="font-size: 7.8pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase; letter-spacing: 0.05em;">CLASS / DIVISION</div>
                <div style="font-size: 9.8pt; font-weight: 600; color: #1f2433; margin-top: 2px;">LY-AIA-3</div>
            </div>
            <div>
                <div style="font-size: 7.8pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase; letter-spacing: 0.05em;">ACADEMIC YEAR</div>
                <div style="font-size: 9.8pt; font-weight: 600; color: #1f2433; margin-top: 2px;">2026–2027</div>
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

def get_page_2_html():
    """Page 2: Declaration & Acknowledgement."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>Declaration</h1>
        <p>
            I, <strong>Atharva Shelar</strong>, hereby declare that this mini project report entitled 
            <strong>“DataPulse AI – Autonomous CSV Dataset Profiler, ML Task Recommender & Generative AI Studio”</strong> 
            is an authentic record of my own independent work carried out for the Continuous Assessment (CA) component of the 
            Generative AI course at MIT ADT University, Pune.
        </p>
        <p>
            The software architectures, algorithmic implementations, Abstract Syntax Tree (AST) security sandbox, 
            heuristic recommendation engines, Sentence-BERT clustering routines, PyTorch CTGAN generative pipelines, 
            and empirical evaluation benchmarks described in this document were designed, developed, and verified by me. 
            All functional screenshots and empirical data reported reflect genuine outputs produced by the application.
        </p>
        <p>
            Third-party open-source libraries, deep learning frameworks, and foundational model architectures 
            (including Google Gemini API, Sentence-Transformers, PyTorch, SDV/CTGAN, Scikit-learn, Pandas, and Streamlit) 
            remain the intellectual property of their respective creators and are acknowledged in the References section. 
            Their utilization in this project adheres strictly to their respective open-source licensing terms.
        </p>

        <div style="margin-top: 22px; display: flex; justify-content: space-between; align-items: flex-end;">
            <div>
                <div style="font-weight: 700; color: #1f2433; font-size: 10pt;">Atharva Shelar</div>
                <div style="color: #64748b; font-size: 8.5pt;">Signature of the Student</div>
            </div>
            <div style="text-align: right;">
                <div style="font-weight: 600; color: #1f2433; font-size: 9.5pt;">07 November 2026</div>
                <div style="color: #64748b; font-size: 8.5pt;">Date</div>
            </div>
        </div>

        <div style="border-top: 1px solid #edf0f5; margin-top: 24px; padding-top: 16px;">
            <h1>Acknowledgement</h1>
            <p>
                I express my deepest gratitude to my faculty guide, <strong>Dr. Snehlata Funde</strong>, for her exceptional guidance, 
                intellectual encouragement, and constructive critique throughout the design and execution of this mini project. 
                Her recommendations on formulating rigorous validation protocols around the units U1–U5 of problem statement P10 
                were instrumental in transforming a broad conceptual vision into a secure, robust, and mathematically grounded system.
            </p>
            <p>
                I extend my heartfelt appreciation to the <strong>Department of Computer Science and Engineering</strong>, 
                MIT School of Computing, MIT ADT University, Pune, for providing a progressive academic curriculum, high-performance 
                computational infrastructure, and an inspiring academic atmosphere.
            </p>
            <p>
                Finally, I convey my thanks to the global open-source artificial intelligence research community whose dedication 
                to transparency, reproducible research, and foundational tooling forms the technical bedrock upon which DataPulse AI is built.
            </p>

            <div style="margin-top: 18px;">
                <div style="font-weight: 700; color: #1f2433; font-size: 9.8pt;">Atharva Shelar</div>
                <div style="color: #64748b; font-size: 8.5pt;">Roll No. 10 · LY-AIA-3 · ADT23SOCB0244</div>
            </div>
        </div>
    </div>
    <div class="page-footer">
        <span>2</span>
    </div>
</div>
"""

def get_page_3_html():
    """Page 3: Abstract & Keywords."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>Abstract</h1>
        <p>
            Exploratory data analysis (EDA), data quality assessment, and machine learning problem formulation represent 
            essential yet time-intensive initial phases of the data science lifecycle. In professional and academic settings, 
            practitioners routinely struggle with heterogeneous CSV formatting, unobserved data hygiene defects (e.g., severe 
            skewness, high missingness, duplicate rows, and outlier contamination), and the cognitive overhead of selecting 
            appropriate algorithmic families. <strong>DataPulse AI</strong> is an autonomous, production-grade tabular dataset profiler, 
            heuristic machine learning task recommender, and generative AI platform engineered to resolve these bottlenecks.
        </p>
        <p>
            Addressing the assigned Continuous Assessment problem statement <strong>P10 (CSV Dataset Insight & Task Recommender)</strong>, 
            the application realizes five interconnected units (U1–U5) combining deterministic statistical computation with modern 
            generative modeling. In <strong>U1</strong>, the system ingests arbitrary CSV files via robust delimiter sniffing, computes 
            per-column parametric and non-parametric distributions, calculates an objective 100-point Data Health Score, classifies 
            the target into Supervised (Binary/Multiclass Classification or Continuous Regression) or Unsupervised paradigms, and 
            formulates a tailored 7-stage ML lifecycle blueprint. In <strong>U2</strong>, an intelligent natural language code assistant 
            leverages large language models (Google Gemini API with a local Ollama fallback) to write and execute pandas transformations; 
            arbitrary code execution risks are neutralized through a dedicated Abstract Syntax Tree (AST) visitor that enforces strict 
            syntactic whitelisting and rejects dangerous system operations.
        </p>
        <p>
            To uncover latent semantic relationships, <strong>U3</strong> embeds column names and contextual schema definitions into a 
            high-dimensional vector space using Sentence-BERT (<code>all-MiniLM-L6-v2</code>) to perform hierarchical column clustering, 
            while an integrated multimodal Vision LLM inspects rendered statistical charts to extract analytical commentary. In <strong>U4</strong>, 
            a deep tabular generative model based on PyTorch Conditional WGAN-GP (CTGAN) synthesizes realistic synthetic tabular samples, 
            empirically benchmarked against ground truth distributions using two-sample Kolmogorov-Smirnov (KS) tests and correlation delta 
            Mean Absolute Error (MAE). Finally, in <strong>U5</strong>, an automated Responsible AI governance suite scans for Personally 
            Identifiable Information (PII) leaks and identifies severe class imbalances with prescriptive re-sampling remediation strategies.
        </p>
        <p>
            DataPulse AI was empirically validated across three public benchmark datasets—Iris Flower (Botanical, Health 99.0/100), 
            Titanic Passenger Survival (Maritime Demographic, Health 90.5/100), and Wine Quality (Physicochemical, Health 83.4/100). 
            Backed by a complete 40-test automated Pytest verification suite achieving a 100% pass rate, the application demonstrates 
            deterministic reproducibility, defensive sandbox integrity, and zero-hallucination factual consistency.
        </p>

        <div style="margin-top: 14px; padding: 10px 14px; background: #fbfbfe; border: 1px solid #e6e8f0; border-radius: 6px;">
            <span style="font-weight: 700; color: #4a3d8f; font-size: 8.8pt;">KEYWORDS: &nbsp;</span>
            <span style="color: #1f2433; font-size: 8.6pt;">Generative AI, Tabular Profiling, Machine Learning Task Recommendation, Abstract Syntax Tree (AST) Sandbox, Sentence-BERT Embeddings, PyTorch CTGAN, Tabular Synthesis, Responsible AI, PII Detection.</span>
        </div>
    </div>
    <div class="page-footer">
        <span>3</span>
    </div>
</div>
"""

def get_page_4_html():
    """Page 4: Contents (Table of Contents)."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>Contents</h1>
        
        <table style="width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 9pt;">
            <tbody>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 5px 0; font-weight: 700; color: #2d2a4a;">1 Introduction</td><td style="text-align: right; font-weight: 700; color: #7c6bc4;">6</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 5px 0; font-weight: 700; color: #2d2a4a;">2 Problem Statement</td><td style="text-align: right; font-weight: 700; color: #7c6bc4;">7</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 5px 0; font-weight: 700; color: #2d2a4a;">3 Objectives</td><td style="text-align: right; font-weight: 700; color: #7c6bc4;">8</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 5px 0; font-weight: 700; color: #2d2a4a;">4 Technology Stack</td><td style="text-align: right; font-weight: 700; color: #7c6bc4;">8</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 5px 0; font-weight: 700; color: #2d2a4a;">5 System Architecture</td><td style="text-align: right; font-weight: 700; color: #7c6bc4;">11</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 5px 0; font-weight: 700; color: #2d2a4a;">6 Implementation Methodology (U1–U5)</td><td style="text-align: right; font-weight: 700; color: #7c6bc4;">13</td></tr>
                <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 4px 0 4px 16px; color: #475569;">6.1 U1 – Distribution Profiling, Data Health & ML Lifecycle</td><td style="text-align: right; color: #64748b;">13</td></tr>
                <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 4px 0 4px 16px; color: #475569;">6.2 U2 – LLM Code Assistant, AST Sandbox & Execution</td><td style="text-align: right; color: #64748b;">15</td></tr>
                <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 4px 0 4px 16px; color: #475569;">6.3 U3 – Sentence-BERT Column Clustering & Vision LLM</td><td style="text-align: right; color: #64748b;">17</td></tr>
                <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 4px 0 4px 16px; color: #475569;">6.4 U4 – PyTorch CTGAN Tabular Generation & KS Benchmark</td><td style="text-align: right; color: #64748b;">19</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0 4px 16px; color: #475569;">6.5 U5 – Responsible AI: PII Detection & Class Imbalance</td><td style="text-align: right; color: #64748b;">20</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 5px 0; font-weight: 700; color: #2d2a4a;">7 Module-wise Implementation</td><td style="text-align: right; font-weight: 700; color: #7c6bc4;">21</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 5px 0; font-weight: 700; color: #2d2a4a;">8 Sample Dataset Demonstrations</td><td style="text-align: right; font-weight: 700; color: #7c6bc4;">23</td></tr>
                <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 4px 0 4px 16px; color: #475569;">8.1 Dataset 1 – Iris Flower (Botanical Morphometrics)</td><td style="text-align: right; color: #64748b;">23</td></tr>
                <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 4px 0 4px 16px; color: #475569;">8.2 Dataset 2 – Titanic Survival (Maritime Demographics)</td><td style="text-align: right; color: #64748b;">25</td></tr>
                <tr style="border-bottom: 1px solid #f8fafc;"><td style="padding: 4px 0 4px 16px; color: #475569;">8.3 Dataset 3 – Wine Quality (Physicochemical Analytics)</td><td style="text-align: right; color: #64748b;">27</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0 4px 16px; color: #475569;">8.4 Cross-Dataset Empirical Comparison Summary</td><td style="text-align: right; color: #64748b;">28</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 5px 0; font-weight: 700; color: #2d2a4a;">9 Testing and Results</td><td style="text-align: right; font-weight: 700; color: #7c6bc4;">29</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 5px 0; font-weight: 700; color: #2d2a4a;">10 Deployment</td><td style="text-align: right; font-weight: 700; color: #7c6bc4;">31</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 5px 0; font-weight: 700; color: #2d2a4a;">11 Limitations</td><td style="text-align: right; font-weight: 700; color: #7c6bc4;">33</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 5px 0; font-weight: 700; color: #2d2a4a;">12 Future Scope</td><td style="text-align: right; font-weight: 700; color: #7c6bc4;">33</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 5px 0; font-weight: 700; color: #2d2a4a;">13 Conclusion</td><td style="text-align: right; font-weight: 700; color: #7c6bc4;">35</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 5px 0; font-weight: 700; color: #2d2a4a;">14 Project Links</td><td style="text-align: right; font-weight: 700; color: #7c6bc4;">35</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 5px 0; font-weight: 700; color: #2d2a4a;">15 References</td><td style="text-align: right; font-weight: 700; color: #7c6bc4;">36</td></tr>
            </tbody>
        </table>
    </div>
    <div class="page-footer">
        <span>4</span>
    </div>
</div>
"""

def get_page_5_html():
    """Page 5: List of Figures & List of Tables."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>List of Figures</h1>
        
        <table style="width: 100%; border-collapse: collapse; margin-top: 6px; font-size: 8.8pt;">
            <tbody>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Figure 1</strong> · Technology stack architecture grouped by function and runtime location</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">10</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Figure 2</strong> · System architecture and decoupled execution boundary of DataPulse AI</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">11</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Figure 3</strong> · End-to-end data processing pipeline featuring AST sandbox and audit gates</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">12</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Figure 4</strong> · U1–U5 implementation methodology overview mapping units to modules</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">13</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Figure 5</strong> · DataPulse AI dataset upload, health scoring, and distribution dashboard</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">14</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Figure 6</strong> · Sandboxed LLM pandas assistant with AST security validation workflow</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">16</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Figure 7</strong> · Sentence-BERT semantic column similarity matrix and cluster groupings</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">17</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Figure 8</strong> · PyTorch CTGAN tabular generation architecture and WGAN-GP training flow</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">19</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Figure 9</strong> · Responsible AI governance panel: PII regex scanner and class imbalance ratios</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">20</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Figure 10</strong> · Multi-dataset empirical benchmark comparison (Data health vs KS fidelity)</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">26</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Figure 11</strong> · Distribution fidelity comparison: Real ground truth vs CTGAN synthetic curves</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">28</td></tr>
                <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Figure 12</strong> · Pytest test suite execution report confirming 40/40 passing test items</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">30</td></tr>
            </tbody>
        </table>

        <div style="margin-top: 18px;">
            <h1>List of Tables</h1>
            <table style="width: 100%; border-collapse: collapse; margin-top: 6px; font-size: 8.8pt;">
                <tbody>
                    <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Table 1</strong> · Comprehensive technology stack, role in DataPulse AI, and runtime environment</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">8</td></tr>
                    <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Table 2</strong> · Software module inventory, file paths, line counts, and functional responsibilities</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">21</td></tr>
                    <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Table 3</strong> · Pytest test suite architecture: file breakdown, test functions, and verified criteria</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">29</td></tr>
                    <tr style="border-bottom: 1px solid #edf0f5;"><td style="padding: 4px 0; color: #1f2433;"><strong>Table 4</strong> · Deployment environment matrix: Local workstation vs Streamlit Community Cloud</td><td style="text-align: right; font-weight: 600; color: #7c6bc4;">31</td></tr>
                </tbody>
            </table>
        </div>
    </div>
    <div class="page-footer">
        <span>5</span>
    </div>
</div>
"""
