#!/usr/bin/env python3
"""
Convert all PDFs in an input directory to UTF-8 .txt files using pdfminer.six.

Usage:
  python tools/pdf_to_text.py --input resources/aptavani --output resources/aptavani/text
"""

import argparse
import sys
from pathlib import Path

from pdfminer.high_level import extract_text


def convert_pdf_to_text(pdf_path: Path, txt_path: Path) -> None:
    text = extract_text(str(pdf_path))
    txt_path.write_text(text or "", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert PDFs to text")
    parser.add_argument("--input", default="resources/aptavani", help="Input directory containing PDFs")
    parser.add_argument("--output", default="resources/aptavani/text", help="Output directory for .txt files")
    args = parser.parse_args()

    in_dir = Path(args.input).resolve()
    out_dir = Path(args.output).resolve()

    if not in_dir.exists() or not in_dir.is_dir():
        print(f"Input directory not found: {in_dir}", file=sys.stderr)
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)

    pdf_files = sorted([p for p in in_dir.iterdir() if p.suffix.lower() == ".pdf"]) 
    if not pdf_files:
        print(f"No PDF files found in {in_dir}")
        return 0

    successes = 0
    failures = 0

    for pdf_path in pdf_files:
        txt_path = out_dir / (pdf_path.stem + ".txt")
        try:
            print(f"Converting {pdf_path.name} -> {txt_path.name} ...")
            convert_pdf_to_text(pdf_path, txt_path)
            # Basic sanity: ensure file created
            if txt_path.exists() and txt_path.stat().st_size >= 0:
                successes += 1
            else:
                failures += 1
        except Exception as exc:
            failures += 1
            print(f"Failed to convert {pdf_path.name}: {exc}", file=sys.stderr)

    print(f"Done. Converted: {successes}, Failed: {failures}")
    return 0 if failures == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())


