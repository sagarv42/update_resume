import markdown
import subprocess
import tempfile
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_MD = os.path.join(SCRIPT_DIR, "Sagar_Vishwakarma_resume.md")
OUTPUT_PDF = os.path.join(SCRIPT_DIR, "Sagar_Vishwakarma_resume_new.pdf")
BRAVE = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

with open(INPUT_MD, "r") as f:
    md_content = f.read()

# Links are now real URLs in the md file, no replacements needed

html_body = markdown.markdown(md_content, extensions=["tables", "extra"])

# Add class to Education and Notable sections for indented sub-lines
import re

def post_process_html(html):
    # Wrap Education/Notable sections for indentation
    for section in ["EDUCATION", "NOTABLE"]:
        pattern = rf'(<h2>{section}</h2>)(.*?)(?=<h2>|$)'
        replacement = rf'\1<div class="indented-section">\2</div>'
        html = re.sub(pattern, replacement, html, flags=re.DOTALL)

    # 1) Job headers: merge h3 + following <p><strong>date</strong></p> into one line
    #    <h3>Title</h3>\n<p><strong>Jan 2025 -- Present</strong></p>
    #    → <h3>Title <span class="date">Jan 2025 -- Present</span></h3>
    html = re.sub(
        r'(<h3>)(.*?)(</h3>)\s*<p><strong>(.*?)</strong></p>',
        r'\1\2<span class="date">\4</span>\3',
        html
    )

    # 2) Project headers: float tech stack right
    #    <p><strong>Name</strong> <em>(tech)</em></p>
    #    → <p class="project-header"><strong>Name</strong><span class="tech"><em>(tech)</em></span></p>
    html = re.sub(
        r'<p><strong>(.*?)</strong>\s*<em>(\(.*?\))</em></p>',
        r'<p class="project-header"><strong>\1</strong><span class="tech"><em>\2</em></span></p>',
        html
    )

    # 3) Education/Notable: float date right (pattern: — **date**)
    #    Within .indented-section, find <strong>title</strong> ... — <strong>date</strong>
    html = re.sub(
        r'(<p><strong>.*?</strong>.*?)\s*(?:—|--)\s*<strong>(.*?)</strong>',
        r'\1<span class="date"><strong>\2</strong></span>',
        html
    )

    return html

html_body = post_process_html(html_body)

css = """
@page {
    margin: 0.4in 0.5in 0.4in 0.5in;
}
body {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.35;
    color: #1a1a1a;
    margin: 0;
    padding: 0;
}
h1 {
    font-size: 22pt;
    font-weight: bold;
    color: #1565C0;
    margin-bottom: 2pt;
    margin-top: 0;
}
h2 {
    font-size: 12pt;
    font-weight: bold;
    color: #1565C0;
    border-bottom: 2px solid #1565C0;
    padding-bottom: 2pt;
    margin-top: 12pt;
    margin-bottom: 4pt;
    text-transform: uppercase;
    page-break-after: avoid;
    break-after: avoid;
}
h3 {
    font-size: 10.5pt;
    font-weight: bold;
    color: #1a1a1a;
    margin-top: 8pt;
    margin-bottom: 1pt;
    page-break-after: avoid;
    break-after: avoid;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}
h3 .date {
    font-weight: normal;
    font-style: italic;
    font-size: 10pt;
    color: #1a1a1a;
    white-space: nowrap;
    margin-left: 8pt;
}
.project-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}
.project-header .tech {
    white-space: nowrap;
    margin-left: 8pt;
}
.date {
    float: right;
    font-style: italic;
    font-weight: normal;
}
p {
    margin-top: 1pt;
    margin-bottom: 3pt;
    orphans: 3;
    widows: 3;
}
strong {
    font-weight: bold;
}
em {
    font-style: italic;
    color: #555;
}
ul {
    margin-top: 1pt;
    margin-bottom: 3pt;
    padding-left: 16pt;
    page-break-before: avoid;
    break-before: avoid;
}
li {
    margin-bottom: 2pt;
    page-break-inside: avoid;
    break-inside: avoid;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 4pt;
    margin-bottom: 4pt;
    font-size: 9.5pt;
}
th { display: none; }
thead { display: none; }
td {
    padding: 2pt 6pt;
    vertical-align: top;
    border: none;
}
td:first-child {
    font-weight: bold;
    white-space: nowrap;
    width: 80pt;
}
hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 6pt 0;
}
a {
    color: #1565C0;
    text-decoration: none;
}
.indented-section p {
    padding-left: 14pt;
    text-indent: -14pt;
}
"""

html_full = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{css}</style>
</head>
<body>
{html_body}
</body>
</html>"""

# Write temp HTML file
tmp_html = tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w")
tmp_html.write(html_full)
tmp_html.close()

# Use Brave headless to print PDF
cmd = [
    BRAVE,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={OUTPUT_PDF}",
    f"file://{tmp_html.name}",
]

result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
os.unlink(tmp_html.name)

if result.returncode == 0 or os.path.exists(OUTPUT_PDF):
    print(f"PDF generated: {OUTPUT_PDF}")
else:
    print(f"Error: {result.stderr}")
