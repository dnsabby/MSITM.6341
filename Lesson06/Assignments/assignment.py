"""
Lesson 6 Take-Home Assignment: Kaggle Dataset EDA
=================================================

Synchronized topics:
- Data loading and inspection
- Missing-value handling
- Descriptive statistics
- Visualization with matplotlib/seaborn

Important:
- This is a scaffold only; implement all TODO sections.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def load_dataset(file_name):
    """
    Load a CSV file selected by the student.

    Args:
        file_name (str): CSV filename.

    Returns:
        pandas.DataFrame: Loaded dataset.
    """
    # TODO: Implement safe CSV loading with error handling.
    pass


def clean_dataset(df):
    """
    Apply missing-value strategy chosen by the user.

    Args:
        df (pandas.DataFrame): Raw dataset.

    Returns:
        pandas.DataFrame: Cleaned dataset.
    """
    # TODO: Prompt user to choose fill vs drop strategy.
    # TODO: Apply the selected cleaning method.
    pass


def summarize_column(df, column_name):
    """
    Print descriptive statistics for one selected column.

    Args:
        df (pandas.DataFrame): Dataset.
        column_name (str): Column to summarize.
    """
    # TODO: Validate column and print useful summary stats.
    pass


def create_visualizations(df):
    """
    Generate at least two visualizations.

    Args:
        df (pandas.DataFrame): Dataset to plot.
    """
    # TODO: Ask user for plot choices and generate charts.
    # Suggested options: histogram, boxplot, scatterplot, countplot.
    _ = plt, sns
    pass


def main():
    """
    Orchestrate Lesson 6 assignment steps.
    """
    file_name = input(
        "Enter your Kaggle dataset CSV filename (including .csv): "
    ).strip()

    # TODO: Call load_dataset().
    # TODO: Show dataset overview (head/info/missing values).
    # TODO: Call clean_dataset().
    # TODO: Call summarize_column().
    # TODO: Call create_visualizations().
    _ = file_name


if __name__ == "__main__":
    main()
