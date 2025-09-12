import argparse
import pathlib
from agents.kernel import run_agent
from scripts.render_card import render


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--concepts", nargs="+", required=True)
    ap.add_argument("--gate-l4", action="store_true")
    ap.add_argument("--out", default="outputs/cards/card.md")
    args = ap.parse_args()

    result = run_agent(args.concepts, gate_with_l4=args.gate_l4)
    # Persist minimal artifacts (user can extend later)
    pathlib.Path("outputs/cards").mkdir(parents=True, exist_ok=True)
    conv = result["convergence"]
    conv_file = "outputs/cards/_latest_convergence.json"
    pathlib.Path(conv_file).write_text(__import__("json").dumps(conv, indent=2), encoding="utf-8")
    practices = [p.get("name", "practice") for p in result.get("practices", [])]
    render(conv_file, practices, args.out)


