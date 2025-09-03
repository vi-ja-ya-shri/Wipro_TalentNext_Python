# OUTLIER DETECTION
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv(r"D:\Wipro_TalentNext_Python\Numpy_and_Pandas\datasetExample.csv") 

# Show first rows
print(df.head())
print("\nColumns:", df.columns.tolist())

# Select only numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns
print("\nNumeric Columns:", numeric_cols)

# --- Detect Outliers using IQR ---
outliers = {}
for col in numeric_cols:
    Q1 = np.percentile(df[col].dropna(), 25)  
    Q3 = np.percentile(df[col].dropna(), 75) 
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    mask = (df[col] < lower_bound) | (df[col] > upper_bound)
    outliers[col] = df.loc[mask, col]


for col, values in outliers.items():
    if not values.empty:
        print(f"\n Outliers in {col}:")
        print(values.to_list())
