import base64
import os
from playwright.sync_api import sync_playwright

def generate_1pager():
    with open('assets/mit_adt_logo.png', 'rb') as f:
        logo_b64 = base64.b64encode(f.read()).decode('utf-8')
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>DataPulse AI – 1-Page Summary Sheet</title>
<style>
    @page {{
        size: A4 portrait;
        margin: 0;
    }}
    * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }}
    body {{
        font-family: "Times New Roman", Times, Georgia, serif;
        color: #1f2433;
        background: #ffffff;
        font-size: 9.5pt;
        line-height: 1.45;
        width: 210mm;
        height: 297mm;
        padding: 16mm 18mm 14mm 18mm;
        position: relative;
        box-sizing: border-box;
    }}
    body::before {{
        content: "";
        position: absolute;
        top: 9mm;
        bottom: 9mm;
        left: 9mm;
        right: 9mm;
        border: 1.5pt solid #2d2a4a;
        pointer-events: none;
        box-sizing: border-box;
        z-index: 100;
    }}
    .header {{
        display: flex;
        align-items: center;
        gap: 16px;
        padding-bottom: 12px;
        border-bottom: 1px solid #e9ecef;
    }}
    .header-logo {{
        width: 60px;
        height: 60px;
        border-radius: 50%;
        object-fit: contain;
    }}
    .header-text {{
        display: flex;
        flex-direction: column;
        gap: 2px;
    }}
    .univ-name {{
        font-size: 11pt;
        font-weight: 800;
        color: #3b3270;
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }}
    .dept-name {{
        font-size: 9.5pt;
        font-weight: 500;
        color: #5b6172;
    }}
    .course-name {{
        font-size: 9pt;
        font-weight: 600;
        color: #7c6bc4;
    }}
    .hero {{
        margin-top: 14px;
        margin-bottom: 12px;
    }}
    .project-title {{
        font-size: 23pt;
        font-weight: 800;
        color: #2d2a4a;
        letter-spacing: -0.02em;
        line-height: 1.15;
    }}
    .project-subtitle {{
        font-size: 11pt;
        font-weight: 500;
        color: #4a4f60;
        margin-top: 3px;
        margin-bottom: 8px;
    }}
    .pill-badge {{
        display: inline-block;
        background: #f3e8ff;
        color: #4a3d8f;
        font-size: 9.2pt;
        font-weight: 600;
        padding: 4px 12px;
        border-radius: 20px;
        border: 1px solid #e9d5ff;
    }}
    .section-label {{
        font-size: 8.5pt;
        font-weight: 700;
        color: #7c6bc4;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 12px;
        margin-bottom: 6px;
    }}
    .card {{
        background: #fbfbfe;
        border: 1px solid #e6e8f0;
        border-radius: 8px;
        padding: 10px 14px;
    }}
    .details-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        row-gap: 8px;
        column-gap: 20px;
    }}
    .detail-item {{
        display: flex;
        flex-direction: column;
    }}
    .detail-label {{
        font-size: 7.8pt;
        color: #8a8fa0;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 0.04em;
    }}
    .detail-value {{
        font-size: 10pt;
        font-weight: 600;
        color: #1f2433;
    }}
    .brief-text {{
        font-size: 9.5pt;
        line-height: 1.52;
        color: #1f2433;
        text-align: justify;
    }}
    .features-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        column-gap: 20px;
        row-gap: 6px;
    }}
    .feature-item {{
        font-size: 9.4pt;
        color: #1f2433;
        display: flex;
        align-items: flex-start;
        gap: 6px;
    }}
    .feature-item::before {{
        content: "•";
        color: #7c6bc4;
        font-weight: bold;
        font-size: 12pt;
        line-height: 1;
    }}
    .links-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
    }}
    .link-card {{
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 9px 14px;
    }}
    .link-tag {{
        font-size: 7.8pt;
        font-weight: 700;
        color: #7c6bc4;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 2px;
    }}
    .link-url {{
        font-size: 8.8pt;
        font-weight: 600;
        color: #1d7770;
        text-decoration: underline;
        word-break: break-all;
    }}
</style>
</head>
<body>

<div class="header">
    <img src="data:image/png;base64,{logo_b64}" class="header-logo" alt="MIT ADT University">
    <div class="header-text">
        <div class="univ-name">MIT ADT UNIVERSITY, PUNE</div>
        <div class="dept-name">Department of Computer Science and Engineering</div>
        <div class="course-name">Generative AI · Mini Project · 2026–2027</div>
    </div>
</div>

<div class="hero">
    <div class="project-title">DataPulse AI</div>
    <div class="project-subtitle">Autonomous CSV Dataset Profiler, ML Task Recommender & Generative AI Studio</div>
    <div class="pill-badge">Problem Statement P10 · CSV Dataset Insight & Task Recommender</div>
</div>

<div class="section-label">STUDENT DETAILS</div>
<div class="card">
    <div class="details-grid">
        <div class="detail-item">
            <span class="detail-label">Student Name</span>
            <span class="detail-value">Atharva Shelar</span>
        </div>
        <div class="detail-item">
            <span class="detail-label">Roll Number</span>
            <span class="detail-value">10</span>
        </div>
        <div class="detail-item">
            <span class="detail-label">Enrollment Number</span>
            <span class="detail-value">ADT23SOCB0244</span>
        </div>
        <div class="detail-item">
            <span class="detail-label">Class / Division</span>
            <span class="detail-value">LY-AIA-3</span>
        </div>
        <div class="detail-item" style="grid-column: span 2;">
            <span class="detail-label">Faculty Guide</span>
            <span class="detail-value">Dr. Snehlata Funde</span>
        </div>
    </div>
</div>

<div class="section-label">PROJECT BRIEF</div>
<div class="card">
    <p class="brief-text">
        DataPulse AI is an autonomous, production-grade tabular dataset profiler and machine learning task recommender built to streamline the entire exploratory data science lifecycle. Users upload any arbitrary CSV dataset to receive immediate structural insights, data health scoring (penalizing missingness, duplicates, and outliers), and heuristic ML problem classification (Supervised Regression, Binary or Multiclass Classification, or Unsupervised Clustering). The system integrates a sandboxed LLM code assistant that writes, strictly AST-validates, and runs pandas transformations with automatic narrative interpretations. To bridge multimodal and generative capabilities, columns are semantically clustered using Sentence-BERT embeddings, synthetic tabular samples are generated and distribution-validated using a PyTorch CTGAN generator, and automated Responsible AI audits proactively detect PII leaks and critical class imbalances.
    </p>
</div>

<div class="section-label">KEY FEATURES</div>
<div class="card">
    <div class="features-grid">
        <div class="feature-item"><span>Statistical column profiling & ML lifecycle recommendation (U1)</span></div>
        <div class="feature-item"><span>PyTorch CTGAN synthetic tabular generation & KS benchmark (U4)</span></div>
        <div class="feature-item"><span>Sandboxed LLM pandas code generation & safe AST execution (U2)</span></div>
        <div class="feature-item"><span>Responsible AI audit: PII detection & class imbalance (U5)</span></div>
        <div class="feature-item"><span>Sentence-BERT column clustering & Vision LLM charts (U3)</span></div>
        <div class="feature-item"><span>Built with Python 3.12, PyTorch, and Streamlit Community Cloud</span></div>
    </div>
</div>

<div class="section-label">PROJECT LINKS</div>
<div class="links-grid">
    <div class="link-card">
        <div class="link-tag">LIVE APPLICATION</div>
        <a href="https://datapulse-ai-p10.streamlit.app/" class="link-url">https://datapulse-ai-p10.streamlit.app/</a>
    </div>
    <div class="link-card">
        <div class="link-tag">GITHUB REPOSITORY</div>
        <a href="https://github.com/atharva1145/Datapulse-ai-p10" class="link-url">https://github.com/atharva1145/Datapulse-ai-p10</a>
    </div>
</div>

</body>
</html>
"""
    with open('templates/summary_sheet.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('file:///' + os.path.abspath('templates/summary_sheet.html').replace('\\', '/'))
        page.pdf(
            path='10_Atharva_Shelar_1Pager.pdf',
            format='A4',
            print_background=True,
            margin={'top': '0mm', 'bottom': '0mm', 'left': '0mm', 'right': '0mm'}
        )
        browser.close()
    print("Successfully generated 10_Atharva_Shelar_1Pager.pdf")

if __name__ == '__main__':
    generate_1pager()
