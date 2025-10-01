"""
End-to-end: data -> train -> evaluate -> monitor
Run: python main.py
"""

from train_model import run_training
from monitor import log_metrics


def main():
    print("[MAIN] Starting E2E run...")
    result = run_training()
    print(f"[MAIN] Accuracy: {result.metrics['accuracy']:.4f}")
    log_metrics(result.metrics)
    print("[MAIN] Done")


if __name__ == "__main__":
    main()
