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
| [@jgullinkala](https://github.com/jgullinkala)     | Jeevan Gullinkala           | jgullinkala@sandiego.edu     |
| [@lrapolu](https://github.com/lrapolu)             | Laxmi Sulakshana Rapolu     | lrapolu@sandiego.edu         |
| [@suvoganguli](https://github.com/suvoganguli)     | Subhabrata Ganguli         | subhabrata.ganguli@gmail.com |

## Models Used
- XGBoost
- CNN with LSTM
- Transformer based models (PatchTST and TimesFM)

## Technologies Used

### Machine Learning & Deep Learning
- **XGBoost** – Gradient boosting for tabular data
- **Keras & TensorFlow** – CNN-LSTM architecture and hyperparameter tuning
- **PyTorch** – Transformer-based models (PatchTST, TimesFM)
- **Optuna** – Automated hyperparameter optimization
- **Imbalanced-learn** – SMOTE and sampling strategies for class imbalance

### Data Processing & Feature Engineering
- **Pandas, NumPy** – Data manipulation and aggregation
- **Scikit-learn** – Preprocessing, scaling, and model evaluation
- **SHAP** – Model interpretability and feature attribution
- **SimpleImputer, KNNImputer** – Handling missing values

### Infrastructure & Workflow
- **Google Colab** – Model training and experimentation
- **GitHub** – Version control and collaboration
- **Google Drive** – Dataset and model storage
- **Asana** – Project management and task tracking

## Evaluation Metrics
- AUROC, Precision, Recall, F1 Score
- SHAP used for interpretability
- Comparative analysis across model architectures
  
## Repository Structure
- `data/`
  - `raw/` – Unprocessed input data
  - `processed/` – Cleaned datasets ready for modeling - CNN-LSTM Datasets (https://drive.google.com/drive/folders/1TQ5Q2ZG7uO1daxshLLaQtI3X8TatiQaP?usp=sharing)
  - `features/` – Feature matrices and engineered data
- `notebooks/` – Jupyter notebooks for EDA, modeling, and evaluation
- `models/` – Saved models and artifacts
- `reports/` – Generated plots, metrics, and summary outputs
- `src/`
  - `utils/` – Helper functions and reusable modules
- `README.md` – Project documentation

## Saved Model Links
- TimesFM Tuned model - https://drive.google.com/file/d/1JXsTK57N6DIJGnWK5LmJ_cAKdrj-g25B/view?usp=sharing
- TimesFM Trained model - https://drive.google.com/file/d/1k10KekqlC3auNg4gKNwPbLaICgBuHAF3/view?usp=sharing

## Project Management

We are using **Asana** to manage our Capstone tasks and progress:
- [🔗 Capstone Project Board on Asana](https://app.asana.com/1/952672460738672/project/1210723072035418/board/1210723120232317)

## 📝 Notes

- This project uses a cleaned version of the PhysioNet 2012 dataset available on [Kaggle](https://www.kaggle.com/datasets/jamesmcguigan/icustay-mortality-prediction).
- CNN-LSTM models require reshaped time-series input with consistent sequence lengths; padding and masking strategies are applied.
- Transformer models (PatchTST, TimesFM) are sensitive to window size and feature scaling—see `notebooks/06b_Transformer_*` for tuning details.
- SHAP values are computed post-hoc for interpretability; results may vary across model types and feature encodings.
- Class imbalance is addressed using SMOTE and threshold tuning—refer to `notebooks/04c_XGBoost_Design.ipynb` for implementation.
- Evaluation metrics prioritize **recall** to support early identification of high-risk patients.
- For reproducibility, all models are trained and validated using stratified splits and consistent random seeds.

## Project Versions & Releases

This repository uses **Git tags and GitHub Releases** to track major project milestones.

- **Tags** mark important points in the project timeline (e.g., `v0.1`, `v1.0`)
- **Releases** are published snapshots based on tags and may include notebooks, reports, or model artifacts

## License
This project is licensed under the MIT License.
