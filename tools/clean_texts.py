#!/usr/bin/env python3
import re
import sys
from pathlib import Path


def normalize_whitespace(text: str) -> str:
    # Convert Windows/Mac line endings to Unix
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    # Remove trailing spaces on each line
    text = re.sub(r'[\t ]+$', '', text, flags=re.MULTILINE)
    return text


def remove_page_headers_and_footers(text: str) -> str:
    # Remove repeated page headers like "Aptavani-2525526Aptavani-2" and similar patterns
    text = re.sub(r'\n\s*Aptavani-[0-9\- ]*Aptavani\-[0-9a-zA-Z\-]*\s*\n', '\n', text)
    # Remove isolated page-number-like lines (just numbers or number ranges)
    text = re.sub(r'\n\s*[0-9]{1,4}\s*\n', '\n', text)
    return text


def fix_hyphenation(text: str) -> str:
    # De-hyphenate words split at line breaks: e.g., 'inter-
    # national' -> 'international'. Avoid hyphens that are part of real words by
    # only joining when a line ends with a hyphen and next line starts with lowercase.
    text = re.sub(r'-\n([a-z])', r'\1', text)
    return text


def collapse_wrapped_lines_into_paragraphs(text: str) -> str:
    # Treat blank lines as paragraph separators. Within paragraphs, collapse single newlines to spaces.
    paragraphs = re.split(r'\n\s*\n', text)
    cleaned_paragraphs = []
    for p in paragraphs:
        # Join lines that are not bullet/numbered prefixes
        lines = [ln.strip() for ln in p.split('\n') if ln.strip()]
        if not lines:
            continue
        # If a line ends with double-space or explicit hard-break markers, keep break; else join with space.
        buf = []
        for ln in lines:
            if buf and (buf[-1].endswith('  ') or re.search(r'[.:;?!\)]$', buf[-1])):
                buf.append(ln)
            else:
                if buf:
                    buf[-1] = (buf[-1] + ' ' + ln).strip()
                else:
                    buf.append(ln)
        cleaned_paragraphs.append('\n'.join(buf))
    return ('\n\n').join(cleaned_paragraphs).strip() + '\n'


def remove_duplicate_blocks(text: str) -> str:
    # Some conversions duplicate chunks back-to-back; remove exact duplicate consecutive paragraphs
    paras = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    deduped = []
    prev = None
    for p in paras:
        if p != prev:
            deduped.append(p)
        prev = p
    return ('\n\n').join(deduped) + '\n'


def clean_text(text: str) -> str:
    text = normalize_whitespace(text)
    text = remove_page_headers_and_footers(text)
    text = fix_hyphenation(text)
    text = collapse_wrapped_lines_into_paragraphs(text)
    text = remove_duplicate_blocks(text)
    return text


def process_file(src: Path, dst_dir: Path) -> None:
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / src.name
    raw = src.read_text(encoding='utf-8', errors='ignore')
    cleaned = clean_text(raw)
    dst.write_text(cleaned, encoding='utf-8')


def main(argv):
    if len(argv) < 2:
        print('Usage: clean_texts.py <input_glob_or_dir> [<more paths>...]')
        print('Cleans into resources/aptavani/clean/')
        return 2
    project_root = Path(__file__).resolve().parents[1]
    clean_dir = project_root / 'resources' / 'aptavani' / 'clean'
    for arg in argv[1:]:
        path = (project_root / arg).resolve() if not arg.startswith('/') else Path(arg)
        if path.is_dir():
            for f in path.glob('*.txt'):
                process_file(f, clean_dir)
        else:
            # support globs relative to project root
            for f in Path().glob(str(path)):
                if f.is_file() and f.suffix.lower() == '.txt':
                    process_file(f, clean_dir)
    print(f'Cleaned texts written to: {clean_dir}')


if __name__ == '__main__':
    sys.exit(main(sys.argv))


