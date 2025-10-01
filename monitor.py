"""
Minimal monitoring: print + append to metrics.json

"""

import json, time
from pathlib import Path


def log_metrics(metrics: dict, path: str = "metrics.json") -> None:
    payload = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "metrics": metrics,
    }
    print("[MONITOR]", json.dumps(payload, indent=2))
    p = Path(path)
    existing = []
    if p.exists():
        try:
            existing = json.loads(p.read_text())
        except Exception:
            existing = []
    existing.append(payload)
    p.write_text(json.dumps(existing, indent=2))

    if __name__ == "__main__":
        log_metrics({"accuracy": 0.93})
