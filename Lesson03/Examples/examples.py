"""
Lesson 3 Examples: OOP, Modules, and Packages
==============================================

This file is synchronized with `Lesson03/Exercises/exercises.py`.
Section order in both files:
1) Classes and objects
2) Inheritance
3) Encapsulation
4) Modules
5) Packages
6) Polymorphism
"""

import math
import random

import my_module
from mypackage import module1, module2


# ========================
# Section 1: Classes and Objects
# ========================


class Car:
    """Represent a car with basic descriptive fields."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        """
        Return a user-friendly description of the car.

        Returns:
            str: Car description.
        """
        return f"{self.year} {self.brand} {self.model}"


car_one = Car("Toyota", "Camry", 2022)
print(car_one.display_info())


# ========================
# Section 2: Inheritance
# ========================


class Person:
    """Represent a person with name and age."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        """
        Return base person details.

        Returns:
            str: Person info.
        """
        return f"{self.name} ({self.age} years old)"


class Student(Person):
    """Extend Person with a student identifier."""

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_info(self):
        """
        Return student details including inherited data.

        Returns:
            str: Student info.
        """
        return f"{super().get_info()} | ID: {self.student_id}"


student_one = Student("Alice", 20, "S12345")
print(student_one.get_info())


# ========================
# Section 3: Encapsulation
# ========================


class BankAccount:
    """Protect account balance using a private attribute."""

    def __init__(self, owner, opening_balance):
        self.owner = owner
        self.__balance = opening_balance

    def deposit(self, amount):
        """
        Add funds to the account when amount is valid.

        Args:
            amount (float): Deposit value.
        """
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        """
        Withdraw funds if balance is sufficient.

        Args:
            amount (float): Withdrawal value.
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        """
        Safely return current account balance.

        Returns:
            float: Current balance.
        """
        return self.__balance


account = BankAccount("John Doe", 1000)
account.deposit(250)
account.withdraw(100)
print("Balance:", account.get_balance())


# ========================
# Section 4: Modules
# ========================

print(my_module.greet("Dennis"))
print("Square root of 16:", math.sqrt(16))
print("Random integer 1-10:", random.randint(1, 10))


# ========================
# Section 5: Packages
# ========================

print("module1.add(5, 3):", module1.add(5, 3))
print("module2.subtract(10, 4):", module2.subtract(10, 4))


# ========================
# Section 6: Polymorphism
# ========================


class Shape:
    """Base class for shape area calculations."""

    def area(self):
        """
        Return default area for unknown shapes.

        Returns:
            float: Area value.
        """
        return 0.0


class Circle(Shape):
    """Circle shape that overrides area behavior."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Compute circle area.

        Returns:
            float: Circle area.
        """
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    """Rectangle shape with custom area formula."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Compute rectangle area.

        Returns:
            float: Rectangle area.
        """
        return self.width * self.height


for shape in [Shape(), Circle(5), Rectangle(4, 6)]:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")
