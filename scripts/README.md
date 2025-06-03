# Fairness in Human-Centered Knowledge Access

This repository contains code and experiments for the paper:

**"Fairness in Human-Centered Knowledge Access: A Theoretical Framework for Guaranteed Equitable AI Systems"**

We propose a fairness-aware recommendation framework with provable guarantees, designed for educational and digital library environments.

---

## 🚀 Features
- Synthetic dataset generation with group-biased relevance
- Fairness Enforcement Algorithm (FEA) for group exposure parity and envy-freeness
- Utility, disparity, and envy evaluation metrics

---

## 🛠 Installation
```bash
pip install -r requirements.txt
```

---

## 📦 Project Structure
```
fairness-knowledge-access/
├── data/              # Synthetic data
├── notebooks/         # (Optional) Exploration notebooks
├── src/               # Core logic modules
├── results/           # Outputs and visualizations
├── appendix/          # LaTeX appendix for submission
├── scripts/           # Run experiments
├── requirements.txt   # Dependencies
└── README.md          # This file
```

---

## ▶️ Running the Experiment
```bash
python scripts/run_experiment.py
```

Outputs include:
- Total utility
- Exposure disparity
- Envy violations
- `results/exposure_matrix.csv`

---

## 📊 Sample Results
| Method           | Utility | Exposure Disparity | Envy Count |
|------------------|---------|---------------------|-------------|
| Top-k Relevance | 0.87    | High                | 42          |
| FEA ($\delta$=0.1) | 0.83    | 0                   | 0           |

---

## 📖 Citation
```
@inproceedings{your2025fairness,
  title={Fairness in Human-Centered Knowledge Access},
  author={},
  booktitle={},
  year={2025}
}
```

## 📜 License
MIT License
