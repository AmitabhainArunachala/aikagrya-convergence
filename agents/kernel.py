from __future__ import annotations

from typing import List, Dict, Any

try:
    from .explorer import run_explorer  # existing module
except Exception:
    def run_explorer(concept: str) -> Dict[str, Any]:
        return {"concept": concept, "sources": [], "bullets": [], "created_at": ""}

try:
    from .synthesizer import run_synthesizer  # existing module
except Exception:
    def run_synthesizer(concepts: List[str]) -> Dict[str, Any]:
        return {"concepts": concepts, "convergences": [], "tensions": [], "created_at": ""}

try:
    from .practice_gen import run_practice  # to be added
except Exception:
    def run_practice(claim: str) -> Dict[str, Any]:
        return {"name": f"Practice for: {claim}", "steps": [], "falsifiable_claim": claim, "measure": "", "created_at": ""}

try:
    from .verifier_l4 import maybe_gate_synthesis  # to be added
except Exception:
    def maybe_gate_synthesis() -> bool:
        return True


def run_agent(concepts: List[str], gate_with_l4: bool = True) -> Dict[str, Any]:
    notes = [run_explorer(c) for c in concepts]
    if gate_with_l4 and not maybe_gate_synthesis():
        conv = {"concepts": concepts, "convergences": [], "tensions": [], "created_at": ""}
    else:
        conv = run_synthesizer(concepts)
    practices = [run_practice(c.get("claim", c)) for c in conv.get("convergences", [])[:2]]
    return {"concepts": concepts, "notes": notes, "convergence": conv, "practices": practices}


