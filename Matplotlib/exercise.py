# 1. EDA on Mall_Customers dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


mall = pd.read_csv(r"D:\Wipro_TalentNext_Python\Matplotlib\Mall_Customers.csv")


print(mall.head())
print(mall.info())
print(mall.describe())


sns.histplot(mall["Age"], kde=True, bins=20)
plt.title("Age Distribution of Customers")
plt.show()


sns.countplot(x="Gender", data=mall)
plt.title("Gender Count")
plt.show()


sns.scatterplot(x="Annual Income (k$)", y="Spending Score (1-100)", hue="Gender", data=mall)
plt.title("Annual Income vs Spending Score")
plt.show()


mall['Gender'] = mall['Gender'].map({'Male': 1, 'Female': 0})


sns.heatmap(mall.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap (with Encoded Gender)")
plt.show()

# 2. EDA on Salary_Data dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
salary = pd.read_csv(r"D:\Wipro_TalentNext_Python\Matplotlib\salary_data.csv")

# Inspect
print(salary.head())
print(salary.info())
print(salary.describe())

# Distribution of YearsExperience
sns.histplot(salary["YearsExperience"], kde=True)
plt.title("Distribution of Years of Experience")
plt.show()

# Scatter plot YearsExperience vs Salary
sns.scatterplot(x="YearsExperience", y="Salary", data=salary)
plt.title("Years of Experience vs Salary")
plt.show()

# Regression line
sns.regplot(x="YearsExperience", y="Salary", data=salary)
plt.title("Regression Plot: Years of Experience vs Salary")
plt.show()

# Correlation heatmap
sns.heatmap(salary.corr(), annot=True, cmap="viridis")
plt.title("Correlation Heatmap")
plt.show()

# 3. EDA on Social_Network_Ads dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
ads = pd.read_csv(r"D:\Wipro_TalentNext_Python\Matplotlib\Social_Network_Ads.csv")

# Inspect
print(ads.head())
print(ads.info())
print(ads.describe())


# Age vs Estimated Salary
sns.scatterplot(x="Age", y="EstimatedSalary", hue="Purchased", data=ads)
plt.title("Age vs Estimated Salary (with Purchase Status)")
plt.show()

# Distribution of Purchased
sns.countplot(x="Purchased", data=ads)
plt.title("Purchase Count (0 = No, 1 = Yes)")
plt.show()

# Correlation heatmap
sns.heatmap(ads.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
