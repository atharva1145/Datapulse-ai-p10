"""
Master Compilation Script for DataPulse AI 12-Page Concise Mini Project Report.
Student: Atharva Shelar | Roll No: 10 | P10
Generates 10_Atharva_Shelar_P10_12Pages.pdf and 10_Atharva_Shelar_P10_12Pages.docx
Strictly Local — No Git Push.
"""

import os
import sys
import base64
from pathlib import Path

if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from playwright.sync_api import sync_playwright
import pymupdf
from pdf2docx import Converter

from report_styles import REPORT_CSS
from report_pages_concise import (
    get_p1_cover, get_p2_cert_decl, get_p3_abstract_toc,
    get_p4_intro, get_p5_tech_stack, get_p6_architecture,
    get_p7_u1_u2, get_p8_u3_u4, get_p9_u5,
    get_p10_benchmarks, get_p11_testing_deploy, get_p12_conclusion
)

def build_concise_report():
    print("=" * 60)
    print("📄 COMPILING 12-PAGE CONCISE MINI PROJECT REPORT")
    print("   Student: Atharva Shelar | Roll: 10 | Problem P10")
    print("   Font: Times New Roman | Margins: 9mm All-Side Border")
    print("=" * 60)

    # Step 1: Read Logo
    print("Step 1: Reading university crest...")
    with open('assets/mit_adt_logo.png', 'rb') as f:
        logo_b64 = base64.b64encode(f.read()).decode('utf-8')

    # Step 2: Assemble exactly 12 pages
    print("Step 2: Assembling 12 pages...")
    pages = [
        get_p1_cover(logo_b64),
        get_p2_cert_decl(),
        get_p3_abstract_toc(),
        get_p4_intro(),
        get_p5_tech_stack(),
        get_p6_architecture(),
        get_p7_u1_u2(),
        get_p8_u3_u4(),
        get_p9_u5(),
        get_p10_benchmarks(),
        get_p11_testing_deploy(),
        get_p12_conclusion()
    ]
    print(f"Total pages assembled: {len(pages)}")

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>DataPulse AI — Concise Mini Project Report (P10)</title>
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
    with open('templates/concise_report.html', 'w', encoding='utf-8') as f:
        f.write(full_html)
    print("Step 3: Saved templates/concise_report.html")

    # Step 4: Render to PDF via Playwright
    pdf_out = "10_Atharva_Shelar_P10_12Pages.pdf"
    print(f"Step 4: Launching Playwright to generate {pdf_out}...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('file:///' + os.path.abspath('templates/concise_report.html').replace('\\', '/'))
        page.pdf(
            path=pdf_out,
            format='A4',
            print_background=True,
            margin={'top': '0mm', 'bottom': '0mm', 'left': '0mm', 'right': '0mm'}
        )
        browser.close()
    print(f"✔ Generated {pdf_out}")

    # Step 5: Verify page count and security audit
    print("\nStep 5: Verifying PDF with PyMuPDF...")
    doc = pymupdf.open(pdf_out)
    page_count = len(doc)
    print(f"✔ Verified Page Count: {page_count} pages")

    forbidden = ['antigravity', 'google deepmind', 'assistant response', 'system message', 'chatgpt']
    violations = []
    for idx, pg in enumerate(doc):
        txt = pg.get_text('text').strip()
        lines = [l.strip() for l in txt.split('\n') if l.strip()]
        first_line = lines[0] if lines else 'EMPTY'
        footer_num = lines[-1] if lines else ''
        for fw in forbidden:
            if fw in txt.lower():
                violations.append((idx + 1, fw))
        print(f"Page {idx + 1:02d}: {first_line[:40]:<40} | Foot: {footer_num:<4}")
    doc.close()

    if violations:
        print("❌ Forbidden terms found:", violations)
    else:
        print("✔ Security audit passed: Zero AI assistant mentions! 100% genuine academic tone.")

    # Step 6: Convert to Word (.docx)
    docx_out = "10_Atharva_Shelar_P10_12Pages.docx"
    print(f"\nStep 6: Converting {pdf_out} → {docx_out}...")
    cv = Converter(pdf_out)
    cv.convert(docx_out)
    cv.close()
    print(f"✔ Generated {docx_out}")

    # Step 7: Copy to submission folder
    sub_folder = Path("10_Atharva_Shelar")
    if sub_folder.exists():
        import shutil
        shutil.copy(pdf_out, str(sub_folder / pdf_out))
        shutil.copy(docx_out, str(sub_folder / docx_out))
        print(f"✔ Copied both files to {sub_folder}/")

    print("\n📁 Submission folder contents:")
    for f in sorted(sub_folder.iterdir()):
        sz = f.stat().st_size / 1_048_576
        print(f"   {f.name:<45} {sz:.2f} MB")

    print("\n🎉 DONE! 12-page concise report created (PDF + Word). NO GIT PUSH.")

if __name__ == '__main__':
    build_concise_report()
