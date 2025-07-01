# AAI 590 Capstone Project: Rapid ICU Mortality Prediction

This repository contains code and documentation for the AAI 590 Capstone Project: **Rapid ICU Mortality Prediction** — developed as part of the Master of Science in Applied Artificial Intelligence (MS in AI) program at the **University of San Diego (USD)**.

---

## Project Overview

The goal is to develop a machine learning model that can predict in-hospital mortality for ICU patients using aggregrate and time-series physiological data. The dataset is derived from the PhysioNet 2012 Challenge and available on Kaggle in a cleaned format.

- Dataset: [Predict Mortality of ICU Patients (Kaggle)](https://www.kaggle.com/datasets/msafi04/predict-mortality-of-icu-patients-physionet/data)
- Records: 4,000 ICU stays

## Team Members

| GitHub Handle | Name                     | Email                          |
|---------------|--------------------------|--------------------------------|
| [@suvoganguli](https://github.com/suvoganguli)     | Subhabrata Ganguli         | subhabrata.ganguli@gmail.com |
| [@jgullinkala](https://github.com/jgullinkala)     | Jeevan Gullinkala           | jgullinkala@sandiego.edu     |
| [@lrapolu](https://github.com/lrapolu)             | Laxmi Sulakshana Rapolu     | lrapolu@sandiego.edu         |


## Repository Structure

- `data/`
  - `raw/` – Unprocessed input data
  - `processed/` – Cleaned datasets ready for modeling
  - `features/` – Feature matrices and engineered data
- `notebooks/` – Jupyter notebooks for EDA, modeling, and evaluation
- `models/` – Saved models and artifacts
- `reports/` – Generated plots, metrics, and summary outputs
- `src/`
  - `utils/` – Helper functions and reusable modules
- `README.md` – Project documentation

## Notes


## Project Versions & Releases

This repository uses **Git tags and GitHub Releases** to track major project milestones.

- **Tags** mark important points in the project timeline (e.g., `v0.1`, `v1.0`)
- **Releases** are published snapshots based on tags and may include notebooks, reports, or model artifacts

