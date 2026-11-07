"""
Automated Screen Recording Generator for DataPulse AI Demo Video
Student: Atharva Shelar | Roll No: 10 | P10
Generates high-definition (1080p) MP4 video following the exact 2-minute scene script.
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

CURSOR_SCRIPT = """
(() => {
    if (document.getElementById('playwright-cursor')) return;
    const box = document.createElement('div');
    box.id = 'playwright-cursor';
    box.style.position = 'fixed';
    box.style.top = '0px';
    box.style.left = '0px';
    box.style.width = '22px';
    box.style.height = '22px';
    box.style.borderRadius = '50%';
    box.style.backgroundColor = 'rgba(239, 68, 68, 0.75)';
    box.style.border = '2px solid #ffffff';
    box.style.pointerEvents = 'none';
    box.style.zIndex = '999999';
    box.style.transition = 'transform 0.15s ease-out, background-color 0.2s';
    box.style.transform = 'translate(-50%, -50%)';
    box.style.boxShadow = '0 0 10px rgba(0,0,0,0.45)';
    document.body.appendChild(box);

    window.__cursorX = 100;
    window.__cursorY = 100;

    window.addEventListener('mousemove', (e) => {
        window.__cursorX = e.clientX;
        window.__cursorY = e.clientY;
        box.style.left = e.clientX + 'px';
        box.style.top = e.clientY + 'px';
    });
    window.addEventListener('mousedown', () => {
        box.style.transform = 'translate(-50%, -50%) scale(0.7)';
        box.style.backgroundColor = 'rgba(34, 197, 94, 0.9)';
    });
    window.addEventListener('mouseup', () => {
        box.style.transform = 'translate(-50%, -50%) scale(1)';
        box.style.backgroundColor = 'rgba(239, 68, 68, 0.75)';
    });
})();
"""

def inject_cursor(page):
    try:
        page.evaluate(CURSOR_SCRIPT)
    except Exception:
        pass

def smooth_move(page, target_x, target_y, steps=20, delay=0.015):
    inject_cursor(page)
    pos = page.evaluate("() => ({ x: window.__cursorX || 100, y: window.__cursorY || 100 })")
    start_x, start_y = pos["x"], pos["y"]
    for i in range(1, steps + 1):
        t = i / steps
        cur_x = start_x + (target_x - start_x) * t
        cur_y = start_y + (target_y - start_y) * t
        page.mouse.move(cur_x, cur_y)
        time.sleep(delay)

def smooth_scroll(page, target_scroll_y, steps=25, delay=0.025):
    inject_cursor(page)
    current_scroll = page.evaluate("() => window.scrollY || 0")
    for i in range(1, steps + 1):
        t = i / steps
        y = current_scroll + (target_scroll_y - current_scroll) * t
        page.evaluate(f"window.scrollTo(0, {y})")
        time.sleep(delay)

def click_element_smoothly(page, locator):
    inject_cursor(page)
    box = locator.bounding_box()
    if box:
        cx = box["x"] + box["width"] / 2
        cy = box["y"] + box["height"] / 2
        smooth_move(page, cx, cy)
        time.sleep(0.3)
        page.mouse.down()
        time.sleep(0.15)
        page.mouse.up()
        time.sleep(0.4)
    else:
        locator.click()

def record_demo():
    video_dir = Path("video_recordings")
    video_dir.mkdir(exist_ok=True)

    print("==================================================")
    print("🎬 STARTING AUTOMATED DEMO RECORDING FOR DATAPULSE AI")
    print("Student: Atharva Shelar | Roll: 10 | Problem P10")
    print("Resolution: 1920x1080 Full HD (Silent Audio)")
    print("==================================================")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--start-maximized", "--disable-infobars"]
        )
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            record_video_dir=str(video_dir),
            record_video_size={"width": 1920, "height": 1080}
        )

        page = context.new_page()
        page.goto("http://localhost:8501", timeout=30000)
        page.wait_for_timeout(4000)
        inject_cursor(page)

        # ----------------------------------------------------
        # SCENE 1: App Header & Fast Dataset Load (0:00 - 0:20)
        # ----------------------------------------------------
        print("▶ [Scene 1] App Header & Loading Titanic Benchmark...")
        smooth_move(page, 180, 70, steps=20)
        page.wait_for_timeout(2000)

        # Click Titanic button under Fast Benchmarks
        titanic_btn = page.locator("button:has-text('Titanic')").first
        if titanic_btn.is_visible():
            click_element_smoothly(page, titanic_btn)
            page.wait_for_timeout(4000)
            inject_cursor(page)
        else:
            print("Titanic button not immediately found; trying fallback button")

        # Move cursor to the green ACTIVE DATASET box
        smooth_move(page, 180, 290, steps=20)
        page.wait_for_timeout(3000)

        # ----------------------------------------------------
        # SCENE 2: Visual Analytics & Health Scorecard (0:20 - 0:50)
        # ----------------------------------------------------
        print("▶ [Scene 2] Visual Analytics & Quality Scorecard...")
        inject_cursor(page)
        # Hover over Health Scorecard
        smooth_move(page, 750, 220, steps=25)
        page.wait_for_timeout(2500)

        # Scroll gently down
        smooth_scroll(page, 400, steps=20)
        page.wait_for_timeout(2500)

        # Switch to Tab 2: Univariate Distributions
        tab2 = page.locator('[data-baseweb="tab"]:has-text("Univariate")').first
        if tab2.is_visible():
            click_element_smoothly(page, tab2)
            page.wait_for_timeout(2000)
            inject_cursor(page)
            smooth_scroll(page, 550, steps=20)
            page.wait_for_timeout(3000)

        # Switch to Tab 3: Pearson Correlation Heatmap
        tab3 = page.locator('[data-baseweb="tab"]:has-text("Correlation")').first
        if tab3.is_visible():
            smooth_scroll(page, 200, steps=15)
            click_element_smoothly(page, tab3)
            page.wait_for_timeout(2000)
            inject_cursor(page)
            smooth_scroll(page, 500, steps=20)
            page.wait_for_timeout(3500)

        # ----------------------------------------------------
        # SCENE 3: ML Task Recommender & Lifecycle (0:50 - 1:15)
        # ----------------------------------------------------
        print("▶ [Scene 3] ML Task Recommender & 10-Stage Lifecycle...")
        smooth_scroll(page, 0, steps=15)
        ml_nav = page.locator("a:has-text('ML')").first
        if ml_nav.is_visible():
            click_element_smoothly(page, ml_nav)
            page.wait_for_timeout(3000)
            inject_cursor(page)

            # Hover over detected task card
            smooth_move(page, 700, 230, steps=20)
            page.wait_for_timeout(3000)

            # Scroll down to show candidate algorithms & metrics
            smooth_scroll(page, 450, steps=25)
            page.wait_for_timeout(3000)

            # Scroll down to show 10-stage ML roadmap
            smooth_scroll(page, 850, steps=25)
            page.wait_for_timeout(3500)

        # ----------------------------------------------------
        # SCENE 4: AI Data Assistant (1:15 - 1:40)
        # ----------------------------------------------------
        print("▶ [Scene 4] AI Data Assistant & AST Sandboxed Execution...")
        smooth_scroll(page, 0, steps=15)
        assistant_nav = page.locator("a:has-text('AI Data Assistant')").first
        if assistant_nav.is_visible():
            click_element_smoothly(page, assistant_nav)
            page.wait_for_timeout(3000)
            inject_cursor(page)

            # Click quick example question: Top 5 records
            top5_btn = page.locator("button:has-text('Top 5 records')").first
            if top5_btn.is_visible():
                click_element_smoothly(page, top5_btn)
                page.wait_for_timeout(1500)

            # Click Run AI Query button
            run_btn = page.locator("button:has-text('Run AI Query')").first
            if run_btn.is_visible():
                click_element_smoothly(page, run_btn)
                page.wait_for_timeout(5000)
                inject_cursor(page)

                # Scroll down to see generated code & AST badge
                smooth_scroll(page, 550, steps=25)
                page.wait_for_timeout(4000)

        # ----------------------------------------------------
        # SCENE 5: Synthetic Data Lab (1:40 - 2:00)
        # ----------------------------------------------------
        print("▶ [Scene 5] Synthetic Data Lab & PyTorch CTGAN...")
        smooth_scroll(page, 0, steps=15)
        synth_nav = page.locator("a:has-text('Synthetic Data Lab')").first
        if synth_nav.is_visible():
            click_element_smoothly(page, synth_nav)
            page.wait_for_timeout(3000)
            inject_cursor(page)

            # Scroll down to show CTGAN configurations and distributions
            smooth_scroll(page, 450, steps=25)
            page.wait_for_timeout(4000)

        # ----------------------------------------------------
        # SCENE 6: Final Report & Wrap Up (2:00 - 2:15)
        # ----------------------------------------------------
        print("▶ [Scene 6] Final Report & Deliverables Wrap-up...")
        smooth_scroll(page, 0, steps=15)
        final_nav = page.locator("a:has-text('Final')").first
        if final_nav.is_visible():
            click_element_smoothly(page, final_nav)
            page.wait_for_timeout(3000)
            inject_cursor(page)

            # Scroll down to show student info card
            smooth_scroll(page, 350, steps=20)
            page.wait_for_timeout(2500)

            # Hover over Download Report button
            dl_btn = page.locator("button:has-text('Download')").first
            if dl_btn.is_visible():
                smooth_move(page, 750, 500, steps=20)
                page.wait_for_timeout(4000)
            else:
                page.wait_for_timeout(3000)

        # Close page and context to finalize video writing
        page.wait_for_timeout(1000)
        page.close()
        context.close()
        browser.close()

    print("✔ Playwright recording finished!")
    recorded_webms = glob.glob(str(video_dir / "*.webm"))
    if not recorded_webms:
        print("❌ No recorded video found in", video_dir)
        return

    latest_webm = max(recorded_webms, key=os.path.getctime)
    print("Raw video recorded at:", latest_webm)

    # Convert to MP4 using ffmpeg
    mp4_target = "10_Atharva_Shelar_Demo.mp4"
    sub_target = Path("10_Atharva_Shelar") / "10_Atharva_Shelar_Demo.mp4"
    
    print(f"Converting to {mp4_target} with ffmpeg (H.264 / 1080p)...")
    cmd = [
        "ffmpeg", "-y",
        "-i", latest_webm,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "22",
        "-pix_fmt", "yuv420p",
        mp4_target
    ]
    subprocess.run(cmd, check=True)
    print(f"✔ Generated {mp4_target} successfully!")

    # Copy to submission folder
    if Path("10_Atharva_Shelar").exists():
        import shutil
        shutil.copy(mp4_target, str(sub_target))
        print(f"✔ Copied to {sub_target}!")

if __name__ == '__main__':
    record_demo()
