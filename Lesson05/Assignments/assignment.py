#!/usr/bin/env python3
"""
Lesson 5 Take-Home Assignment: Pandas + NumPy Pipeline
=======================================================

Synchronized topics:
- DataFrame creation and inspection
- Converting pandas columns to NumPy arrays
- Vectorized calculations and filtering

Important:
- This file is scaffold-only.
- Complete each TODO without replacing the assignment intent.
"""

import os

try:
    import pandas as pd
except ImportError:
    pd = None

# Keep file behavior consistent from any launch location.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def pandas_numpy_assignment():
    """
    Build a mini analysis pipeline using pandas and NumPy.
    """
    print("\n--- Lesson 5 Assignment: Pandas + NumPy Pipeline ---")

    if pd is None:
        print("Pandas is not installed. Install it before completing this task.")
        return

    # Import NumPy inside the function so students can focus on dependency handling.
    try:
        import numpy as np
    except ImportError:
        print("NumPy is not installed. Install it before completing this task.")
        return

    # Step 1: Create sample data and a DataFrame.
    data = {
        "Student": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
        "Math": [88, 92, 79, 85, 90],
        "Science": [91, 85, 88, 90, 86],
        "English": [85, 87, 90, 82, 88],
    }
    # TODO: Convert `data` into a DataFrame and print preview rows.

    # Step 2: Convert score columns into a NumPy array.
    # TODO: Select numeric subject columns and call `.to_numpy()`.

    # Step 3: Compute per-student averages with NumPy.
    # TODO: Use a vectorized NumPy mean across each row.

    # Step 4: Add average scores back into the DataFrame.
    # TODO: Create a new column such as `Average`.

    # Step 5: Compute class-level subject averages with pandas.
    # TODO: Calculate mean values for Math, Science, and English.

    # Step 6: Filter students above a threshold.
    # TODO: Show students with Math above class Math average.
    _ = np  # Keep linter quiet until TODOs are implemented.


if __name__ == "__main__":
    pandas_numpy_assignment()
