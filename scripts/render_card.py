import json
import sys
import pathlib
import datetime as dt

TEMPLATE = """# {title}

**Concepts:** {concepts}
**Created:** {created}

## Convergences
{conv_lines}

## Tensions
{ten_lines}

## Practices
{prac_lines}

---

*Evidence citations preserved in data files.*
"""


def render(convergence_json: str, practices: list[str], out_path: str) -> None:
    with open(convergence_json, "r", encoding="utf-8", errors="ignore") as f:
        conv = json.load(f)
    conv_lines = "\n".join(
        [f"- **{c['claim']}** (confidence {float(c.get('confidence', 0.7)):.2f})" for c in conv.get("convergences", [])]
    )
    ten_lines = "\n".join([f"- {t['issue']}" for t in conv.get("tensions", [])])
    prac_lines = "\n".join([f"- {p}" for p in practices])
    md = TEMPLATE.format(
        title="Convergence Card",
        concepts=", ".join(conv.get("concepts", [])),
        created=dt.datetime.utcnow().isoformat(),
        conv_lines=conv_lines or "- None yet.",
        ten_lines=ten_lines or "- None recorded.",
        prac_lines=prac_lines or "- TBD.",
    )
    pathlib.Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(out_path).write_text(md, encoding="utf-8")
    print("wrote:", out_path)


if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2:-1], sys.argv[-1])


