# 1.Data Preprocessing on melb_data.csv
import pandas as pd
import numpy as np


data = pd.read_csv(r"D:\Wipro_TalentNext_Python\Data_Preprocessing\melb_data.csv")


print("First 5 rows:\n", data.head())


print("\nShape of dataset:", data.shape)
print("\nColumn Information:")
print(data.info())


print("\nMissing Values:\n", data.isnull().sum())


data = data.dropna(axis=1, thresh=0.7*len(data)) 
data = data.fillna(data.median(numeric_only=True))
data = data.fillna(data.mode().iloc[0])     

print("\nDuplicate rows:", data.duplicated().sum())
data = data.drop_duplicates()

print("\nStatistical Summary:\n", data.describe())

data_encoded = pd.get_dummies(data, drop_first=True)

print("\nCorrelation with target variable 'Price':\n", data_encoded.corr()['Price'].sort_values(ascending=False))

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
numeric_cols = data_encoded.select_dtypes(include=[np.number]).columns
data_encoded[numeric_cols] = scaler.fit_transform(data_encoded[numeric_cols])

print("\nPreprocessed Data (first 5 rows):\n", data_encoded.head())

# 2.Data Preprocessing on melb_data.csv

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


data = pd.read_csv(r"D:\Wipro_TalentNext_Python\Data_Preprocessing\melb_data.csv")


print("Shape of dataset:", data.shape)
print("\nFirst 5 rows:\n", data.head())
print("\nDataset Info:\n")
print(data.info())


print("\nMissing Values per Column:\n", data.isnull().sum())


data = data.dropna(axis=1, thresh=0.7*len(data))

data = data.fillna(data.median(numeric_only=True))


data = data.fillna(data.mode().iloc[0])


print("\nNumber of duplicate rows:", data.duplicated().sum())
data = data.drop_duplicates()


print("\nStatistical Summary:\n", data.describe(include='all'))


data_encoded = pd.get_dummies(data, drop_first=True)


print("\nCorrelation with Target (Price):\n", data_encoded.corr()['Price'].sort_values(ascending=False))


scaler = StandardScaler()
numeric_cols = data_encoded.select_dtypes(include=[np.number]).columns
data_encoded[numeric_cols] = scaler.fit_transform(data_encoded[numeric_cols])

print("\nFinal Preprocessed Data (first 5 rows):\n", data_encoded.head())