"""
Lesson 1 Assignment: Python Basics
==================================

Synchronized topics:
- Variables, data types, and operators
- Conditionals and basic function design

Important:
- This file is a starter scaffold.
- Complete the TODO sections yourself.
"""


# =============================
# Task 1: Simple Calculator
# =============================
"""
Goal:
- Ask the user for two numbers and one operator (+, -, *, /).
- Return the calculated result.

Pseudo-code:
1. Read two numeric inputs.
2. Read an operator string.
3. Use conditional logic to match the operator.
4. Handle division-by-zero safely.
5. Print the final result.
"""


def calculate(num_one, num_two, operator):
    """
    Calculate a result using two numbers and one operator.

    Args:
        num_one (float): First number.
        num_two (float): Second number.
        operator (str): Arithmetic operator (+, -, *, /).

    Returns:
        float | str: Numeric result or a friendly error message.
    """
    # TODO: Implement operator handling with if/elif/else.
    # TODO: Add division-by-zero protection.
    pass


# =============================
# Task 2: Area of a Rectangle
# =============================
"""
Goal:
- Compute rectangle area using length and width values.

Pseudo-code:
1. Read length and width inputs.
2. Convert inputs to numbers.
3. Validate that both values are positive.
4. Calculate area.
5. Print the area.
"""


def rectangle_area(length, width):
    """
    Return the area of a rectangle.

    Args:
        length (float): Rectangle length.
        width (float): Rectangle width.

    Returns:
        float: Computed area.
    """
    # TODO: Validate inputs and return the computed area.
    pass


if __name__ == "__main__":
    # TODO: Collect inputs and call `calculate`.
    # TODO: Collect inputs and call `rectangle_area`.
    pass
