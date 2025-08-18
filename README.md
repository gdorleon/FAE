# Fairness in Human-Centered Knowledge Access

This repository contains code and experiments for the paper:
**"Achieving Exposure Parity and Envy-Freeness in AI-Driven Knowledge Systems"**

We propose a fairness-aware recommendation framework with provable guarantees, designed for educational and digital library environments.

## About it

- Synthetic dataset generation with group-biased relevance  
- Fairness Enforcement Algorithm (FEA) for group exposure parity and envy-freeness  
- Utility, disparity, and envy evaluation metrics

## Data

The project uses both synthetic and real-world data:

- **Real Dataset**: [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) from Kaggle. It includes user, book, and rating information. Credit for the dataset goes to its original creator.

## Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

## Repo Structure
```
fairness-knowledge-access/
├── data/              # Synthetic and real-world data
├── src/               # Core logic modules
├── results/           # Outputs and visualizations
├── scripts/           # Run experiments
├── requirements.txt   # Dependencies
└── README.md          # This file
```
## Running the Experiment
```bash
python scripts/run_experiment.py
```
## Citation
```
@inproceedings{...,
  title={Fairness in Human-Centered Knowledge Access},
  author={},
  booktitle={},
  year={2025}
}
```


