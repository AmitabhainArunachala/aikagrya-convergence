from __future__ import annotations

from typing import Dict, Any
from datetime import datetime


def run_practice(convergence_claim: str) -> Dict[str, Any]:
    return {
        "name": f"Protocol: {convergence_claim[:60]}",
        "steps": [
            "Sit quietly for 3 minutes",
            "Hold the claim in awareness",
            "Notice any shift in clarity or equanimity",
        ],
        "falsifiable_claim": convergence_claim,
        "measure": "Self-reported clarity delta after 3 minutes",
        "created_at": datetime.utcnow().isoformat(),
    }


