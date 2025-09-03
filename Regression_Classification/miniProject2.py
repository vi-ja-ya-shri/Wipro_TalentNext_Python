# Diabetes Prediction using PIMA Indians Dataset
# ==========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_curve, auc
)

# 1. Load Dataset

df = pd.read_csv(r"D:\Wipro_TalentNext_Python\Regression_Classification\diabetes.csv")   # replace with your path if needed

print("First 5 rows:")
print(df.head())
print("\nDataset info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# 2. Data Preprocessing
zero_as_missing = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[zero_as_missing] = df[zero_as_missing].replace(0, np.nan)

# Impute missing with median
imputer = SimpleImputer(strategy='median')
df[zero_as_missing] = imputer.fit_transform(df[zero_as_missing])

print("\nAfter preprocessing (check missing):")
print(df.isnull().sum())

# 3. Exploratory Data Analysis (EDA)
plt.figure(figsize=(5,4))
df['Outcome'].value_counts().plot(kind='bar', color=['skyblue','salmon'])
plt.title('Class Balance (0=No Diabetes, 1=Diabetes)')
plt.xlabel('Outcome')
plt.ylabel('Count')
plt.show()

# Feature distributions
df.hist(bins=20, figsize=(12,10), color="skyblue", edgecolor="black")
plt.suptitle("Feature Distributions")
plt.show()

# Correlation heatmap
plt.figure(figsize=(10,7))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()

# 4. Train-Test Split

X = df.drop(columns=['Outcome'])
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Build Models
# Logistic Regression
lr_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression(max_iter=1000, solver='liblinear'))
])
lr_pipeline.fit(X_train, y_train)

# KNN with hyperparameter tuning
knn_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', KNeighborsClassifier())
])

param_grid = {'clf__n_neighbors': [3,5,7,9,11]}
grid = GridSearchCV(knn_pipeline, param_grid, cv=5, scoring='f1')
grid.fit(X_train, y_train)

best_knn = grid.best_estimator_
print("\nBest K value for KNN:", grid.best_params_)

# 6. Evaluation Function
def evaluate(model, X_test, y_test, model_name="Model"):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:,1] if hasattr(model,"predict_proba") else None

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

    print(f"\n=== {model_name} ===")
    print(f"Accuracy : {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall   : {rec:.4f}")
    print(f"F1-score : {f1:.4f}")
    print("\nClassification Report:\n", classification_report(y_test, y_pred, digits=4, zero_division=0))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap="Blues",
                xticklabels=["No Diabetes","Diabetes"],
                yticklabels=["No Diabetes","Diabetes"])
    plt.title(f"Confusion Matrix - {model_name}")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    # ROC Curve
    if y_proba is not None:
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        roc_auc = auc(fpr, tpr)
        plt.figure()
        plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
        plt.plot([0,1],[0,1],'--',color='gray')
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title(f"ROC Curve - {model_name}")
        plt.legend()
        plt.show()

# 7. Evaluate Models
evaluate(lr_pipeline, X_test, y_test, model_name="Logistic Regression")
evaluate(best_knn, X_test, y_test, model_name="K-Nearest Neighbors")
