# evaluation_utils.py

import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score,
    roc_curve,
    precision_recall_curve,
    average_precision_score
)

def evaluate_classification_model(model, X_test, y_test, model_name="Model", output_dir="../reports/figures/"):
    """
    Generates, displays, and saves a comprehensive evaluation for a classification model.

    Args:
        model: The trained classification model object.
        X_test: Test features.
        y_test: True test labels.
        model_name (str): The name of the model for plot titles and filenames.
        output_dir (str): The directory to save the output plots.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Get class predictions and probability scores
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]

    # 1. Print Accuracy and Classification Report
    print(f"--- {model_name} Evaluation ---")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    auc_roc = roc_auc_score(y_test, y_pred_proba)
    print(f"AUC-ROC Score: {auc_roc:.4f}")
    print("-" * 30)

    # --- Generate and Save Plots ---
    
    # 2. Confusion Matrix
    plt.figure(figsize=(8, 6))
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'{model_name} - Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.savefig(os.path.join(output_dir, f'{model_name}_confusion_matrix.png'), bbox_inches='tight')
    plt.show()

    # 3. ROC Curve and AUC Score
    plt.figure(figsize=(8, 6))
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    plt.plot(fpr, tpr, label=f'AUC = {auc_roc:.4f}')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.title(f'{model_name} - ROC Curve')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend()
    plt.savefig(os.path.join(output_dir, f'{model_name}_roc_curve.png'), bbox_inches='tight')
    plt.show()

    # 4. Precision-Recall (PR) Curve
    plt.figure(figsize=(8, 6))
    precision, recall, _ = precision_recall_curve(y_test, y_pred_proba)
    ap_score = average_precision_score(y_test, y_pred_proba)
    plt.plot(recall, precision, label=f'AP = {ap_score:.4f}')
    plt.title(f'{model_name} - Precision-Recall Curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.legend()
    plt.savefig(os.path.join(output_dir, f'{model_name}_pr_curve.png'), bbox_inches='tight')
    plt.show()