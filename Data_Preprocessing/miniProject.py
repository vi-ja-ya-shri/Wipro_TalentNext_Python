# 1: Load the data in DataFrame
import pandas as pd

# Load dataset
df = pd.read_csv(r"D:\Wipro_TalentNext_Python\Data_Preprocessing\melb_data.csv")


print(df.head())

print(df.info())
print(df.describe())

# 2: Handle Inappropriate Data


df = df.drop(['Address', 'SellerG', 'Date'], axis=1)

df = df.drop_duplicates()
df = df[df['Price'] < 3000000]

# 3: Handle Missing Data

threshold = len(df) * 0.3
df = df.dropna(thresh=threshold, axis=1)

num_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

cat_cols = df.select_dtypes(include=['object']).columns
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

# 4: Handle Categorical Data
df = pd.get_dummies(df, drop_first=True)

print(df.head())