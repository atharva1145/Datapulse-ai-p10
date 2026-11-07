"""
CSS Stylesheet module for DataPulse AI Mini Project Report.
Matches the academic typography and layout of MIT ADT University reference documents.
"""

REPORT_CSS = """
@page {
    size: A4 portrait;
    margin: 0;
}
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1f2433;
    background: #ffffff;
    font-size: 9.3pt;
    line-height: 1.5;
}
.page {
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    min-height: 297mm;
    padding: 16mm 20mm 15mm 20mm;
    position: relative;
    overflow: hidden;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    background: #ffffff;
}
.page-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 8.4pt;
    padding-bottom: 6px;
    border-bottom: 1px solid #edf0f5;
    margin-bottom: 14px;
    flex-shrink: 0;
}
.header-left {
    color: #7c6bc4;
    font-weight: 600;
}
.header-right {
    color: #5b6172;
    font-weight: 500;
}
.page-footer {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 8.5pt;
    color: #8a8fa0;
    padding-top: 6px;
    border-top: 1px solid #edf0f5;
    margin-top: auto;
    flex-shrink: 0;
}
.page-body {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}
h1 {
    color: #2d2a4a;
    font-size: 18pt;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 10px;
    letter-spacing: -0.01em;
}
h2 {
    color: #2d2a4a;
    font-size: 12.8pt;
    font-weight: 700;
    margin-top: 8px;
    margin-bottom: 5px;
    line-height: 1.25;
}
h3 {
    color: #3b3270;
    font-size: 10.2pt;
    font-weight: 700;
    margin-top: 7px;
    margin-bottom: 3px;
}
p {
    font-size: 9.2pt;
    line-height: 1.5;
    color: #1f2433;
    margin-bottom: 7px;
    text-align: justify;
}
ul, ol {
    margin-left: 18px;
    margin-bottom: 8px;
    font-size: 9.1pt;
    line-height: 1.45;
}
li {
    margin-bottom: 3px;
}
.pill-badge {
    display: inline-block;
    background: #f3e8ff;
    color: #4a3d8f;
    font-size: 8.5pt;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 9999px;
    border: 1px solid #e9d5ff;
}
.unit-badge {
    display: inline-block;
    background: #e0e7ff;
    color: #3730a3;
    font-size: 7.8pt;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 4px;
    margin-right: 6px;
}
.alert-box {
    background: #fbfbfe;
    border-left: 3.5px solid #4a3d8f;
    border-radius: 3px 6px 6px 3px;
    padding: 7px 11px;
    margin: 8px 0;
    border-top: 1px solid #e8eaf2;
    border-right: 1px solid #e8eaf2;
    border-bottom: 1px solid #e8eaf2;
    flex-shrink: 0;
}
.alert-title {
    font-size: 7.8pt;
    font-weight: 800;
    color: #4a3d8f;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 3px;
}
.alert-content {
    font-size: 8.6pt;
    line-height: 1.42;
    color: #2d2a4a;
}
table {
    width: 100%;
    border-collapse: collapse;
    font-size: 8.5pt;
    margin: 8px 0;
}
th {
    background: #2d2a4a;
    color: #ffffff;
    font-weight: 600;
    text-align: left;
    padding: 5px 8px;
    font-size: 8.2pt;
    letter-spacing: 0.02em;
}
td {
    padding: 4.5px 8px;
    border-bottom: 1px solid #eef1f6;
    color: #1f2433;
    vertical-align: top;
    line-height: 1.35;
}
tr:nth-child(even) {
    background: #fbfbfe;
}
.figure-wrapper {
    margin: 7px 0;
    text-align: center;
    flex-shrink: 0;
}
.figure-caption {
    font-size: 8.2pt;
    color: #5b6172;
    margin-top: 4px;
    text-align: left;
    line-height: 1.35;
}
.figure-caption strong {
    color: #2d2a4a;
}
.code-block {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 7px 10px;
    font-family: 'SFMono-Regular', Consolas, Menlo, monospace;
    font-size: 8pt;
    line-height: 1.38;
    color: #0f172a;
    margin: 6px 0;
    white-space: pre-wrap;
    word-break: break-all;
}
.card {
    background: #fbfbfe;
    border: 1px solid #e6e8f0;
    border-radius: 7px;
    padding: 8px 12px;
    margin: 6px 0;
}
.grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
}
.grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
}
"""
