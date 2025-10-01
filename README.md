# Mini MLOps Pipeline + Quantum Foundations

A hands on learning project built **entirely by hand** on Ubuntu.  
This repository blends **Python fundamentals**, a **minimal MLOps pipeline**, and **introductory quantum computing** using Qiskit.

The goal: **understand by doing** — every script written manually to strengthen comprehension of how data, models, and metrics flow together.

---

## Project Overview

| Category        | Focus |
|-----------------|--------|
| **Language**    | Python 3 (on Ubuntu) |
| **Concepts**    | Core Python, Data Structures, Functions, OOP |
| **MLOps**       | Dataset loading, splitting, model training, evaluation, metric logging, CI |
| **Quantum**     | Single-qubit gates, Bloch sphere visualization, entanglement, simulation |
| **CI/CD**       | GitHub Actions with linting and testing |
| **Workflow**    | Reference-based learning with AI support (LLMs), rewritten in human-readable code |

---

## Structure

```bash
mini-mlops-quantum/
├── concepts.py              # Day 1 – Python fundamentals
├── data_structures.py       # Day 2 – Lists, dicts, sets, tuples
├── binary_search.py         # Day 2 – Classic algorithm practice
├── pipeline.py              # Day 3 – Data loading & splitting (Iris dataset)
├── train_model.py           # Day 4 – Logistic Regression + metrics
├── monitor.py               # Day 5 – Metric logging to console + JSON
├── main.py                  # Day 6 – Integrated pipeline (E2E)
├── notebooks/
│   ├── hello_quantum.ipynb  # Intro qubit (H gate)
│   ├── bloch_visual.ipynb   # Bloch sphere visualization
│   ├── entanglement.ipynb   # 2-qubit entanglement
│   └── simulate_circuit.ipynb # Simulation & measurement
├── tests/
│   └── test_smoke.py        # Basic smoke test for imports
├── .github/workflows/ci.yml # GitHub Actions (lint + pytest)
├── requirements.txt         # Dependencies
├── reflection.md            # Personal takeaways (fill after Day 7)
└── README.md
