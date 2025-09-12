#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTDIR = ROOT / "outputs" / "reports"
OUTMD = OUTDIR / "collage_compendium.md"

SECTIONS = [
    ("Collage Overview (n8n × LangGraph)", ROOT / "protocols" / "n8n_langgraph_readme_collage.md", "text"),
    ("n8n Starter Template (JSON)", ROOT / "templates" / "n8n" / "gmail_summary.json", "json"),
    ("LangGraph Starter Template (Python)", ROOT / "templates" / "langgraph" / "gmail_summary.py", "python"),
    ("Sources Manifest", ROOT / "resources" / "collage_sources" / "sources.json", "json"),
]


def fence(lang: str, content: str) -> str:
    return f"```{lang}\n{content}\n```\n"


def main() -> int:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    parts = ["# Agentic Workflow Collage Compendium\n"]
    for title, path, kind in SECTIONS:
        parts.append(f"\n## {title}\n\n")
        if not path.exists():
            parts.append(f"(missing) {path}\n")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if kind == "text":
            parts.append(text.strip() + "\n")
        else:
            parts.append(fence(kind, text))
    OUTMD.write_text("\n".join(parts), encoding="utf-8")
    print("Wrote", OUTMD)
    return 0


if __name__ == "__main__":
    sys.exit(main())


