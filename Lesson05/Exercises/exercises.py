#!/usr/bin/env python3
"""
Lesson 5 In-Class Exercises (No Answers)
========================================

This file is scaffold-only.
Complete each TODO step during class.
"""

import csv
import json
import os

import requests

try:
    import pandas as pd
except ImportError:
    pd = None

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def exercise_1():
    """
    API Data Fetch and CSV Conversion.
    """
    print("\n--- Exercise 1 ---")
    url = "https://jsonplaceholder.typicode.com/posts"

    # TODO: Request data from API and handle errors.
    # TODO: Save data to `posts.json`.
    # TODO: Read `posts.json`.
    # TODO: Export selected fields to `posts.csv`.
    _ = requests, url
    pass


def exercise_2():
    """
    Directory analysis and file manipulation.
    """
    print("\n--- Exercise 2 ---")
    dir_name = "data"

    # TODO: Create `data` directory if missing.
    # TODO: Create `file1.txt`, `file2.txt`, `file3.txt`.
    # TODO: Print each file name and file size.
    _ = dir_name
    pass


def exercise_3():
    """
    CSV -> JSON pipeline with optional pandas analysis.
    """
    print("\n--- Exercise 3 ---")
    csv_filename = "students.csv"
    json_filename = "students.json"

    # TODO: Create CSV with header and sample rows.
    # TODO: Read CSV using DictReader into a list.
    # TODO: Write list to JSON.
    # TODO: If pandas available, compute average age and grade.
    _ = csv, json, pd, csv_filename, json_filename
    pass


def main_exercises():
    """
    Run all Lesson 5 exercises.
    """
    exercise_1()
    exercise_2()
    exercise_3()


if __name__ == "__main__":
    main_exercises()
