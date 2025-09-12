#!/usr/bin/env python3
import subprocess
import sys
import shutil
from pathlib import Path


def command_exists(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def run(cmd: list[str]) -> int:
    return subprocess.call(cmd)


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def ocr_pdf_if_available(src: Path, dst: Path) -> Path:
    # Prefer OCR if ocrmypdf exists; otherwise copy as-is
    ensure_dir(dst.parent)
    if command_exists('ocrmypdf'):
        tmp = dst.with_suffix('.tmp.pdf')
        cmd = [
            'ocrmypdf',
            '--deskew',
            '--rotate-pages',
            '--remove-background',
            '--optimize', '0',
            str(src),
            str(tmp),
        ]
        code = run(cmd)
        if code == 0 and tmp.exists():
            tmp.replace(dst)
            return dst
    # fallback: copy original
    shutil.copy2(src, dst)
    return dst


def extract_markdown_with_pymupdf(src_pdf: Path, out_md: Path) -> bool:
    try:
        import fitz  # PyMuPDF
    except Exception:
        return False
    doc = fitz.open(str(src_pdf))
    chunks: list[str] = []
    for page in doc:
        text = None
        # Try preferred formats in order
        for fmt in ('markdown', 'md', 'xhtml', 'html', 'text'):
            try:
                text = page.get_text(fmt)
                if text:
                    break
            except Exception:
                continue
        if text:
            chunks.append(text)
    if not chunks:
        return False
    ensure_dir(out_md.parent)
    out_md.write_text(''.join(chunks), encoding='utf-8')
    return True


def render_html_with_poppler(src_pdf: Path, out_html: Path) -> bool:
    if not command_exists('pdftohtml'):
        return False
    ensure_dir(out_html.parent)
    # Use single HTML (-s) and complex mode (-c), no frames
    tmp_dir = out_html.parent
    base = out_html.with_suffix('')
    cmd = ['pdftohtml', '-c', '-s', '-noframes', str(src_pdf), str(base)]
    code = run(cmd)
    # pdftohtml writes base.html
    candidate = out_html
    if code == 0:
        # Some versions output base.html directly
        if not candidate.exists():
            alt = base.with_suffix('.html')
            if alt.exists():
                alt.replace(candidate)
        return candidate.exists()
    return False


def html_to_markdown_with_pandoc(src_html: Path, out_md: Path) -> bool:
    if not command_exists('pandoc'):
        return False
    ensure_dir(out_md.parent)
    code = run(['pandoc', str(src_html), '-o', str(out_md)])
    return code == 0 and out_md.exists()


def process_one(pdf_path: Path, searchable_dir: Path, md_dir: Path, html_dir: Path) -> None:
    searchable_pdf = searchable_dir / pdf_path.name
    md_out = md_dir / (pdf_path.stem + '.md')
    html_out = html_dir / (pdf_path.stem + '.html')

    # 1) OCR (optional)
    ocr_pdf_if_available(pdf_path, searchable_pdf)

    # 2) Markdown via PyMuPDF
    md_ok = extract_markdown_with_pymupdf(searchable_pdf, md_out)

    # 3) HTML via Poppler, then optional MD via pandoc as fallback
    html_ok = render_html_with_poppler(searchable_pdf, html_out)
    if not md_ok and html_ok:
        html_to_markdown_with_pandoc(html_out, md_out)


def main(argv: list[str]) -> int:
    project_root = Path(__file__).resolve().parents[1]
    src_dir = project_root / 'resources' / 'aptavani'
    pdfs = sorted(p for p in src_dir.glob('*.pdf'))
    if not pdfs:
        print('No PDFs found in resources/aptavani')
        return 1
    searchable_dir = src_dir / 'searchable'
    md_dir = src_dir / 'md'
    html_dir = src_dir / 'html'

    print(f'Found {len(pdfs)} PDFs')
    for i, pdf in enumerate(pdfs, 1):
        print(f'[{i}/{len(pdfs)}] Processing {pdf.name} ...')
        process_one(pdf, searchable_dir, md_dir, html_dir)
    print('Done.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))


