"""
Lesson 1 Examples: Python Basics
================================

This file is synchronized with `Lesson01/Exercises/exercises.py`.
Section order in both files:
1) Variables and input-ready values
2) Core data types
3) Operators
4) Control flow
5) Functions
"""

# ========================
# Section 1: Variables
# ========================

# Example 1: Defining variables
student_name = "Alice"
student_age = 30
is_enrolled = True
print(
    f"My name is {student_name}, I am {student_age} years old, "
    f"and enrolled status is {is_enrolled}."
)

# Example 2: Updating variable values
student_age = student_age + 1
print(f"Next year, {student_name} will be {student_age}.")

# Example 3: Multiple assignment
x_value, y_value = 5, 10
print(f"x_value: {x_value}, y_value: {y_value}")

# ========================
# Section 2: Data Types
# ========================

# Example 1: Common data types
integer_value = 123
float_value = 3.14
string_value = "Python"
boolean_value = False

# Example 2: Collection data types
list_value = [1, 2, 3]
dict_value = {"key": "value"}
tuple_value = (4, 5, 6)
set_value = {"apple", "banana", "cherry"}

# Example 3: Checking types
print(type(integer_value))
print(type(list_value))

# ========================
# Section 3: Operators
# ========================

# Example 1: Arithmetic operators
num_a, num_b = 15, 4
print(num_a + num_b)
print(num_a - num_b)
print(num_a * num_b)
print(num_a / num_b)
print(num_a % num_b)
print(num_a ** num_b)

# Example 2: Comparison operators
print(num_a > num_b)
print(num_a < num_b)
print(num_a == num_b)

# Example 3: Logical operators
print(num_a > 10 and num_b < 5)
print(num_a > 20 or num_b < 5)

# ========================
# Section 4: Control Flow
# ========================

# Example 1: If-elif-else statement
number_to_check = -3
if number_to_check > 0:
    print("Positive")
elif number_to_check < 0:
    print("Negative")
else:
    print("Zero")

# Example 2: For loop
for index in range(1, 6):
    print(f"Iteration {index}")

# Example 3: While loop
countdown = 3
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1

# ========================
# Section 5: Functions
# ========================


def greet(name):
    """
    Return a simple greeting message.

    Args:
        name (str): Name of the learner.

    Returns:
        str: Greeting message.
    """
    return f"Hello, {name}!"


def greet_with_default(name="Guest"):
    """
    Return a welcome message with a default name.

    Args:
        name (str): Optional visitor name.

    Returns:
        str: Welcome message.
    """
    return f"Welcome, {name}!"


def factorial(number):
    """
    Compute factorial using a loop.

    Args:
        number (int): Non-negative integer.

    Returns:
        int: Factorial result.
    """
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result


print(greet("Alice"))
print(greet_with_default())
print(greet_with_default("Bob"))
print(factorial(5))
