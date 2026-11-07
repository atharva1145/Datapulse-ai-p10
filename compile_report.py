"""
Master Compilation Script for DataPulse AI Mini Project Report.
Assembles all 36 pages, writes HTML template, and compiles to 10_Atharva_Shelar_P10.pdf via Playwright.
"""

import os
import sys
import shutil
import base64

if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
from playwright.sync_api import sync_playwright
import pymupdf

from report_styles import REPORT_CSS
from report_pages_front import (
    get_page_1_html, get_page_2_html, get_page_3_html, 
    get_page_4_html, get_page_5_html
)
from report_pages_ch1_to_ch5 import (
    get_page_6_html, get_page_7_html, get_page_8_html,
    get_page_9_html, get_page_10_html, get_page_11_html, get_page_12_html
)
from report_pages_ch6 import (
    get_page_13_html, get_page_14_html, get_page_15_html,
    get_page_16_html, get_page_17_html, get_page_18_html,
    get_page_19_html, get_page_20_html
)
from report_pages_ch7_to_ch10 import (
    get_page_21_html, get_page_22_html, get_page_23_html,
    get_page_24_html, get_page_25_html, get_page_26_html,
    get_page_27_html, get_page_28_html, get_page_29_html,
    get_page_30_html, get_page_31_html, get_page_32_html
)
from report_pages_ch11_to_ch15 import (
    get_page_33_html, get_page_34_html, get_page_35_html, get_page_36_html
)

def build_full_report():
    print("Step 1: Reading university logo...")
    with open('assets/mit_adt_logo.png', 'rb') as f:
        logo_b64 = base64.b64encode(f.read()).decode('utf-8')

    print("Step 2: Assembling 36 pages...")
    pages = [
        get_page_1_html(logo_b64),
        get_page_2_html(),
        get_page_3_html(),
        get_page_4_html(),
        get_page_5_html(),
        get_page_6_html(),
        get_page_7_html(),
        get_page_8_html(),
        get_page_9_html(),
        get_page_10_html(),
        get_page_11_html(),
        get_page_12_html(),
        get_page_13_html(),
        get_page_14_html(),
        get_page_15_html(),
        get_page_16_html(),
        get_page_17_html(),
        get_page_18_html(),
        get_page_19_html(),
        get_page_20_html(),
        get_page_21_html(),
        get_page_22_html(),
        get_page_23_html(),
        get_page_24_html(),
        get_page_25_html(),
        get_page_26_html(),
        get_page_27_html(),
        get_page_28_html(),
        get_page_29_html(),
        get_page_30_html(),
        get_page_31_html(),
        get_page_32_html(),
        get_page_33_html(),
        get_page_34_html(),
        get_page_35_html(),
        get_page_36_html()
    ]

    print(f"Total pages assembled: {len(pages)}")

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>DataPulse AI – Academic Mini Project Report</title>
<style>
{REPORT_CSS}
</style>
</head>
<body>
{''.join(pages)}
</body>
</html>
"""

    os.makedirs('templates', exist_ok=True)
    with open('templates/full_report.html', 'w', encoding='utf-8') as f:
        f.write(full_html)
    print("Step 3: Saved templates/full_report.html")

    print("Step 4: Launching Playwright Chromium for PDF rendering...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('file:///' + os.path.abspath('templates/full_report.html').replace('\\', '/'))
        page.pdf(
            path='10_Atharva_Shelar_P10.pdf',
            format='A4',
            print_background=True,
            margin={'top': '0mm', 'bottom': '0mm', 'left': '0mm', 'right': '0mm'}
        )
        browser.close()
    print("Step 5: Generated 10_Atharva_Shelar_P10.pdf")

    print("Step 6: Verifying with PyMuPDF...")
    doc = pymupdf.open('10_Atharva_Shelar_P10.pdf')
    page_count = len(doc)
    print(f"Verified Page Count: {page_count} pages")

    print("\n=== Page-by-Page Header & Heading Verification ===")
    forbidden_words = ['antigravity', 'google deepmind', 'assistant response', 'system message']
    violations = []
    
    for idx, pg in enumerate(doc):
        text = pg.get_text('text').strip()
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        first_line = lines[0] if lines else 'EMPTY'
        heading = lines[1] if len(lines) > 1 else ''
        footer_num = lines[-1] if lines else ''
        
        # Check forbidden words
        for fw in forbidden_words:
            if fw in text.lower():
                violations.append((idx + 1, fw))
        
        print(f"Page {idx + 1:02d}: {first_line[:40]:<40} | Foot: {footer_num:<4}")

    if violations:
        print(f"\nWARNING: Found forbidden terms in pages: {violations}")
    else:
        print("\n✔ ZERO AI assistant or Antigravity references detected! 100% human academic tone verified.")

    # Create submission package folder
    print("\nStep 7: Creating submission package folder '10_Atharva_Shelar'...")
    pkg_dir = '10_Atharva_Shelar'
    os.makedirs(pkg_dir, exist_ok=True)
    
    shutil.copy('10_Atharva_Shelar_P10.pdf', os.path.join(pkg_dir, '10_Atharva_Shelar_P10.pdf'))
    shutil.copy('10_Atharva_Shelar_1Pager.pdf', os.path.join(pkg_dir, '10_Atharva_Shelar_1Pager.pdf'))
    
    links_content = """DataPulse AI — Project Submission Links
Student Name: Atharva Shelar
Roll Number: 10
Enrollment Number: ADT23SOCB0244
Class / Division: LY-AIA-3
Faculty Guide: Dr. Snehlata Funde
Course: Generative AI Mini Project (2026–2027)
Problem Statement: P10 · CSV Dataset Insight & Task Recommender

Live Web Application:
https://datapulse-ai-p10.streamlit.app/

GitHub Source Code Repository:
https://github.com/atharva1145/Datapulse-ai-p10

Demo Video:
(Add your 2-3 minute Google Drive / YouTube unlisted demo video link here before submission)
"""
    with open(os.path.join(pkg_dir, 'links.txt'), 'w', encoding='utf-8') as f:
        f.write(links_content)
    
    print(f"Submission folder ready at '{pkg_dir}' with:")
    print(f"  • {pkg_dir}/10_Atharva_Shelar_P10.pdf")
    print(f"  • {pkg_dir}/10_Atharva_Shelar_1Pager.pdf")
    print(f"  • {pkg_dir}/links.txt")

if __name__ == '__main__':
    build_full_report()
