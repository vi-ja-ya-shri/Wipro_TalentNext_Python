# REGRESSION
# 1. Predict Car Price (cars.csv) – Multiple Linear Regression
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
cars = pd.read_csv(r"D:\Wipro_TalentNext_Python\Regression_Classification\CarPrice.csv")

# Preview
print(cars.head())
print(cars.info())
# Drop Car_ID
cars = cars.drop("car_ID", axis=1)

# Extract Car brand
cars["CarBrand"] = cars["CarName"].apply(lambda x: x.split(' ')[0])
cars = cars.drop("CarName", axis=1)

# Encode categorical features
cars = pd.get_dummies(cars, drop_first=True)

# Features & Target
X = cars.drop("Price", axis=1)
y = cars["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluation
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

#Compare actual vs predicted
df_compare = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
print(df_compare.head(10))
plt.figure(figsize=(8,5))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Car Prices")
plt.show()


# 2. Predict Startup Profit (50_startups.csv) – Multiple Linear Regression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
startup = pd.read_csv(r"D:\Wipro_TalentNext_Python\Numpy_and_Pandas\startups.csv")

# Encode categorical 'State' column if present
startup = pd.get_dummies(startup, drop_first=True)

X = startup.drop("Profit", axis=1)
y = startup["Profit"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))


# 3. Predict Salary (Salary_Data.csv) – Simple Linear Regression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

salary = pd.read_csv(r"D:\Wipro_TalentNext_Python\Regression_Classification\salary_data.csv")

X = salary[["YearsExperience"]]
y = salary["Salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))

# Visualization
plt.scatter(X, y, color="blue")
plt.plot(X, model.predict(X), color="red")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# CLASSIFICATION
# 4. Predict Cancer (cancer.csv) – Logistic Regression
# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#  Step 2: Load Dataset
# Load dataset directly from sklearn
data = load_breast_cancer()

# Features (X) and Target (y)
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)   # 0 = malignant, 1 = benign

# Check shape and preview
print("Dataset Shape:", X.shape)
print(X.head())
print("Target values count:\n", y.value_counts())


# Step 3: EDA (Exploratory Data Analysis)
# Target distribution
sns.countplot(x=y)
plt.title("Cancer Diagnosis (0 = Malignant, 1 = Benign)")
plt.show()

# Correlation heatmap (optional, for insight)
plt.figure(figsize=(12,8))
sns.heatmap(X.corr(), cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

#  Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Step 5: Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#  Step 6: Train Model (Logistic Regression)
model = LogisticRegression(max_iter=10000)
model.fit(X_train_scaled, y_train)

#  Step 7: Predictions & Evaluation
y_pred = model.predict(X_test_scaled)

# Evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=data.target_names))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

#  Step 8: Confusion Matrix Visualization
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=data.target_names, yticklabels=data.target_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


# 5. Predict Purchase (Social_Network_Ads.csv) – Logistic Regression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

ads = pd.read_csv(r"D:\Wipro_TalentNext_Python\Regression_Classification\Social_Network_Ads.csv")

X = ads.drop("Purchased", axis=1)
y = ads["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()