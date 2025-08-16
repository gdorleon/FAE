# Fairness in Human-Centered Knowledge Access

This repository contains code and experiments for the paper:

**"Fairness in Human-Centered Knowledge Access: A Theoretical Framework for Guaranteed Equitable AI Systems"**

We propose a fairness-aware recommendation framework with provable guarantees, designed for educational and digital library environments.

---

## About it
- Synthetic dataset generation with group-biased relevance
- Fairness Enforcement Algorithm (FEA) for group exposure parity and envy-freeness
- Utility, disparity, and envy evaluation metrics

---

## Installation
```bash
pip install -r requirements.txt
```

---

## Project Structure
```
fairness-knowledge-access/
├── data/              # Synthetic data for testing purpose
├── src/               # Core logic modules
├── results/           # Outputs and visualizations
├── scripts/           # Run experiments
├── requirements.txt   # Dependencies
└── README.md          # This file
```

---

## Running the Experiment
```bash
python scripts/run_experiment.py
```

Outputs include:
- Total utility
- Exposure disparity
- Envy violations
- `results/exposure_matrix.csv`


## Citation
```
@inproceedings{...,
  title={Fairness in Human-Centered Knowledge Access},
  author={},
  booktitle={},
  year={2025}
}
```

## License
MIT License
