#!/usr/bin/env python3
"""
In-Class Examples: Demonstration of Python Modules Individually and in Integration

This script demonstrates:
  1. File Handling: Writing to and reading from a text file.
  2. OS Module: Checking directories and listing files.
  3. Web Requests: Fetching data from a public API.
  4. CSV and JSON Processing: Writing and reading CSV/JSON files.
  5. Pandas: Creating and manipulating a DataFrame.
  6. NumPy: Creating arrays and performing vectorized operations.
  7. Integrated Exercise: Combining all of the above modules into one application.

Synchronization note:
  - This file is aligned with `Lesson05/Exercises/exercises.py`.
"""

import os
import json
import csv
import requests  # pip install requests
import numpy as np  # pip install numpy

# Attempt to import pandas (pip install pandas)
try:
    import pandas as pd
except ImportError:
    pd = None

# Change the working directory to the current file's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# ------------------------------
# Example 1: OS Module Demonstration
# ------------------------------
def demo_os_module():
    """
    Demonstrates usage of the OS module:
      - Print the current working directory.
      - List files and directories.
      - Create a new directory if it doesn't exist.
    """
    print("\n--- Example 1: OS Module Demonstration ---")
    current_dir = os.getcwd()
    print(f"Current working directory: {current_dir}")
    
    # List files and directories
    items = os.listdir(current_dir)
    print("Items in current directory:")
    for item in items:
        print(f"  {item}")
        
    # Create a new directory if it doesn't exist
    new_dir = os.path.join(current_dir, "demo_dir")
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        print(f"Created directory: {new_dir}")
    else:
        print(f"Directory already exists: {new_dir}")
    
    return new_dir

# ------------------------------
# Example 2: File Handling Demonstration
# ------------------------------
def demo_file_handling():
    """
    Demonstrates basic file handling: writing and reading a text file.
    """
    print("\n--- Example 2: File Handling Demonstration ---")
    filename = "example.txt"
    content = ("This is a demonstration of file handling in Python.\n"
               "File I/O is simple using open(), read(), and write().")
    
    # Write content to file
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Wrote to {filename}")
    
    # Read content from file
    with open(filename, 'r') as file:
        read_content = file.read()
    print("Read content from file:")
    print(read_content)


# ------------------------------
# Example 3: Web Requests Demonstration
# ------------------------------
def demo_web_requests():
    """
    Demonstrates making a GET request using the requests module:
      - Fetch data from a public API.
      - Print the JSON response.
    """
    print("\n--- Example 3: Web Requests Demonstration ---")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        print("Fetched data from API:")
        print(json.dumps(data, indent=4))
    except Exception as e:
        print("Error fetching web data:", e)

# ------------------------------
# Example 4: CSV and JSON Processing Demonstration
# ------------------------------
def demo_csv_json_processing():
    """
    Demonstrates CSV and JSON processing:
      - Write sample data to a CSV file.
      - Read the CSV file into a list of dictionaries.
      - Write the data into a JSON file.
    """
    print("\n--- Example 4: CSV and JSON Processing Demonstration ---")
    csv_filename = "sample_data.csv"
    json_filename = "sample_data.json"
    
    header = ["Name", "Age", "City"]
    rows = [
        ["Alice", "30", "New York"],
        ["Bob", "25", "Los Angeles"],
        ["Charlie", "35", "Chicago"]
    ]
    
    # Write CSV file
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(rows)
    print(f"Wrote CSV file: {csv_filename}")
    
    # Read CSV file into list of dictionaries
    data_list = []
    with open(csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_list.append(row)
    print("Data read from CSV:")
    print(data_list)
    
    # Write list of dictionaries to JSON file
    with open(json_filename, 'w') as jsonfile:
        json.dump(data_list, jsonfile, indent=4)
    print(f"Converted CSV data to JSON file: {json_filename}")

# ------------------------------
# Example 5: Pandas Demonstration
# ------------------------------
def demo_pandas():
    """
    Demonstrates basic usage of pandas:
      - Create a DataFrame.
      - Add a computed column.
      - Display basic statistics.
    """
    print("\n--- Example 5: Pandas Demonstration ---")
    if pd is None:
        print("Pandas is not installed.")
        return
    
    data = {
        "Product": ["Apple", "Banana", "Cherry"],
        "Price": [1.2, 0.5, 2.5],
        "Quantity": [10, 20, 15]
    }
    df = pd.DataFrame(data)
    print("Initial DataFrame:")
    print(df)
    
    # Compute a new column: Total cost per product
    df["Total"] = df["Price"] * df["Quantity"]
    print("DataFrame after adding Total column:")
    print(df)
    
    # Display basic statistics
    print("Basic statistics:")
    print(df.describe())

# ------------------------------
# Example 6: NumPy Demonstration
# ------------------------------
def demo_numpy():
    """
    Demonstrates basic usage of NumPy:
      - Create an array.
      - Perform vectorized arithmetic operations.
      - Compute statistics like mean and sum.
    """
    print("\n--- Example 6: NumPy Demonstration ---")
    arr = np.array([1, 2, 3, 4, 5])
    print("Original NumPy array:")
    print(arr)
    
    # Vectorized addition
    arr_plus = arr + 10
    print("Array after adding 10:")
    print(arr_plus)
    
    # Compute statistics
    mean_val = np.mean(arr)
    sum_val = np.sum(arr)
    print(f"Mean of the array: {mean_val:.2f}, Sum of the array: {sum_val}")

# ------------------------------
# Example 7: Integrated Exercise
# ------------------------------
def integrated_exercise():
    """
    An integrated Example that combines:
      - Fetching web data using requests.
      - Saving data to a file using file handling.
      - Using OS module to check file existence.
      - Converting data to CSV and JSON.
      - Loading and analyzing CSV data using pandas and NumPy.
    """
    print("\n--- Example 7: Integrated Example ---")
    
    # Step 1: Fetch data from a web API
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        post_data = response.json()
    except Exception as e:
        print("Error fetching API data:", e)
        return
    
    # Step 2: Save the fetched data to a text file
    txt_filename = "integrated_post.txt"
    with open(txt_filename, 'w') as file:
        file.write(json.dumps(post_data, indent=4))
    print(f"Saved API data to {txt_filename}")
    
    # Step 3: Check file existence using the OS module
    if os.path.exists(txt_filename):
        print(f"Confirmed: {txt_filename} exists.")
    else:
        print(f"Error: {txt_filename} does not exist.")
    
    # Step 4: Convert selected API data to CSV format
    csv_filename = "integrated_post.csv"
    keys = ["userId", "id", "title", "body"]
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerow({k: post_data.get(k, "") for k in keys})
    print(f"Converted API data to CSV: {csv_filename}")
    
    # Step 5: Load CSV with pandas and use NumPy for simple analysis
    if pd:
        try:
            df = pd.read_csv(csv_filename)
            print("Data loaded into DataFrame:")
            print(df)
            # Compute the length of the title using a NumPy array
            title_lengths = np.array([len(str(title)) for title in df['title']])
            print("Length of the title (computed with NumPy):", title_lengths)
        except Exception as e:
            print("Error during integrated analysis:", e)
    else:
        print("Pandas not installed; skipping DataFrame analysis.")

# ------------------------------
# Main Execution
# ------------------------------
def main():
    # The new demo directory created by the file demo_os_module exercise
    new_dir = demo_os_module()
    # Change the working directory to the new directory
    os.chdir(new_dir)

    demo_file_handling()
    #demo_web_requests()
    #demo_csv_json_processing()
    #demo_pandas()
    #demo_numpy()
    #integrated_exercise()

if __name__ == '__main__':
    main()
