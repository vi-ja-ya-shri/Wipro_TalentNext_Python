# Numpy
# 1.Create a two-dimensional 3×3 array and perform ndim, shape, and slicing.

# import numpy as np


# arr2D = np.array([[1, 2, 3],
#                   [4, 5, 6],
#                   [7, 8, 9]])

# print("Array:\n", arr2D)


# print("ndim:", arr2D.ndim)


# print("shape:", arr2D.shape)


# print("Slicing [0:2, 0:2]:\n", arr2D[0:2, 0:2])


# print("Second column:", arr2D[:, 1])




# # 2.Create a one-dimensional array and perform ndim, shape, and reshape.


# arr1D = np.array([1, 2, 3, 4, 5, 6])

# print("Array:", arr1D)


# print("ndim:", arr1D.ndim)


# print("shape:", arr1D.shape)


# reshaped = arr1D.reshape(2, 3)
# print("Reshaped array:\n", reshaped)


# Pandas
#3. Pandas – DataFrame (cars dataset)
import pandas as pd


cars = pd.read_csv(r"D:\Wipro_TalentNext_Python\Numpy_and_Pandas\cars.csv")


print("First 10 rows:\n", cars.head(10))


print("\nShape of DataFrame:", cars.shape)


print("\nCars DataFrame:\n", cars.head())


print("\nLast 5 rows:\n", cars.tail())


print("\nMeta Information:")

# 4. Pandas – 50_startups dataset
import pandas as pd

# Load dataset
startups = pd.read_csv(r"D:\Wipro_TalentNext_Python\Numpy_and_Pandas\startups.csv")

# a. Display first 5 rows
print("First 5 rows:\n", startups.head())

# b. Statistical summary
print("\nStatistical Summary:\n", startups.describe())

# c. Correlation between variables
print("\nCorrelation Matrix:\n", startups.corr(numeric_only=True))
