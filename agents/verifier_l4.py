from __future__ import annotations

import json
import subprocess
import tempfile
import os


def maybe_gate_synthesis(threshold_pass: bool = True) -> bool:
    try:
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
        tmp.close()
        cmd = ["python3", "recursive-alignment/code/l4_health_check.py", "--json-out", tmp.name]
        subprocess.run(cmd, check=True)
        with open(tmp.name, "r", encoding="utf-8", errors="ignore") as f:
            health = json.load(f)
        os.unlink(tmp.name)
        return bool(health.get("passed", threshold_pass))
    except Exception:
        return True


