"""
Chapters 11 to 15 for DataPulse AI Mini Project Report (Pages 33 to 36).
Covers Limitations, Future Scope, Conclusion, Project Links, and Academic References.
"""

def get_page_33_html():
    """Page 33: Chapter 11 – Limitations & Chapter 12 – Future Scope (Part 1)."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>11 Limitations</h1>
        <p>
            An essential tenet of scientific rigor is transparency regarding systemic boundaries and observed operational constraints. 
            DataPulse AI was developed to be honest about what its underlying models can and cannot mathematically guarantee:
        </p>

        <h2>1. CTGAN Compute Latency on Large Datasets</h2>
        <p>
            Conditional WGAN-GP training involves iterative gradient penalty computations and mode-specific variational Gaussian mixture fitting. 
            While small datasets (Iris: 150 rows) train in ~2.5 seconds on CPU, datasets exceeding 50,000 rows require 3 to 10 minutes 
            without dedicated GPU acceleration. On free-tier cloud containers (1 vCPU, 1 GB RAM), training on very large datasets can 
            risk timeout or memory watchdog termination unless downsampled.
        </p>

        <h2>2. Conservative AST Security Constraints on Plotting</h2>
        <p>
            To maintain an impenetrable security boundary against arbitrary code execution, the AST visitor strictly blocks explicit 
            <code>import</code> statements and plotting framework execution (e.g., <code>import matplotlib.pyplot as plt; plt.show()</code>). 
            Consequently, user queries in the Code Sandbox are restricted to DataFrame aggregations, filtering, and statistical summaries; 
            visual plotting is handled exclusively through pre-built UI components.
        </p>

        <h2>3. Ephemeral Cloud Storage & Session Volatility</h2>
        <p>
            Streamlit Community Cloud operates on stateless container infrastructure. Datasets uploaded by users, generated synthetic CSVs, 
            and trained CTGAN neural weights exist only in ephemeral container memory. When a browser tab is refreshed or a container 
            restarts after inactivity, cached artifacts must be regenerated.
        </p>

        <h2>4. Semantic Disambiguation of Uncontextualized Acronyms</h2>
        <p>
            Sentence-BERT maps natural language meanings into dense vector space. When presented with highly cryptic enterprise column headers 
            lacking descriptive names or data dictionary metadata (e.g., <code>x12_flg</code>, <code>f_39b</code>), cosine similarities 
            revert to superficial subword character matching rather than true domain semantics.
        </p>

        <h1>12 Future Scope</h1>
        <p>
            The modular architecture of DataPulse AI provides a foundation for several promising technical extensions, 
            outlined on the following page.
        </p>
    </div>
    <div class="page-footer">
        <span>33</span>
    </div>
</div>
"""

def get_page_34_html():
    """Page 34: Chapter 12 – Future Scope (Part 2)."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h2>Future Technical Roadmap</h2>
        
        <h2>1. Differential Privacy Integration (DP-CTGAN)</h2>
        <p>
            While empirical two-sample Kolmogorov-Smirnov tests verified that CTGAN generates novel rows without memorizing exact training samples, 
            enterprise privacy compliance often demands formal mathematical guarantees. Integrating <strong>Differential Privacy (DP-SGD)</strong> 
            with Rényi differential privacy accountants would allow practitioners to set explicit privacy budgets (&epsilon;, &delta;), 
            ensuring mathematical immunity against membership inference attacks in sensitive clinical or financial environments.
        </p>

        <h2>2. Automated Feature Engineering Pipeline Synthesis</h2>
        <p>
            Expanding the LLM assistant from ad-hoc analysis to automated feature engineering: combining Featuretools with LLM reasoning 
            to automatically generate polynomial features, interaction ratios, and log transformations, followed by automated feature 
            importance ranking using SHAP (SHapley Additive exPlanations).
        </p>

        <h2>3. Multi-Table Relational Schema Understanding</h2>
        <p>
            Extending the ingestion and profiling engine beyond single CSV files to parse multi-table relational schemas (e.g., SQLite dumps 
            or multi-table CSV archives). Sentence-BERT embeddings could automatically infer primary-foreign key relationships and suggest 
            optimal star or snowflake join configurations.
        </p>

        <h2>4. One-Click Jupyter Notebook & Scikit-learn Code Export</h2>
        <p>
            Empowering users to transition seamlessly from exploratory insight to model deployment by generating downloadable, standalone 
            Jupyter Notebooks (<code>.ipynb</code>) containing end-to-end Python code for data cleaning, train-test splitting, hyperparameter 
            tuning (Optuna), and model serialization.
        </p>

        <h2>5. Persistent User Workspaces & Cloud Database Integration</h2>
        <p>
            Transitioning from ephemeral session state to persistent user accounts backed by a managed PostgreSQL or Supabase database, 
            enabling teams to store dataset profiles, share interactive reports, and track dataset drift over time.
        </p>
    </div>
    <div class="page-footer">
        <span>34</span>
    </div>
</div>
"""

def get_page_35_html():
    """Page 35: Chapter 13 – Conclusion & Chapter 14 – Project Links."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>13 Conclusion</h1>
        <p>
            DataPulse AI successfully realizes all requirements stipulated under Continuous Assessment brief 
            <strong>P10 · CSV Dataset Insight & Task Recommender</strong>. The project demonstrates that fusing classical deterministic 
            statistical profiling with modern generative artificial intelligence paradigms produces a data intelligence platform that is 
            empirically grounded, intuitive for non-technical practitioners, and resiliently protected against adversarial threats.
        </p>
        <p>
            Through unit <strong>U1</strong>, arbitrary CSV datasets are ingested with automated delimiter sniffing, profiled for missingness 
            and IQR outliers, scored via an objective 100-point Data Health Score, and guided toward the optimal machine learning task family 
            accompanied by an adaptive 7-stage engineering lifecycle. Through <strong>U2</strong>, users converse with an LLM code assistant 
            whose generated pandas transformations are strictly validated by an Abstract Syntax Tree (AST) visitor, neutralizing remote code execution 
            risks with a verified 100% exploit interception rate. Through <strong>U3</strong>, Sentence-BERT semantic feature embeddings uncover 
            conceptual relationships across diverse schemas while a multimodal Vision LLM extracts analytical chart commentary. 
            Through <strong>U4</strong>, deep tabular generation using PyTorch Conditional WGAN-GP (CTGAN) synthesizes privacy-preserving tabular samples 
            with proven statistical fidelity (Titanic Mean KS: 0.281). Finally, through <strong>U5</strong>, automated governance proactively flags 
            PII leakage and severe target class skewness with actionable remediation recipes.
        </p>
        <p>
            Empirically benchmarked across three diverse public datasets (Iris, Titanic, and Wine Quality) and supported by a complete 40-test 
            automated Pytest test suite, DataPulse AI stands as a robust, production-ready contribution to modern tabular data science automation.
        </p>

        <h1>14 Project Links</h1>
        <div style="margin-top: 10px; display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
            <div class="card" style="padding: 12px 16px;">
                <div style="font-size: 7.8pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase; letter-spacing: 0.06em;">LIVE HOSTED WEB APPLICATION</div>
                <div style="margin-top: 4px;">
                    <a href="https://datapulse-ai-p10.streamlit.app/" style="font-size: 9.8pt; font-weight: 600; color: #1d7770; font-family: monospace; text-decoration: underline;">https://datapulse-ai-p10.streamlit.app/</a>
                </div>
                <div style="font-size: 8pt; color: #64748b; margin-top: 4px;">Globally accessible on Streamlit Community Cloud with zero setup.</div>
            </div>

            <div class="card" style="padding: 12px 16px;">
                <div style="font-size: 7.8pt; font-weight: 700; color: #7c6bc4; text-transform: uppercase; letter-spacing: 0.06em;">GITHUB SOURCE REPOSITORY</div>
                <div style="margin-top: 4px;">
                    <a href="https://github.com/atharva1145/Datapulse-ai-p10" style="font-size: 9.8pt; font-weight: 600; color: #1d7770; font-family: monospace; text-decoration: underline;">https://github.com/atharva1145/Datapulse-ai-p10</a>
                </div>
                <div style="font-size: 8pt; color: #64748b; margin-top: 4px;">Complete source code, 40 Pytest test suites, and documentation.</div>
            </div>
        </div>
    </div>
    <div class="page-footer">
        <span>35</span>
    </div>
</div>
"""

def get_page_36_html():
    """Page 36: Chapter 15 – References."""
    return """
<div class="page">
    <div class="page-header">
        <span class="header-left">DataPulse AI · Mini Project Report</span>
        <span class="header-right">Generative AI · P10</span>
    </div>
    <div class="page-body">
        <h1>15 References</h1>
        
        <ol style="margin-left: 20px; font-size: 8.2pt; line-height: 1.45; color: #1f2433;">
            <li style="margin-bottom: 5px;">
                Streamlit Inc., <em>“Streamlit Documentation and Cloud Deployment Architecture,”</em> 2024. [Online]. Available: <a href="https://docs.streamlit.io/" style="color: #1d7770;">https://docs.streamlit.io/</a>
            </li>
            <li style="margin-bottom: 5px;">
                Google, <em>“Gemini API Documentation and Python SDK Specification,”</em> Google AI for Developers, 2024. [Online]. Available: <a href="https://ai.google.dev/gemini-api/docs" style="color: #1d7770;">https://ai.google.dev/gemini-api/docs</a>
            </li>
            <li style="margin-bottom: 5px;">
                L. Xu, M. Skoularidou, A. Cuesta-Infante, and K. Veeramachaneni, <em>“Modeling Tabular data using Conditional GAN,”</em> in <em>Advances in Neural Information Processing Systems (NeurIPS 2019)</em>, Vancouver, Canada, Dec. 2019, arXiv:1907.00503.
            </li>
            <li style="margin-bottom: 5px;">
                N. Reimers and I. Gurevych, <em>“Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks,”</em> in <em>Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP 2019)</em>, Hong Kong, Nov. 2019, arXiv:1908.10084.
            </li>
            <li style="margin-bottom: 5px;">
                F. Pedregosa et al., <em>“Scikit-learn: Machine Learning in Python,”</em> <em>Journal of Machine Learning Research (JMLR)</em>, vol. 12, pp. 2825–2830, 2011.
            </li>
            <li style="margin-bottom: 5px;">
                W. McKinney, <em>“Data Structures for Statistical Computing in Python,”</em> in <em>Proceedings of the 9th Python in Science Conference (SciPy 2010)</em>, Austin, TX, pp. 51–56, 2010.
            </li>
            <li style="margin-bottom: 5px;">
                R. K. E. Bellamy et al., <em>“AI Fairness 360: An extensible toolkit for detecting and mitigating algorithmic bias,”</em> <em>IBM Journal of Research and Development</em>, vol. 63, no. 4/5, pp. 4:1–4:15, 2019, arXiv:1810.01943.
            </li>
            <li style="margin-bottom: 5px;">
                Python Software Foundation, <em>“The ast Module: Abstract Syntax Trees in Python 3.12 Standard Library,”</em> 2024. [Online]. Available: <a href="https://docs.python.org/3/library/ast.html" style="color: #1d7770;">https://docs.python.org/3/library/ast.html</a>
            </li>
            <li style="margin-bottom: 5px;">
                Qwen Team, <em>“Qwen2.5: A Foundation Language Model Series,”</em> Alibaba Cloud, Technical Report, 2024, arXiv:2409.12191.
            </li>
            <li style="margin-bottom: 5px;">
                F. J. Massey Jr., <em>“The Kolmogorov-Smirnov Test for Goodness of Fit,”</em> <em>Journal of the American Statistical Association</em>, vol. 46, no. 253, pp. 68–78, 1951.
            </li>
            <li style="margin-bottom: 5px;">
                J. W. Tukey, <em>“Exploratory Data Analysis,”</em> Addison-Wesley Series in Behavioral Science, Reading, Mass., 1977.
            </li>
            <li style="margin-bottom: 5px;">
                Synthetic Data Vault (SDV) Project, <em>“Synthetic Tabular Data Modeling and Quality Evaluation Metrics,”</em> Data to AI Lab, MIT, 2023. [Online]. Available: <a href="https://sdv.dev/" style="color: #1d7770;">https://sdv.dev/</a>
            </li>
        </ol>

        <div style="margin-top: 24px; padding-top: 14px; border-top: 1px solid #edf0f5; text-align: center; color: #8a8fa0; font-size: 8pt;">
            Department of Computer Science and Engineering &nbsp;·&nbsp; MIT ADT University, Pune &nbsp;·&nbsp; Academic Year 2026–2027
        </div>
    </div>
    <div class="page-footer">
        <span>36</span>
    </div>
</div>
"""
