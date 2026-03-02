"""
Lesson 7 Examples: From Data Analysis to Machine Learning
=========================================================

Synchronization note:
- This file pairs with `Lesson07/Exercises/exercises.py`.
"""

# --- 1. Recap of Python for Data Science ---
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib  # for model saving/loading

# Sample NumPy array and operations
arr = np.array([10, 20, 30, 40])
print("NumPy array:", arr)
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Reshaped (2,2):\n", arr.reshape(2, 2))

# Sample pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Ella'],
    'Age': [25, 30, 35, 40, 28],
    'Salary': [50000, 60000, 75000, 90000, 52000],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR']
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
print("\nData Types:\n", df.dtypes)
print("\nDescriptive Stats:\n", df.describe())

# --- 2. The Data Science Workflow (Illustrated by a Mini Pipeline) ---
# Step 1: Data Overview
print("\nColumn Names:", df.columns)
print("\nFirst two records:\n", df.head(2))
print("\nMissing values per column:\n", df.isnull().sum())

# Step 2: Grouping & Aggregation
print("\nAverage Salary by Department:\n", df.groupby('Department')['Salary'].mean())

# --- 3. Exploratory Data Analysis (EDA) Best Practices ---
sns.histplot(df['Salary'], kde=True)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# Boxplot of Salary by Department
sns.boxplot(x='Department', y='Salary', data=df)
plt.title("Salary Distribution by Department")
plt.show()

# Pairplot to visualize relationship between features
sns.pairplot(df.drop('Name', axis=1))
plt.show()

# --- 4. Transition to Machine Learning ---
# Definitions (represented as comments)
# Supervised: You know the label (e.g., predict salary based on age)
# Unsupervised: No predefined label (e.g., cluster similar customers)

# --- 5. Core ML Concepts ---
# Train/Test split using sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Use Age and Department (encoded) to predict Salary
# Convert categorical variables using one-hot encoding
X = pd.get_dummies(df[['Age', 'Department']], drop_first=True)
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# --- 6. First ML Model: Linear Regression ---
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction and evaluation
y_pred = model.predict(X_test)
print("\nTest Features:\n", X_test)
print("\nPredictions:", y_pred)
print("\nActual:", y_test.values)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R^2 Score:", r2_score(y_test, y_pred))

# Visualize regression line (1D Example)
plt.scatter(df['Age'], df['Salary'], color='blue', label='Actual')
predicted_line = model.predict(X)
plt.plot(df['Age'], predicted_line, color='red', label='Regression Line')
plt.title("Linear Regression: Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.show()

# --- 7. Saving and Loading Models ---
# Save the trained model to a file
joblib.dump(model, 'linear_model_salary.pkl')
print("\nModel saved to 'linear_model_salary.pkl'")

# Later... in the same or different script:
# Load the model from file
loaded_model = joblib.load('linear_model_salary.pkl')
new_predictions = loaded_model.predict(X_test)
print("\nLoaded model predictions:", new_predictions)

# --- 8. End of Class Recap ---
# You’ve:
# - Created NumPy arrays and performed math operations
# - Used pandas for data analysis
# - Created visualizations with seaborn/matplotlib
# - Built a simple Linear Regression model with scikit-learn
# - Saved and reused a trained ML model
# Next class: classification problems (e.g., predicting if salary > 70K)

# --- Optional Challenge ---
# Try training a DecisionTreeRegressor on the same data
# from sklearn.tree import DecisionTreeRegressor
# tree_model = DecisionTreeRegressor()
# tree_model.fit(X_train, y_train)
# tree_pred = tree_model.predict(X_test)
# print("Tree R^2:", r2_score(y_test, tree_pred))
