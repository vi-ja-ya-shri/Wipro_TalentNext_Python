import pandas as pd

# Load the dataset
df = pd.read_csv(r"D:\Wipro_TalentNext_Python\Matplotlib\diabetes.csv")

# Show first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Shape
print("\nShape of dataset:", df.shape)

# Statistical summary
print("\nSummary Statistics:")
print(df.describe())

# Data Preprocessing
import numpy as np

cols_with_zero = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
df[cols_with_zero] = df[cols_with_zero].replace(0, np.nan)

# Check missing values count
print(df.isnull().sum())


# Uni-variate Analysis

import matplotlib.pyplot as plt
import seaborn as sns


df.hist(bins=20, figsize=(12,10))
plt.show()


sns.countplot(x='Outcome', data=df)
plt.show()

# Bi-variate Analysis

plt.figure(figsize=(12,8))
for i, col in enumerate(df.columns[:-1], 1):
    plt.subplot(3,3,i)
    sns.boxplot(x='Outcome', y=col, data=df)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
