"""
Lesson 7 In-Class Exercises (No Answers)
========================================

This file is scaffold-only and aligned with Lesson 7 examples.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

data = {
    "StudentID": [101, 102, 103, 104, 105, 106, 107],
    "Hours_Studied": [5, 3, 8, 2, 7, 6, 1],
    "Attendance_Rate": [0.9, 0.6, 0.95, 0.5, 0.8, 0.85, 0.4],
    "Assignments_Completed": [10, 7, 12, 6, 11, 10, 4],
    "Passed": [1, 0, 1, 0, 1, 1, 0],
}

df = pd.DataFrame(data)


def exploration_exercise():
    """
    Inspect the dataset and basic quality metrics.
    """
    # TODO: Print head(), isnull().sum(), and describe().
    pass


def visualization_exercise():
    """
    Create pairplot and correlation heatmap.
    """
    # TODO: Build pairplot for numeric features.
    # TODO: Build annotated heatmap.
    _ = plt, sns
    pass


def preprocessing_exercise():
    """
    Prepare model features and train/test split.
    """
    # TODO: Select feature columns and target.
    # TODO: Apply normalization (optional but recommended).
    # TODO: Split into train/test sets.
    pass


def modeling_exercise():
    """
    Train and evaluate a RandomForest classifier.
    """
    # TODO: Initialize model.
    # TODO: Fit model with training data.
    # TODO: Predict test labels.
    # TODO: Print accuracy and classification report.
    _ = RandomForestClassifier, train_test_split
    _ = accuracy_score, classification_report
    pass


def feature_importance_exercise():
    """
    Plot model feature importance.
    """
    # TODO: Create feature importance DataFrame.
    # TODO: Plot with seaborn bar chart.
    pass


if __name__ == "__main__":
    # TODO: Call exercises in order.
    pass
