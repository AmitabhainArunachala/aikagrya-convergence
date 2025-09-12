#!/usr/bin/env python3
import json
import os
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen
import ssl
import certifi


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "resources" / "collage_sources" / "sources.json"
OUTDIR = ROOT / "resources" / "collage_sources" / "downloaded"


def fetch_url(url: str) -> str:
    req = Request(url, headers={"User-Agent": "aikagrya-collage-fetch/1.0"})
    context = ssl.create_default_context(cafile=certifi.where())
    with urlopen(req, timeout=30, context=context) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def sanitize_filename(url: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9_.-]", "_", url)
    return name[:200]


def main() -> int:
    data = json.loads(SOURCES.read_text(encoding="utf-8"))
    OUTDIR.mkdir(parents=True, exist_ok=True)

    def save(category: str, label: str, url: str):
        try:
            content = fetch_url(url)
        except Exception as e:
            subdir = OUTDIR / category / label
            subdir.mkdir(parents=True, exist_ok=True)
            (subdir / (sanitize_filename(url) + ".error.txt")).write_text(str(e), encoding="utf-8")
            print("WARN:", url, "->", e)
            return
        subdir = OUTDIR / category / label
        subdir.mkdir(parents=True, exist_ok=True)
        fname = sanitize_filename(url) + (".md" if url.endswith(".md") else ".txt")
        (subdir / fname).write_text(content, encoding="utf-8")

    for url in data.get("n8n", {}).get("github", []):
        save("n8n", "github", url)

    for url in data.get("langgraph", {}).get("github", []):
        save("langgraph", "github", url)
    for url in data.get("langgraph", {}).get("docs", []):
        save("langgraph", "docs", url)

    for vendor, urls in data.get("vendors", {}).items():
        for url in urls:
            save("vendors", vendor, url)

    print("Fetched sources into", OUTDIR)
    return 0


if __name__ == "__main__":
    sys.exit(main())


