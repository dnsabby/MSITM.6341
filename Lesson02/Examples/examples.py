"""
Lesson 2 Examples: Advanced Data Types and Algorithms
=====================================================

This file is synchronized with `Lesson02/Exercises/exercises.py`.
Section order in both files:
1) Collections (list, tuple, set, dictionary)
2) Indexing and slicing
3) Control flow and loops
4) Functions and scope
5) Nested data structures
6) Pseudo-code to implementation
"""

import random


# =============================
# Section 1: Collections
# =============================

# Example 1: List operations
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits.remove("banana")
print("List:", fruits)

# Example 2: Tuple operations
coordinates = (10, 20)
print("Tuple:", coordinates)

# Example 3: Set operations
numbers = {1, 2, 3, 3, 4, 5}
numbers.add(6)
numbers.remove(2)
print("Set:", numbers)

# Example 4: Dictionary operations
student = {"name": "Alice", "age": 25, "course": "Python"}
student["age"] = 26
student["email"] = "alice@example.com"
print("Dictionary:", student)


# =============================
# Section 2: Indexing and Slicing
# =============================

languages = ["Python", "Java", "C++", "JavaScript"]
print("First element:", languages[0])
print("Last element:", languages[-1])
print("Middle slice:", languages[1:3])

sentence = "Python programming is fun!"
print("First five chars:", sentence[:5])
print("Every second char:", sentence[::2])


# =============================
# Section 3: Control Flow and Loops
# =============================

number_to_check = 11
if number_to_check % 2 == 0:
    print("Even number")
else:
    print("Odd number")

for index in range(1, 6):
    print(f"For-loop value: {index}")

count = 0
while count < 3:
    print(f"While-loop count: {count}")
    count += 1


# =============================
# Section 4: Functions and Scope
# =============================

global_label = "I am global"


def greet(name):
    """
    Return a simple greeting message.

    Args:
        name (str): Name of the person.

    Returns:
        str: Greeting.
    """
    return f"Hello, {name}!"


def show_scope():
    """
    Demonstrate local and global variables.

    Returns:
        tuple[str, str]: Local label and global label.
    """
    local_label = "I am local"
    return local_label, global_label


print(greet("Alice"))
print("Scope values:", show_scope())


# =============================
# Section 5: Nested Data Structures
# =============================

student_records = {
    "Alice": {"subjects": ["Math", "Science"], "grades": [88, 92]},
    "Bob": {"subjects": ["Math", "History"], "grades": [80, 84]},
}

for student_name, details in student_records.items():
    average_grade = sum(details["grades"]) / len(details["grades"])
    print(f"{student_name} average: {average_grade:.2f}")


# =============================
# Section 6: Pseudo-code and Implementation
# =============================

"""
Pseudo-code: Number Guessing Game
1. Pick a target number between 1 and 20.
2. Read guesses until the user guesses correctly.
3. Tell the user if each guess is too high or too low.
4. Stop when the guess matches the target.
"""


def replayable_guessing_demo(guesses):
    """
    Demonstrate number-guessing logic without interactive input.

    Args:
        guesses (list[int]): Sequence of guesses to test.

    Returns:
        bool: True if the target is guessed, otherwise False.
    """
    target = random.randint(1, 20)
    print(f"(Demo target for instructors: {target})")
    for guess in guesses:
        if guess > target:
            print(f"{guess}: Too high")
        elif guess < target:
            print(f"{guess}: Too low")
        else:
            print(f"{guess}: Correct")
            return True
    print("Target was not guessed in this demo run.")
    return False


replayable_guessing_demo([5, 12, 17, 19])
