"""
Chapters 1 to 5 for DataPulse AI Mini Project Report (Pages 6 to 12).
Includes Introduction, Problem Statement, Objectives, Technology Stack, System Architecture.
"""

from report_svgs import get_fig1_svg, get_fig2_svg, get_fig3_svg

def get_page_6_html():
    """Page 6: Chapter 1 – Introduction."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>1 Introduction</h1>
        <p>
            Generative Artificial Intelligence has revolutionized unstructured data domains such as natural language processing, 
            computer vision, and synthetic audio generation. However, in enterprise, financial, medical, and scientific analytics, 
            the vast majority of actionable business data remains fundamentally <strong>tabular</strong>—structured in relational tables 
            and Comma-Separated Values (CSV) formats. Despite decades of advancement in relational databases and machine learning libraries, 
            the initial exploratory phase of data science remains fraught with manual friction, subjective heuristics, and security risks.
        </p>
        <p>
            In standard machine learning workflows, a data scientist presented with an unfamiliar CSV file must perform a repetitive 
            series of diagnostic procedures: inspecting column data types, identifying missing values, computing central tendency and 
            dispersion statistics, plotting marginal distributions, diagnosing skewness and outliers, determining whether the business 
            problem corresponds to classification, regression, or unsupervised clustering, and verifying that the dataset does not leak 
            confidential or protected attributes. This exploratory data analysis (EDA) phase is both time-consuming and prone to human oversight.
        </p>
        
        <h2>Limitations of Traditional Static Profilers</h2>
        <p>
            Traditional automated profiling utilities (such as Pandas Profiling or ydata-profiling) generate monolithic, static HTML reports 
            that suffer from three structural drawbacks. First, they are <em>passive</em>: they display descriptive charts but fail to synthesize 
            actionable algorithmic guidance, leaving model family selection entirely to manual guesswork. Second, they lack <em>interactive semantic reasoning</em>: 
            users cannot interrogate the data through conversational queries or demand customized ad-hoc transformations without manually writing 
            boilerplate code. Third, they offer <em>zero generative or augmentation capabilities</em>: when datasets suffer from severe class imbalances 
            or privacy constraints preventing cloud sharing, legacy profilers cannot synthesize privacy-preserving tabular rows or benchmark distribution fidelity.
        </p>

        <h2>The Generative AI Paradigm for Tabular Data</h2>
        <p>
            DataPulse AI bridges this divide by orchestrating a tripartite synergy of artificial intelligence paradigms:
        </p>
        <ul>
            <li><strong>Deterministic Heuristic Profilers:</strong> Rapid, mathematical computation of missingness penalties, IQR outlier bounds, and parametric normality checks that provide grounded, non-hallucinated data hygiene scores.</li>
            <li><strong>Large Language Model (LLM) Reasoning:</strong> Utilizing advanced frontier LLMs (Google Gemini API with local Ollama fallback) to generate precise pandas transformation scripts from natural language queries, accompanied by contextual narrative interpretations.</li>
            <li><strong>Deep Tabular Generative Modeling:</strong> Deploying a Conditional Tabular Generative Adversarial Network (CTGAN) implemented in PyTorch to synthesize realistic, non-memorized tabular rows that preserve multi-column correlations and marginal distributions.</li>
        </ul>

        <h2>Engineering Philosophy & Defensive Security</h2>
        <p>
            Allowing an LLM to generate and execute code dynamically within a production web runtime introduces severe threat vectors, 
            chiefly arbitrary remote code execution (RCE) and system inspection. A core engineering contribution of DataPulse AI is its 
            <strong>defense-in-depth Abstract Syntax Tree (AST) validation sandbox</strong>. Rather than relying on fragile keyword blacklists, 
            the system inspects the Python parse tree before execution, blocking unauthorized system calls, filesystem writes, and introspection 
            dunders. The resulting platform delivers high analytical agility while maintaining uncompromising operational security.
        </p>
    </div>
    <div class="page-footer">
        <span>6</span>
    </div>
</div>
"""

def get_page_7_html():
    """Page 7: Chapter 2 – Problem Statement."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>2 Problem Statement</h1>
        <p>
            The assigned Continuous Assessment (CA) project is <strong>P10 · CSV Dataset Insight & Task Recommender</strong>. 
            The primary goal of the project is to develop an autonomous, production-ready system capable of profiling any arbitrary 
            uploaded CSV dataset, providing deep statistical insights, and recommending the optimal machine learning task and downstream lifecycle steps.
        </p>

        <div class="card" style="margin: 10px 0; background: #fbfbfe; border-left: 4px solid #3b3270;">
            <div style="font-weight: 700; color: #2d2a4a; font-size: 9.5pt;">CORE PROBLEM OBJECTIVE</div>
            <p style="margin-top: 4px; font-size: 9pt; color: #4a4f60; margin-bottom: 0;">
                <em>"Profile any uploaded CSV and recommend the right ML task and next steps. Complete all 5 units (U1–U5) and deploy as a live web application accompanied by empirical evaluation across 3 public datasets."</em>
            </p>
        </div>

        <h2>Unit-wise Requirements & Architectural Mapping</h2>
        <p>
            The project specification mandates the complete implementation of five distinct technical units (U1–U5). 
            Table 2.1 delineates each unit, its technical mandate, the implementing modules within the codebase, and where 
            substantive empirical evidence appears in this report.
        </p>

        <table>
            <thead>
                <tr>
                    <th style="width: 10%;">Unit</th>
                    <th style="width: 32%;">Prescribed Brief Requirement</th>
                    <th style="width: 38%;">Technical Implementation in DataPulse AI</th>
                    <th style="width: 20%;">Report Evidence</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>U1</strong></td>
                    <td>Plot column distributions; recommend learning type and lifecycle steps.</td>
                    <td>Parametric & non-parametric profiling; 100-pt Health Score; heuristic ML task decision trees; 7-stage lifecycle roadmap.</td>
                    <td>Section 6.1, Figs 4, 5;<br>Section 8 (3 Datasets)</td>
                </tr>
                <tr>
                    <td><strong>U2</strong></td>
                    <td>Have the LLM write and run pandas code, then explain the output.</td>
                    <td>Gemini API + Ollama provider; AST NodeVisitor security validator; sandboxed execution engine; narrative interpreter.</td>
                    <td>Section 6.2, Fig 6;<br>Section 9 (Pytest 40/40)</td>
                </tr>
                <tr>
                    <td><strong>U3</strong></td>
                    <td>Group similar columns with BERT embeddings; let a vision LLM read the charts.</td>
                    <td>Sentence-BERT (<code>all-MiniLM-L6-v2</code>) schema embeddings; cosine similarity matrix; Gemini Vision multimodal chart reader.</td>
                    <td>Section 6.3, Fig 7;<br>Module <code>embeddings.py</code></td>
                </tr>
                <tr>
                    <td><strong>U4</strong></td>
                    <td>Generate synthetic rows with CTGAN; compare real vs synthetic.</td>
                    <td>PyTorch Conditional WGAN-GP; variational Gaussian mixture normalization; 2-sample KS tests; correlation delta MAE.</td>
                    <td>Section 6.4, Fig 8;<br>Figs 10, 11</td>
                </tr>
                <tr>
                    <td><strong>U5</strong></td>
                    <td>Flag sensitive columns and class imbalance.</td>
                    <td>Regex/heuristic PII leak scanner; Shannon entropy imbalance ratios; SMOTE/class-weight mitigation; zero-hallucination test.</td>
                    <td>Section 6.5, Fig 9;<br>Responsible AI Suite</td>
                </tr>
            </tbody>
        </table>

        <h2>Deliverable Specifications</h2>
        <p>
            The deliverable obligations encompass:
        </p>
        <ul>
            <li>A live, globally accessible web application deployed on <strong>Streamlit Community Cloud</strong> with zero infrastructure setup required.</li>
            <li>A public, cleanly documented GitHub repository featuring clean git commit history, comprehensive docstrings, and a 40-test Pytest test suite.</li>
            <li>Empirical multi-dataset evaluation reports detailing performance across three diverse public benchmarks: <em>Iris Flower</em>, <em>Titanic Survival</em>, and <em>Wine Quality</em>.</li>
            <li>A comprehensive academic report and a 1-page executive summary sheet formatted according to university standards.</li>
        </ul>
    </div>
    <div class="page-footer">
        <span>7</span>
    </div>
</div>
"""

def get_page_8_html():
    """Page 8: Chapter 3 – Objectives & Chapter 4 – Technology Stack (Part 1)."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>3 Objectives</h1>
        <p>
            To fulfill the requirements of Continuous Assessment problem statement P10, the following ten concrete engineering objectives were established:
        </p>
        <ol style="margin-left: 18px; font-size: 8.8pt; line-height: 1.42;">
            <li><strong>Robust Ingestion Engine:</strong> Ingest arbitrary, user-uploaded CSV files with automatic delimiter sniffing (comma, semicolon, tab) and resilient type inference.</li>
            <li><strong>Automated Data Health Scoring:</strong> Calculate an objective 100-point Data Health Score based on missingness percentage, duplicate rows, and Interquartile Range (IQR) outliers.</li>
            <li><strong>Heuristic ML Task Classification:</strong> Formulate an automated rule engine to recommend Supervised Regression, Binary/Multiclass Classification, or Unsupervised Clustering based on target cardinality and feature distributions.</li>
            <li><strong>Adaptive ML Lifecycle Synthesis:</strong> Generate tailored 7-stage lifecycle plans with estimated engineering time allocations and task-specific algorithmic families.</li>
            <li><strong>Sandboxed Natural Language Code Assistant:</strong> Integrate an LLM agent that synthesizes valid pandas code transformations from conversational user prompts.</li>
            <li><strong>Defense-in-Depth AST Validator:</strong> Implement an Abstract Syntax Tree (AST) visitor that guarantees a 100% interception rate against dangerous system calls, file writes, and code injection exploits.</li>
            <li><strong>Semantic Feature Clustering:</strong> Compute high-dimensional semantic vector embeddings using Sentence-BERT (<code>all-MiniLM-L6-v2</code>) to cluster conceptually redundant features.</li>
            <li><strong>Multimodal Vision Chart Interpretation:</strong> Deploy a multimodal Vision LLM agent to directly read and interpret rendered statistical charts for novice users.</li>
            <li><strong>Deep Tabular Generative Synthesis:</strong> Train a PyTorch Conditional WGAN-GP (CTGAN) on-the-fly to sample non-memorized synthetic rows, benchmarked via two-sample Kolmogorov-Smirnov tests.</li>
            <li><strong>Responsible AI Governance:</strong> Proactively audit datasets for Personally Identifiable Information (PII) leakage and detect extreme target class imbalances with mitigation formulas.</li>
        </ol>

        <h1>4 Technology Stack</h1>
        <p>
            DataPulse AI is implemented in Python 3.12, leveraging modular libraries distributed across client, web runtime, cloud inference, and local execution boundaries. Table 1 catalogs the full technology stack and runtime locations.
        </p>

        <div style="font-weight: 700; color: #2d2a4a; font-size: 8.2pt; margin-top: 4px;">Table 1 · Comprehensive Technology Stack & Runtime Environments (Part 1)</div>
        <table>
            <thead>
                <tr>
                    <th style="width: 22%;">Technology</th>
                    <th style="width: 58%;">Purpose in DataPulse AI</th>
                    <th style="width: 20%;">Runtime Location</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Python 3.12</strong></td>
                    <td>Underlying runtime for data structures, typing, mathematical computation, and AST parsing.</td>
                    <td>All Environments</td>
                </tr>
                <tr>
                    <td><strong>Streamlit</strong></td>
                    <td>Interactive, reactive single-page web framework powering the user interface and session state.</td>
                    <td>Local / Hosted Cloud</td>
                </tr>
                <tr>
                    <td><strong>Pandas 2.2</strong></td>
                    <td>High-performance columnar DataFrame structures, group-by aggregations, and ingestion parsing.</td>
                    <td>In-Memory Application</td>
                </tr>
                <tr>
                    <td><strong>NumPy 1.26</strong></td>
                    <td>Vectorized numerical computing, matrix mathematics, quantile calculation, and random sampling.</td>
                    <td>In-Memory Application</td>
                </tr>
                <tr>
                    <td><strong>Scikit-learn 1.4</strong></td>
                    <td>Machine learning heuristics, target label encoding, train-test splitting, and evaluation metrics.</td>
                    <td>In-Memory Application</td>
                </tr>
                <tr>
                    <td><strong>SciPy Stats</strong></td>
                    <td>Two-sample Kolmogorov-Smirnov tests for distribution fidelity, kurtosis, and skewness tests.</td>
                    <td>In-Memory Application</td>
                </tr>
            </tbody>
        </table>
    </div>
    <div class="page-footer">
        <span>8</span>
    </div>
</div>
"""

def get_page_9_html():
    """Page 9: Chapter 4 – Technology Stack (Part 2)."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <div style="font-weight: 700; color: #2d2a4a; font-size: 8.2pt;">Table 1 · Comprehensive Technology Stack & Runtime Environments (Part 2)</div>
        <table>
            <thead>
                <tr>
                    <th style="width: 22%;">Technology</th>
                    <th style="width: 58%;">Purpose in DataPulse AI</th>
                    <th style="width: 20%;">Runtime Location</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Google Gemini API</strong></td>
                    <td>Cloud LLM provider (<code>gemini-2.5-flash</code> / <code>flash-lite</code>) for natural language pandas code synthesis and narrative interpretations.</td>
                    <td>Google Cloud Services</td>
                </tr>
                <tr>
                    <td><strong>Ollama & Qwen2.5</strong></td>
                    <td>Local fallback LLM provider running <code>qwen2.5:1.5b-instruct</code> for offline execution without cloud API dependency.</td>
                    <td>Local Workstation</td>
                </tr>
                <tr>
                    <td><strong>Python <code>ast</code></strong></td>
                    <td>Standard library Abstract Syntax Tree module for structural static analysis and security boundary enforcement.</td>
                    <td>In-Memory Application</td>
                </tr>
                <tr>
                    <td><strong>Sentence-Transformers</strong></td>
                    <td>Pre-trained Siamese neural network (<code>all-MiniLM-L6-v2</code>) generating 384-dimensional dense semantic column embeddings.</td>
                    <td>Local / PyTorch CPU</td>
                </tr>
                <tr>
                    <td><strong>PyTorch 2.6</strong></td>
                    <td>Deep learning tensor computation engine powering CTGAN neural generator and discriminator networks.</td>
                    <td>Local CPU / Torch</td>
                </tr>
                <tr>
                    <td><strong>CTGAN / SDV</strong></td>
                    <td>Conditional Tabular GAN architecture utilizing mode-specific normalization and Wasserstein loss with gradient penalty.</td>
                    <td>Local CPU / Torch</td>
                </tr>
                <tr>
                    <td><strong>Plotly Express</strong></td>
                    <td>Interactive GPU-accelerated interactive charts: marginal histograms, box plots, correlation heatmaps, and scatter plots.</td>
                    <td>Browser Web Client</td>
                </tr>
                <tr>
                    <td><strong>Matplotlib / Seaborn</strong></td>
                    <td>Static publication-quality plotting engine used to render charts for multimodal Vision LLM interpretation.</td>
                    <td>In-Memory Application</td>
                </tr>
                <tr>
                    <td><strong>Pytest 9.1</strong></td>
                    <td>Automated test execution harness running 40 unit and integration tests across 7 verification modules.</td>
                    <td>CI / Local Workstation</td>
                </tr>
            </tbody>
        </table>

        <h2>Runtime Environment Distribution Analysis</h2>
        <p>
            A deliberate architectural priority was to ensure that DataPulse AI operates reliably in two distinct execution modes:
        </p>
        <ul>
            <li><strong>Hosted Mode (Streamlit Community Cloud):</strong> The entire web application, deterministic profiling algorithms, AST security validators, Sentence-BERT semantic embeddings, and PyTorch CTGAN synthesis run inside a containerized Linux instance (1 GB RAM, 1 vCPU). Cloud LLM generation connects securely via encrypted HTTPS to the Google Gemini API using secrets configured in <code>st.secrets</code>.</li>
            <li><strong>Local Development Mode (Offline Workstation):</strong> When deployed locally on the developer's workstation, the system can operate with zero external network connectivity. Code generation falls back gracefully to a local Ollama server running <code>qwen2.5:1.5b-instruct</code>, while CTGAN leverages multi-core local CPU threads.</li>
        </ul>
        <p>
            Figure 1 on the following page visually organizes these technologies into functional tiers and distinguishes their physical execution environments.
        </p>
    </div>
    <div class="page-footer">
        <span>9</span>
    </div>
</div>
"""

def get_page_10_html():
    """Page 10: Figure 1 – Technology Stack Architecture Grid."""
    fig1 = get_fig1_svg()
    return f"""
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h2>Technology Stack Functional Mapping</h2>
        <p>
            The software components comprising DataPulse AI are partitioned into six functional disciplines: Interface & Web Core, 
            Tabular Profiling & Classical ML, Sandboxed LLM Code Generation, Multimodal Embeddings & Vision, Tabular Generative AI, 
            and Governance & Automated Verification.
        </p>

        <div class="figure-wrapper">
            {fig1}
            <div class="figure-caption">
                <strong>Figure 1 · Technology stack architecture grouped by function.</strong> Distinct columns indicate functional subsystems, while colored badges at the base delineate where each technology executes (In-Memory, Cloud API, Local CPU, or Automated CI).
            </div>
        </div>

        <p>
            By decoupling the interactive presentation layer (Streamlit) from the underlying computational engines (Pandas, PyTorch, AST Visitor, and Gemini SDK), 
            the architecture achieves complete modularity. Each subsystem exposes strict, typed Python interfaces, enabling independent unit testing, 
            easy replacement of LLM providers, and low-latency response times during interactive dataset exploration.
        </p>
    </div>
    <div class="page-footer">
        <span>10</span>
    </div>
</div>
"""

def get_page_11_html():
    """Page 11: Chapter 5 – System Architecture (Part 1)."""
    fig2 = get_fig2_svg()
    return f"""
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>5 System Architecture</h1>
        <p>
            DataPulse AI is architected around a decoupled, pipeline-oriented design pattern. Rather than constructing a monolithic script, 
            the application is structured into four distinct physical and logical layers: the Client Presentation Layer, the Core Application 
            Boundary, the Defensive Execution Sandbox, and the External Generative & Deep Learning Services (Figure 2).
        </p>

        <div class="figure-wrapper">
            {fig2}
            <div class="figure-caption">
                <strong>Figure 2 · System architecture and decoupled execution boundary of DataPulse AI.</strong> User input crosses into the Streamlit application core, where profiling, AST inspection, embeddings, and generative synthesis are coordinated across safe execution boundaries.
            </div>
        </div>

        <h2>Architectural Layers & Decoupling</h2>
        <ul>
            <li><strong>User Interaction Layer:</strong> Implemented in Streamlit, this layer handles drag-and-drop CSV ingestion, interactive parameter selection (target column picker, clustering threshold slider, synthetic sample count), and visual feedback rendering.</li>
            <li><strong>Core Processing Core (<code>modules/</code>):</strong> Encapsulates deterministic feature profiling (<code>data_profiler.py</code>), rule-based ML task recommendation (<code>ml_recommender.py</code>), Sentence-BERT semantic clustering (<code>embeddings.py</code>), and Responsible AI auditing (<code>responsible_ai.py</code>).</li>
            <li><strong>Defensive Execution Boundary:</strong> Enforces an impermeable barrier between untrusted LLM-generated Python code and the host environment. The <code>code_validator.py</code> module performs AST grammar inspection prior to invoking <code>safe_executor.py</code>.</li>
            <li><strong>External Engine Layer:</strong> Interfaces with the Google Gemini API for cloud intelligence, local Ollama endpoints for offline fallback, and PyTorch for neural CTGAN tabular synthesis.</li>
        </ul>
    </div>
    <div class="page-footer">
        <span>11</span>
    </div>
</div>
"""

def get_page_12_html():
    """Page 12: Chapter 5 – System Architecture (Part 2)."""
    fig3 = get_fig3_svg()
    return f"""
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h2>End-to-End Processing Pipeline</h2>
        <p>
            When a user uploads a CSV file, data flows through six sequential, inspectable stages. Each stage is gated by validation 
            checks, ensuring that malformed inputs or unsafe operations are intercepted before downstream tasks are triggered (Figure 3).
        </p>

        <div class="figure-wrapper">
            {fig3}
            <div class="figure-caption">
                <strong>Figure 3 · End-to-end data processing pipeline featuring AST sandbox and audit gates.</strong> Raw CSV data progresses sequentially through Ingestion, Profiling (U1), Code Generation (U2), Embedding Clustering (U3), CTGAN Synthesis (U4), and Responsible AI Governance (U5).
            </div>
        </div>

        <h2>Dataflow Mechanics & State Management</h2>
        <p>
            State across stages is managed cleanly through Streamlit's reactive session cache (<code>st.session_state</code>). 
            When a CSV file is ingested, a single canonical Pandas DataFrame is stored in memory. Profiling metrics, embedding vectors, 
            and synthetic rows are cached as derived artifacts:
        </p>
        <ul>
            <li><strong>Non-Destructive In-Memory Transformation:</strong> Code executed by the LLM assistant operates on isolated DataFrame slices or produces explicit return values; the canonical master dataset remains immutable.</li>
            <li><strong>Inspectable Intermediate Artifacts:</strong> Users can inspect intermediate outputs at every juncture: viewing the raw AST syntax tree, examining the Sentence-BERT cosine similarity matrix, and downloading the synthetic CTGAN table as a standalone CSV file.</li>
            <li><strong>Strict Security Gating:</strong> If the AST validator detects a forbidden node (such as <code>ast.Import</code> or <code>ast.Call</code> to <code>eval</code>), execution halts immediately, emitting a clear diagnostic alert in the UI without crashing the web session.</li>
        </ul>
    </div>
    <div class="page-footer">
        <span>12</span>
    </div>
</div>
"""
