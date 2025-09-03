# SALES PREDICTION
# 1. Load Data in DataFrame
import pandas as pd

df = pd.read_csv(r"D:\Wipro_TalentNext_Python\Regression_Classification\Advertising.csv")

df = df.drop("Unnamed: 0", axis=1)

print(df.head())
print(df.info())
print(df.describe())

# 2. Exploratory Data Analysis (EDA)
import matplotlib.pyplot as plt
import seaborn as sns

sns.pairplot(df)
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()

# 3.Build Model (Multiple Linear Regression)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = df[['TV','Radio','Newspaper']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# 4.Evaluation Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = mse**0.5
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("R² Score:", r2)

