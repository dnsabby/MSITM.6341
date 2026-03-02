"""
Lesson 6 In-Class Exercises (No Answers)
========================================

This file is scaffold-only and aligned with Lesson 6 examples.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = {
    "Player": [
        "LeBron James",
        "Stephen Curry",
        "Kevin Durant",
        "Giannis Antetokounmpo",
        "Nikola Jokic",
        "Luka Doncic",
        "Joel Embiid",
        "James Harden",
        "Jayson Tatum",
        "Devin Booker",
    ],
    "Team": [
        "Lakers",
        "Warriors",
        "Nets",
        "Bucks",
        "Nuggets",
        "Mavericks",
        "76ers",
        "76ers",
        "Celtics",
        "Suns",
    ],
    "Position": ["SF", "PG", "SF", "PF", "C", "PG", "C", "SG", "SF", "SG"],
    "PPG": [27.3, 29.6, 28.5, 29.9, 26.2, 30.2, 33.1, 21.3, 26.7, 27.0],
    "APG": [7.4, 6.3, 5.2, 5.9, 7.8, 8.1, 4.3, 10.5, 4.4, 4.8],
    "RPG": [7.9, 4.5, 7.4, 11.7, 13.8, 9.1, 10.6, 6.2, 8.5, 5.1],
}

df_nba = pd.DataFrame(data)


def numpy_exercise():
    """
    Practice NumPy matrix creation and summary statistics.
    """
    # TODO: Ask for matrix size.
    # TODO: Create random square matrix.
    # TODO: Compute row and column means.
    _ = np
    pass


def pandas_filter_exercise():
    """
    Practice DataFrame filtering based on user input.
    """
    # TODO: Ask for team filter and print matching rows.
    _ = df_nba
    pass


def normalization_exercise():
    """
    Practice min-max normalization on one selected stat column.
    """
    # TODO: Ask for one column (PPG/APG/RPG).
    # TODO: Validate selection.
    # TODO: Create normalized column.
    pass


def eda_exercise():
    """
    Compute aggregate stats for one selected numeric column.
    """
    # TODO: Ask for target column and print mean/median/std.
    pass


def visualization_exercise():
    """
    Generate one selected chart.
    """
    # TODO: Ask which plot to generate.
    # TODO: Build histogram OR scatter OR boxplot.
    _ = plt, sns
    pass


if __name__ == "__main__":
    # TODO: Call each exercise function in sequence.
    pass
