# SALES PREDICTION
# 1. Load Data in DataFrame
import pandas as pd

df = pd.read_csv(r"D:\Wipro_TalentNext_Python\Regression_Classification\Advertising.csv")

df = df.drop("Unnamed: 0", axis=1)

print(df.head())
print(df.info())
print(df.describe())

