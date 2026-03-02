"""
Lesson 6: Introduction to Data Science with Python
---------------------------------------------------
This script covers:
1. NumPy Basics
2. Pandas DataFrame Basics
3. Handling Missing Values
4. Exploratory Data Analysis (EDA)
5. Data Visualization with Matplotlib & Seaborn

To run this script, you need to have the following libraries installed:
pip install numpy pandas matplotlib seaborn

Synchronization note:
- This file is aligned with `Lesson06/Exercises/exercises.py`.

"""

# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------
# 1. NumPy Basics
# -------------------------------------

print("\n========== NumPy Basics ==========")

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print("\nNumPy Array:\n", arr)

# Array operations
arr_squared = arr ** 2
print("\nSquared Array:\n", arr_squared)

# Creating a 2D array and reshaping
matrix = np.arange(1, 10).reshape(3, 3)
print("\n2D Matrix:\n", matrix)

# Calculating mean and sum
print("\nMean of the Matrix:", np.mean(matrix))
print("Sum of the Matrix:", np.sum(matrix))

# -------------------------------------
# 2. Pandas DataFrame Basics
# -------------------------------------

print("\n========== Pandas DataFrame Basics ==========")

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Basic DataFrame Operations
print("\nBasic Info:\n", df.info())
print("\nDescriptive Statistics:\n", df.describe())

# Selecting Columns
print("\nSelect 'Name' Column:\n", df['Name'].to_string(index=False))

# Filtering Data
filtered_df = df[df['Salary'] > 60000]
print("\nFiltered Data (Salary > 60,000):\n", filtered_df)

# -------------------------------------
# 3. Handling Missing Values
# -------------------------------------

print("\n========== Handling Missing Values ==========")

# Creating a DataFrame with Missing Values
data_with_missing = {
    'Name': ['Alice', 'Bob', 'Charlie', None],
    'Age': [25, np.nan, 35, 40],
    'Salary': [50000, 60000, None, 80000]
}

df_missing = pd.DataFrame(data_with_missing)
print("\nOriginal Data with Missing Values:\n", df_missing)

# Handling Missing Values
df_filled = df_missing.fillna({'Age': df_missing['Age'].mean(), 'Salary': df_missing['Salary'].median()})
print("\nData After Filling Missing Values:\n", df_filled)

df_dropped = df_missing.dropna()
print("\nData After Dropping Missing Values:\n", df_dropped)

# -------------------------------------
# 4. Exploratory Data Analysis (EDA)
# -------------------------------------

print("\n========== Exploratory Data Analysis (EDA) ==========")

# Loading a sample dataset
df_titanic = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

# Displaying dataset info
print("\nDataset Info:")
df_titanic.info()

# Checking for missing values
print("\nMissing Values:\n", df_titanic.isnull().sum())

# Descriptive statistics
print("\nSummary Statistics:\n", df_titanic.describe())

# Value counts for categorical data
print("\nSurvival Count:\n", df_titanic['survived'].value_counts())

# Grouping data by a column
avg_age_by_survival = df_titanic.groupby('survived')['age'].mean()

# Counting passengers in each class
class_counts = df_titanic['class'].value_counts()

# -------------------------------------
# 5. Data Visualization with Matplotlib & Seaborn
# -------------------------------------

print("\n========== Data Visualization ==========")

# Setting style for seaborn
sns.set_style("whitegrid")

# Bar plot for survival count
plt.figure(figsize=(6,4))
sns.countplot(x='survived', data=df_titanic, palette='Set2')
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()

# Histogram of age distribution
plt.figure(figsize=(6,4))
sns.histplot(df_titanic['age'].dropna(), bins=20, kde=True, color='blue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Box plot of fares paid by different passenger classes
plt.figure(figsize=(6,4))
sns.boxplot(x='class', y='fare', data=df_titanic.dropna(subset=['fare']), palette="coolwarm")
plt.title("Fare Distribution by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Fare Paid")
plt.show()

# Heatmap for correlation
plt.figure(figsize=(8,6))
sns.heatmap(df_titanic.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()
