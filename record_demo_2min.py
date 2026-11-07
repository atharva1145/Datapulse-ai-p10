"""
Automated 2-Minute Demo Recording for DataPulse AI
Student: Atharva Shelar | Roll No: 10 | P10
Covers all 6 core modules with clear pauses for evaluator readability.
Outputs: 10_Atharva_Shelar_Demo.mp4 (locally only, NOT pushed to git)
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
        width: 20px; height: 20px;
        border-radius: 50%;
        background: rgba(220, 38, 38, 0.80);
        border: 2.5px solid #ffffff;
        pointer-events: none;
        z-index: 999999;
        transform: translate(-50%, -50%);
        box-shadow: 0 2px 12px rgba(0,0,0,0.5);
        transition: transform 0.12s ease, background 0.15s;
        top: 0; left: 0;
    `;
    document.body.appendChild(dot);
    window._cx = 200; window._cy = 200;
    window.addEventListener('mousemove', e => {
        window._cx = e.clientX; window._cy = e.clientY;
        dot.style.left = e.clientX + 'px';
        dot.style.top  = e.clientY + 'px';
    });
    window.addEventListener('mousedown', () => {
        dot.style.transform = 'translate(-50%, -50%) scale(0.65)';
        dot.style.background = 'rgba(22, 163, 74, 0.90)';
    });
    window.addEventListener('mouseup', () => {
        dot.style.transform = 'translate(-50%, -50%) scale(1)';
        dot.style.background = 'rgba(220, 38, 38, 0.80)';
    });
})();
"""

def inject(page):
    try: page.evaluate(CURSOR_JS)
    except: pass

def move(page, tx, ty, steps=22, delay=0.016):
    inject(page)
    pos = page.evaluate("() => ({ x: window._cx||200, y: window._cy||200 })")
    sx, sy = pos['x'], pos['y']
    for i in range(1, steps + 1):
        t = i / steps
        page.mouse.move(sx + (tx - sx) * t, sy + (ty - sy) * t)
        time.sleep(delay)

def scroll_to(page, target_y, steps=28, delay=0.025):
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
    if msg: print(f"   ⏳ Pausing {secs}s — {msg}")
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

def record():
    video_dir = Path("video_recordings")
    video_dir.mkdir(exist_ok=True)

    print("=" * 55)
    print("🎬 DataPulse AI — 6 Core Modules Demo Recording")
    print("   Atharva Shelar | Roll No: 10 | P10")
    print("   Resolution: 1920×1080 Full HD | Audio: Silent")
    print("=" * 55)

    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            headless=True,
            args=["--disable-infobars", "--no-sandbox"]
        )
        ctx = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            record_video_dir=str(video_dir),
            record_video_size={"width": 1920, "height": 1080}
        )
        page = ctx.new_page()

        # ── App Load ──────────────────────────────────────────
        print("\n▶ [SCENE 1 — 0:00] App launch & dataset ingestion")
        page.goto("http://localhost:8501", timeout=30000)
        page.wait_for_timeout(4500)
        inject(page)

        # Hover brand card
        move(page, 180, 68)
        pause(2.5, "Brand card — DataPulse AI · Autonomous ML Engine")

        # Click Titanic
        titanic = page.locator("button:has-text('Titanic')").first
        if titanic.count() > 0:
            click_loc(page, titanic, wait=0)
            print("   ✓ Clicked Titanic benchmark")
            page.wait_for_timeout(4000)
            inject(page)

        # Hover ACTIVE DATASET status box
        move(page, 180, 290)
        pause(3.0, "Active dataset → 891 rows · 12 features")

        # ── Visual Analytics ──────────────────────────────────
        print("\n▶ [SCENE 2 — 0:25] Visual Analytics & Health Scorecard")
        inject(page)

        # Tab 1: Health scorecard
        move(page, 760, 200)
        pause(2.5, "Health Scorecard — 90.5 / 100")

        scroll_to(page, 350)
        pause(2.5, "Missing Values & Hygiene audit cards")

        scroll_to(page, 0)
        pause(0.5)

        # Tab 2: Univariate distributions
        tab2 = page.locator("button:has-text('Univariate')").first
        if tab2.count() == 0:
            tab2 = page.locator("[role='tab']:has-text('Univariate')").first
        if tab2.count() > 0 and tab2.is_visible():
            click_loc(page, tab2, wait=1.5)
            inject(page)
            print("   ✓ Switched to Univariate Distributions tab")
        scroll_to(page, 350)
        pause(2.5, "Numerical distribution histogram / KDE")

        # Tab 3: Correlation heatmap
        scroll_to(page, 0)
        tab3 = page.locator("button:has-text('Correlation')").first
        if tab3.count() == 0:
            tab3 = page.locator("[role='tab']:has-text('Correlation')").first
        if tab3.count() > 0 and tab3.is_visible():
            click_loc(page, tab3, wait=1.5)
            inject(page)
            print("   ✓ Switched to Correlation Heatmap tab")
        scroll_to(page, 400)
        pause(3.0, "Pearson Correlation Matrix — centred on screen")

        # ── ML Recommendations ────────────────────────────────
        print("\n▶ [SCENE 3 — 0:55] ML Task Recommender & 10-Stage Lifecycle")
        nav_to(page, "ML")

        move(page, 760, 200)
        pause(2.5, "Detected: Binary Classification (Target: Survived)")

        scroll_to(page, 350)
        pause(2.5, "Candidate algorithms — RF, XGBoost, Logistic Reg")

        scroll_to(page, 700)
        pause(2.5, "Evaluation metrics — ROC-AUC, F1, Precision/Recall")

        scroll_to(page, 1050)
        pause(3.0, "10-Stage ML Lifecycle Roadmap")

        # ── AI Data Assistant ─────────────────────────────────
        print("\n▶ [SCENE 4 — 1:30] AI Data Assistant & AST Sandbox")
        nav_to(page, "AI Data Assistant")

        q_missingness = page.locator("button:has-text('missingness')").first
        q_top5 = page.locator("button:has-text('Top 5')").first
        for q in [q_top5, q_missingness]:
            if q.count() > 0 and q.is_visible():
                click_loc(page, q, wait=1.0)
                print("   ✓ Selected quick question")
                break

        run_btn = page.locator("button:has-text('Run AI Query')").first
        if run_btn.count() > 0 and run_btn.is_visible():
            click_loc(page, run_btn, wait=0)
            print("   ✓ Clicked Run AI Query")
            page.wait_for_timeout(5000)
            inject(page)

        scroll_to(page, 350)
        pause(2.5, "Generated Pandas code shown")

        scroll_to(page, 650)
        pause(3.0, "AST Security Validation badge & safe output")

        # ── Column Intelligence ───────────────────────────────
        print("\n▶ [SCENE 5 — 1:55] Column Intelligence & Sentence-BERT")
        nav_to(page, "Column Intelligence")

        move(page, 760, 220)
        pause(2.5, "Sentence-BERT column clustering")

        scroll_to(page, 450)
        pause(3.0, "Semantic groupings — numeric, identifier, categorical")

        # ── Synthetic Data Lab ────────────────────────────────
        print("\n▶ [SCENE 6 — 2:15] Synthetic Data Lab — PyTorch CTGAN")
        nav_to(page, "Synthetic Data Lab")

        move(page, 760, 200)
        pause(2.0, "CTGAN training parameters")

        scroll_to(page, 400)
        pause(2.5, "Real vs Synthetic distribution overlay charts")

        scroll_to(page, 750)
        pause(3.0, "KS Score: Titanic 0.281 — statistical fidelity proven")

        # ── Responsible AI ────────────────────────────────────
        print("\n▶ [SCENE 7 — 2:40] Responsible AI — PII & Imbalance Audit")
        nav_to(page, "Responsible AI")

        move(page, 760, 220)
        pause(2.5, "Responsible AI dashboard")

        scroll_to(page, 400)
        pause(3.0, "PII detection & class imbalance audit — Titanic 1.61:1")

        # Concluding overview on Visual Analytics
        print("\n▶ [WRAP UP] Concluding Overview")
        nav_to(page, "Visual Analytics")
        move(page, 760, 210)
        pause(3.0, "Overview hold: Titanic Survival Dataset (Health: 90.5/100)")

        # Finish recording
        pause(1.5)
        page.close()
        ctx.close()
        browser.close()

    print("\n✔ Playwright recording done!")

    webms = glob.glob(str(video_dir / "*.webm"))
    if not webms:
        print("❌ No webm found in", video_dir)
        return

    webm = max(webms, key=os.path.getctime)
    print(f"   Raw WebM: {webm}")

    mp4_out = "10_Atharva_Shelar_Demo.mp4"
    sub_out  = Path("10_Atharva_Shelar") / mp4_out

    print(f"\n🔧 Converting → {mp4_out} (H.264 / 1080p) ...")
    cmd = [
        "ffmpeg", "-y",
        "-i", webm,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "20",
        "-pix_fmt", "yuv420p",
        mp4_out
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ ffmpeg error:", result.stderr[-400:])
        return

    size_mb = os.path.getsize(mp4_out) / 1_048_576
    print(f"✔ Generated {mp4_out} ({size_mb:.1f} MB)")

    import shutil
    shutil.copy(mp4_out, str(sub_out))
    print(f"✔ Copied to {sub_out}")

    print("\n📁 Final submission folder contents:")
    for f in sorted(Path("10_Atharva_Shelar").iterdir()):
        sz = f.stat().st_size / 1_048_576
        print(f"   {f.name:<45} {sz:.2f} MB")

    print("\n🎉 DONE! No git push performed.")

if __name__ == "__main__":
    record()
