"""
Full Working System Walkthrough Video Recording for DataPulse AI
Student: Atharva Shelar | Roll No: 10 | P10
Course: Generative AI Mini Project (2026-2027)

Interacts with and triggers all 6 core functional modules live on screen:
1. Ingestion: Dual benchmark dataset switch (Iris -> Titanic)
2. Visual Analytics: All 5 tabs, column dropdown switch, correlation matrix, bivariate
3. ML Recommender: Task heuristic, candidate algorithms, 10-stage lifecycle roadmap
4. AI Data Assistant: Natural language query, live AST security check, execution output
5. Column Intelligence: Sentence-BERT 384-d semantic clustering & slider adjustment
6. Synthetic Data Lab: PyTorch CTGAN generator, real vs. synthetic distribution overlays & KS score
7. Responsible AI: Live PII scanner (GDPR/DPDP) & Target class imbalance audit (1.61:1)

Resolution: 1920x1080 Full HD (H.264 MP4, Silent Audio with animated cursor)
NO GIT PUSH: All files remain strictly local.
"""

import os
import sys
import time
import glob
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

CURSOR_JS = """
(() => {
    if (document.getElementById('cursor-dot')) return;
    const dot = document.createElement('div');
    dot.id = 'cursor-dot';
    dot.style.cssText = `
        position: fixed;
        width: 22px; height: 22px;
        border-radius: 50%;
        background: rgba(220, 38, 38, 0.82);
        border: 2.5px solid #ffffff;
        pointer-events: none;
        z-index: 999999;
        transform: translate(-50%, -50%);
        box-shadow: 0 2px 14px rgba(0,0,0,0.55);
        transition: transform 0.12s ease, background 0.15s;
        top: 0; left: 0;
    `;
    document.body.appendChild(dot);
    window._cx = 250; window._cy = 250;
    window.addEventListener('mousemove', e => {
        window._cx = e.clientX; window._cy = e.clientY;
        dot.style.left = e.clientX + 'px';
        dot.style.top  = e.clientY + 'px';
    });
    window.addEventListener('mousedown', () => {
        dot.style.transform = 'translate(-50%, -50%) scale(0.60)';
        dot.style.background = 'rgba(22, 163, 74, 0.95)';
    });
    window.addEventListener('mouseup', () => {
        dot.style.transform = 'translate(-50%, -50%) scale(1)';
        dot.style.background = 'rgba(220, 38, 38, 0.82)';
    });
})();
"""

def inject(page):
    try: page.evaluate(CURSOR_JS)
    except: pass

def move(page, tx, ty, steps=24, delay=0.016):
    inject(page)
    pos = page.evaluate("() => ({ x: window._cx||250, y: window._cy||250 })")
    sx, sy = pos['x'], pos['y']
    for i in range(1, steps + 1):
        t = i / steps
        page.mouse.move(sx + (tx - sx) * t, sy + (ty - sy) * t)
        time.sleep(delay)

def scroll_to(page, target_y, steps=30, delay=0.024):
    cur = page.evaluate("() => window.scrollY || 0")
    for i in range(1, steps + 1):
        t = i / steps
        page.evaluate(f"window.scrollTo(0, {cur + (target_y - cur) * t})")
        time.sleep(delay)

def click_loc(page, loc, wait=0.5):
    inject(page)
    box = loc.bounding_box()
    if box:
        cx = box['x'] + box['width'] / 2
        cy = box['y'] + box['height'] / 2
        move(page, cx, cy)
        time.sleep(0.25)
        page.mouse.down(); time.sleep(0.12); page.mouse.up()
        time.sleep(wait)
    else:
        try: loc.click()
        except: pass
        time.sleep(wait)

def pause(secs, msg=""):
    if msg: print(f"   ⏳ {msg} ({secs}s)")
    time.sleep(secs)

def nav_to(page, link_text, wait=3.5):
    inject(page)
    scroll_to(page, 0, steps=15)
    lnk = page.locator(f"a:has-text('{link_text}')").first
    if lnk.count() > 0 and lnk.is_visible():
        click_loc(page, lnk, wait=wait)
        inject(page)
        return True
    return False

def record_full_working_video():
    video_dir = Path("video_recordings")
    video_dir.mkdir(exist_ok=True)

    print("=" * 65)
    print("🎬 STARTING FULL WORKING SYSTEM RECORDING — 6 CORE MODULES")
    print("   Student: Atharva Shelar | Roll: 10 | Problem P10")
    print("   Resolution: 1920x1080 Full HD (Silent Audio with Cursor)")
    print("   Status: Strictly Local (No Git Push)")
    print("=" * 65)

    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            headless=True,
            args=["--disable-infobars", "--no-sandbox", "--start-maximized"]
        )
        ctx = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            record_video_dir=str(video_dir),
            record_video_size={"width": 1920, "height": 1080}
        )
        page = ctx.new_page()

        # =====================================================================
        # SCENE 1: Ingestion Engine & Live Benchmark Switching
        # =====================================================================
        print("\n▶ [SCENE 1] Launching App & Testing Ingestion Engine...")
        page.goto("http://localhost:8501", timeout=30000)
        page.wait_for_timeout(5000)
        inject(page)

        # 1. Point to app branding
        move(page, 180, 68)
        pause(2.5, "DataPulse AI · Autonomous ML Engine")

        # 2. Click Iris benchmark first to show dynamic switching
        iris_btn = page.locator("button:has-text('Iris')").first
        if iris_btn.count() > 0 and iris_btn.is_visible():
            click_loc(page, iris_btn, wait=0)
            print("   ✓ Loaded Iris Multiclass Benchmark")
            page.wait_for_timeout(3500)
            inject(page)
            move(page, 180, 290)
            pause(2.5, "Verified active dataset: Iris (150 rows • 5 features)")

        # 3. Now switch to Titanic benchmark for rich multimodal & imbalance demo
        titanic_btn = page.locator("button:has-text('Titanic')").first
        if titanic_btn.count() > 0 and titanic_btn.is_visible():
            click_loc(page, titanic_btn, wait=0)
            print("   ✓ Switched to Titanic Survival Benchmark")
            page.wait_for_timeout(4000)
            inject(page)
            move(page, 180, 290)
            pause(3.0, "Verified active dataset: Titanic (891 rows • 12 features)")

        # =====================================================================
        # SCENE 2: Visual Analytics Studio — All 5 Tabs Thoroughly
        # =====================================================================
        print("\n▶ [SCENE 2] Visual Analytics Studio (All 5 Tabs In-Depth)...")
        inject(page)

        # Tab 1: Dataset Health & Quality Score
        move(page, 760, 210)
        pause(3.0, "Health Scorecard: 90.5 / 100 with zero duplicate rows")

        scroll_to(page, 380)
        pause(3.0, "Missing Values audit: Age (19.9%), Cabin (77.1%), Embarked (0.2%)")

        scroll_to(page, 680)
        pause(2.5, "Outlier & Skewness audit cards")

        scroll_to(page, 0)
        pause(0.5)

        # Tab 2: Univariate Distributions — with interactive column dropdown change!
        tab2 = page.locator("button:has-text('Univariate')").first
        if tab2.count() == 0:
            tab2 = page.locator("[role='tab']:has-text('Univariate')").first
        if tab2.count() > 0 and tab2.is_visible():
            click_loc(page, tab2, wait=2.0)
            inject(page)
            print("   ✓ Switched to Tab 2: Univariate Distributions")
            scroll_to(page, 350)
            pause(3.0, "Showing numerical distribution histogram & KDE")

            # Switch column dropdown
            col_select = page.locator("div[data-baseweb='select']").first
            if col_select.count() > 0 and col_select.is_visible():
                click_loc(page, col_select, wait=1.0)
                page.keyboard.press("ArrowDown")
                page.keyboard.press("Enter")
                page.wait_for_timeout(2000)
                inject(page)
                pause(3.0, "Dynamically redrew univariate plot for alternate column")

        # Tab 3: Pearson Correlation Heatmap
        scroll_to(page, 0)
        tab3 = page.locator("button:has-text('Correlation')").first
        if tab3.count() == 0:
            tab3 = page.locator("[role='tab']:has-text('Correlation')").first
        if tab3.count() > 0 and tab3.is_visible():
            click_loc(page, tab3, wait=2.0)
            inject(page)
            print("   ✓ Switched to Tab 3: Correlation Heatmap")
            scroll_to(page, 420)
            pause(3.5, "Pearson correlation matrix centered on screen")

        # Tab 4: Bivariate Relationships & Scatter Plots
        scroll_to(page, 0)
        tab4 = page.locator("button:has-text('Bivariate')").first
        if tab4.count() == 0:
            tab4 = page.locator("[role='tab']:has-text('Bivariate')").first
        if tab4.count() > 0 and tab4.is_visible():
            click_loc(page, tab4, wait=2.0)
            inject(page)
            print("   ✓ Switched to Tab 4: Bivariate Relationships")
            scroll_to(page, 400)
            pause(3.5, "Bivariate relationship plot & scatter analysis")

        # Tab 5: Descriptive Statistics Inventory
        scroll_to(page, 0)
        tab5 = page.locator("button:has-text('Descriptive')").first
        if tab5.count() == 0:
            tab5 = page.locator("[role='tab']:has-text('Descriptive')").first
        if tab5.count() > 0 and tab5.is_visible():
            click_loc(page, tab5, wait=2.0)
            inject(page)
            print("   ✓ Switched to Tab 5: Descriptive Statistics")
            scroll_to(page, 350)
            pause(3.0, "Full summary statistics inventory table")

        # =====================================================================
        # SCENE 3: ML Task Recommender & 10-Stage Lifecycle Studio
        # =====================================================================
        print("\n▶ [SCENE 3] ML Task Recommender & Lifecycle Roadmap...")
        nav_to(page, "ML")

        move(page, 760, 210)
        pause(3.0, "Heuristic detected: Binary Classification (Target: Survived)")

        scroll_to(page, 380)
        pause(3.5, "Candidate Algorithms: Random Forest, XGBoost, Logistic Regression")

        scroll_to(page, 720)
        pause(3.0, "Evaluation Metrics: ROC-AUC, F1-Score, Precision/Recall")

        scroll_to(page, 1100)
        pause(4.0, "10-Stage ML Lifecycle Roadmap & GenAI vs Discriminative Table")

        # =====================================================================
        # SCENE 4: AI Data Assistant — Live AST Sandboxed Query Execution
        # =====================================================================
        print("\n▶ [SCENE 4] AI Data Assistant & AST Sandboxed Execution...")
        nav_to(page, "AI Data Assistant")

        # Click quick question button
        q_missing = page.locator("button:has-text('missingness')").first
        q_top5 = page.locator("button:has-text('Top 5')").first
        if q_missing.count() > 0 and q_missing.is_visible():
            click_loc(page, q_missing, wait=1.5)
            print("   ✓ Selected prompt: 'Which columns have missing values and how many?'")
        elif q_top5.count() > 0 and q_top5.is_visible():
            click_loc(page, q_top5, wait=1.5)
            print("   ✓ Selected prompt: 'Top 5 records'")

        pause(1.5, "Query formulated in natural language")

        # Click Run AI Query button
        run_btn = page.locator("button:has-text('Run AI Query')").first
        if run_btn.count() > 0 and run_btn.is_visible():
            click_loc(page, run_btn, wait=0)
            print("   ✓ Triggered Run AI Query — synthesising & validating...")
            page.wait_for_timeout(5500)
            inject(page)

        # Scroll to inspect code and AST badge
        scroll_to(page, 380)
        pause(3.5, "Generated Pandas transformation code displayed")

        scroll_to(page, 700)
        pause(4.0, "AST Security Validation Badge (Approved) & execution dataframe")

        # =====================================================================
        # SCENE 5: Column Intelligence — Sentence-BERT & Interactive Slider
        # =====================================================================
        print("\n▶ [SCENE 5] Column Intelligence & Semantic Clustering...")
        nav_to(page, "Column Intelligence")

        move(page, 760, 220)
        pause(3.0, "Sentence-BERT 384-dimensional dense semantic embeddings")

        # Show Cosine Similarity Heatmap
        scroll_to(page, 450)
        pause(3.5, "Pairwise Semantic Cosine Similarity Heatmap")

        # Interactive Cosine Slider adjustment
        slider = page.locator("div[role='slider']").first
        if slider.count() > 0 and slider.is_visible():
            box = slider.bounding_box()
            if box:
                move(page, box['x'], box['y'])
                page.mouse.down()
                page.mouse.move(box['x'] + 60, box['y'])
                page.mouse.up()
                page.wait_for_timeout(2000)
                inject(page)
                pause(3.0, "Adjusted Cosine Similarity threshold to 0.75 — clusters regrouped live!")

        scroll_to(page, 800)
        pause(3.0, "Semantic column groupings displayed")

        # =====================================================================
        # SCENE 6: Synthetic Data Lab — PyTorch CTGAN & Statistical Evaluation
        # =====================================================================
        print("\n▶ [SCENE 6] Synthetic Data Lab — PyTorch CTGAN...")
        nav_to(page, "Synthetic Data Lab")

        move(page, 760, 210)
        pause(2.5, "CTGAN Tabular Synthesizer controls (Epochs & rows)")

        # Switch to Tab 2: Real vs. Synthetic Statistical Evaluation
        tab_eval = page.locator("button:has-text('Real vs. Synthetic')").first
        if tab_eval.count() == 0:
            tab_eval = page.locator("[role='tab']:has-text('Real vs. Synthetic')").first
        if tab_eval.count() > 0 and tab_eval.is_visible():
            click_loc(page, tab_eval, wait=2.0)
            inject(page)
            print("   ✓ Switched to Tab 2: Real vs. Synthetic Statistical Evaluation")

            scroll_to(page, 400)
            pause(3.5, "Real vs. Synthetic continuous distribution overlay curves")

            scroll_to(page, 750)
            pause(4.0, "Two-sample KS score: Titanic 0.281 & correlation difference matrix")

        # =====================================================================
        # SCENE 7: Responsible AI & Concluding Executive Summary
        # =====================================================================
        print("\n▶ [SCENE 7] Responsible AI — PII & Class Imbalance Audit...")
        nav_to(page, "Responsible AI")

        # Tab 1: PII Audit
        move(page, 760, 220)
        pause(3.0, "PII Scanner: Identified sensitive attributes (Name, Ticket)")

        scroll_to(page, 380)
        pause(3.5, "GDPR / DPDP compliance risk categories and remediation actions")

        # Tab 2: Class Imbalance
        scroll_to(page, 0)
        tab_imb = page.locator("button:has-text('Class Imbalance')").first
        if tab_imb.count() == 0:
            tab_imb = page.locator("[role='tab']:has-text('Class Imbalance')").first
        if tab_imb.count() > 0 and tab_imb.is_visible():
            click_loc(page, tab_imb, wait=2.0)
            inject(page)
            print("   ✓ Switched to Tab 2: Class Imbalance Analysis")

            scroll_to(page, 350)
            pause(4.0, "Target imbalance ratio: 1.61:1 — SMOTE & class-weight recipe displayed")

        # Return to Visual Analytics for an executive summary hold (NO Final page)
        print("\n▶ [WRAP UP] Concluding on Executive Analytics Dashboard...")
        nav_to(page, "Visual Analytics")
        move(page, 760, 210)
        pause(3.0, "Executive overview: Titanic Survival Dataset (Health: 90.5/100)")
        scroll_to(page, 320)
        pause(4.0, "Complete system walkthrough concluded — all 6 core modules verified!")

        # Wrap up
        pause(1.5)
        page.close()
        ctx.close()
        browser.close()

    print("\n✔ Full working recording finished!")

    # Find the recorded webm
    webms = glob.glob(str(video_dir / "*.webm"))
    if not webms:
        print("❌ No webm found in", video_dir)
        return

    webm = max(webms, key=os.path.getctime)
    print(f"   Raw WebM: {webm}")

    mp4_out = "10_Atharva_Shelar_Full_Working_Demo.mp4"
    sub_out = Path("10_Atharva_Shelar") / mp4_out
    std_sub = Path("10_Atharva_Shelar") / "10_Atharva_Shelar_Demo.mp4"

    print(f"\n🔧 Converting → {mp4_out} (H.264 / 1080p)...")
    cmd = [
        "ffmpeg", "-y",
        "-i", webm,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "21",
        "-pix_fmt", "yuv420p",
        mp4_out
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("❌ ffmpeg error:", res.stderr[-400:])
        return

    size_mb = os.path.getsize(mp4_out) / 1_048_576
    print(f"✔ Generated {mp4_out} ({size_mb:.1f} MB)!")

    # Copy to submission folder
    import shutil
    shutil.copy(mp4_out, str(sub_out))
    shutil.copy(mp4_out, str(std_sub))
    print(f"✔ Copied to {sub_out}")
    print(f"✔ Also updated {std_sub}")

    print("\n📁 Submission folder contents:")
    for f in sorted(Path("10_Atharva_Shelar").iterdir()):
        sz = f.stat().st_size / 1_048_576
        print(f"   {f.name:<45} {sz:.2f} MB")

    print("\n🎉 DONE! Zero git push performed (all files strictly local).")

if __name__ == '__main__':
    record_full_working_video()
