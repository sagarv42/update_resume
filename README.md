# Resume Generator

A simple tool to maintain a resume in Markdown and generate a styled PDF using a headless browser.

## Files

- `Sagar_Vishwakarma_resume.md` - Resume source file in Markdown
- `Sagar_Vishwakarma_resume.pdf` - Original resume PDF
- `Sagar_Vishwakarma_resume_new.pdf` - Generated PDF from Markdown
- `generate_pdf.py` - Script to convert Markdown to styled PDF

## Requirements

- Python 3.8+
- [Brave Browser](https://brave.com/) installed at default macOS path
- Python dependencies (see below)

## Setup

```bash
pip install -r requirements.txt
```

## Usage

1. Edit `Sagar_Vishwakarma_resume.md` with your updates
2. Run the PDF generator:

```bash
python generate_pdf.py
```

3. Output: `Sagar_Vishwakarma_resume_new.pdf`

## How It Works

1. Reads the Markdown resume file
2. Converts to HTML using the `markdown` library
3. Applies custom CSS for professional resume styling (blue headers, right-aligned dates, indented sections)
4. Post-processes HTML to right-align dates and tech stacks
5. Uses Brave Browser in headless mode to render HTML to PDF with proper page-break handling

## Notes

- Brave Browser path is hardcoded for macOS: `/Applications/Brave Browser.app/Contents/MacOS/Brave Browser`
- To use Chrome instead, update the `BRAVE` variable in `generate_pdf.py`
- Page margins and font sizes can be adjusted in the CSS section of `generate_pdf.py`
