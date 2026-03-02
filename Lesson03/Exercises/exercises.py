"""
Lesson 3 In-Class Exercises (No Answers)
========================================

This file is scaffold-only.
Implement each class/function during practice.
"""

import os

import math_operations
from geometry import circle, rectangle

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# ========================
# Exercise 1: Classes and Objects
# ========================


class Book:
    """Represent one book with core metadata."""

    def __init__(self, title, author, year):
        # TODO: Store constructor inputs as instance attributes.
        pass

    def book_info(self):
        """
        Return one formatted summary string for the book.
        """
        # TODO: Return formatted book description.
        pass


# ========================
# Exercise 2: Inheritance
# ========================


class Person:
    """Base class for person data."""

    def __init__(self, name, age):
        # TODO: Initialize name and age.
        pass

    def get_info(self):
        """Return base info text."""
        # TODO: Return person info string.
        pass


class Student(Person):
    """Subclass that adds student-specific data."""

    def __init__(self, name, age, student_id):
        # TODO: Call parent initializer and store student_id.
        pass

    def get_info(self):
        """Return combined info including student ID."""
        # TODO: Override and extend parent info.
        pass


# ========================
# Exercise 3: Encapsulation
# ========================


class BankAccount:
    """Practice private attributes and controlled updates."""

    def __init__(self, owner, balance):
        # TODO: Store owner and create private balance.
        pass

    def deposit(self, amount):
        # TODO: Add validation and update balance.
        pass

    def withdraw(self, amount):
        # TODO: Add validation and update balance.
        pass

    def get_balance(self):
        # TODO: Return current balance.
        pass


# ========================
# Exercise 4: Working with Modules
# ========================

# TODO: Call add, subtract, multiply, and divide functions
# from `math_operations.py`.
_ = math_operations


# ========================
# Exercise 5: Using Packages
# ========================

# TODO: Call area/circumference helpers from `geometry/circle.py`.
# TODO: Call area helper from `geometry/rectangle.py`.
_ = circle, rectangle


# ========================
# Exercise 6: Polymorphism
# ========================


class Shape:
    """Base class for polymorphism exercise."""

    def area(self):
        # TODO: Return default area value.
        pass


class CircleShape(Shape):
    """Circle subclass."""

    def __init__(self, radius):
        # TODO: Store radius.
        pass

    def area(self):
        # TODO: Return circle area.
        pass


class RectangleShape(Shape):
    """Rectangle subclass."""

    def __init__(self, width, height):
        # TODO: Store width and height.
        pass

    def area(self):
        # TODO: Return rectangle area.
        pass


if __name__ == "__main__":
    # TODO: Instantiate each class and print practice results.
    pass
