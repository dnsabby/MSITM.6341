"""
Lesson 1 In-Class Exercises
===========================

Lesson 1 exercises covering:
1) Variables
2) Data Types
3) Operators
4) Control Flow
5) Functions
"""

# ========================
# Section 1: Variables
# ========================

# Exercise 1:
# Define variables for employee name and years of employment.
# Print a sentence using f-string formatting.

employee_name = "Eli"
employment_age = 2
is_employee = True

print(
    f"{employee_name} has been with the company for {employment_age} years, "
    f"and employment status is {is_employee}."
)


# Exercise 2:
# Convert two string numbers to integers.
# Print their sum and division result.

first_number = "20"
second_number = "5"

first_number = int(first_number)
second_number = int(second_number)

print(f"Sum: {first_number + second_number}")
print(f"Division: {first_number / second_number}")


# ========================
# Section 2: Data Types
# ========================

# Exercise 3:
# Create int, float, str, and bool variables.
# Print each variable's data type.

employee_id = 1234
employee_salary = 55000.50
employee_department = "Information Technology"
employee_active = True

print(type(employee_id))
print(type(employee_salary))
print(type(employee_department))
print(type(employee_active))


# ========================
# Section 3: Operators
# ========================

# Exercise 4:
# Define two numbers.
# Print +, -, *, /, and % results.

num_a = 20
num_b = 6

print(f"Addition: {num_a + num_b}")
print(f"Subtraction: {num_a - num_b}")
print(f"Multiplication: {num_a * num_b}")
print(f"Division: {num_a / num_b}")
print(f"Remainder: {num_a % num_b}")


# ========================
# Section 4: Control Flow
# ========================

# Exercise 5:
# Write an if/elif/else block to classify a number as
# positive, negative, or zero.

number_to_check = -5

if number_to_check > 0:
    print("The number is positive.")
elif number_to_check < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Exercise 6:
# Determine whether a number is even or odd.

number = 7

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


# Exercise 7:
# Use a for-loop to print values 1 through 5.

for number in range(1, 6):
    print(number)


# Exercise 8:
# Compute factorial using a while-loop.

factorial_number = 5
factorial_result = 1
current_number = factorial_number

while current_number > 0:
    factorial_result = factorial_result * current_number
    current_number -= 1

print(f"The factorial of {factorial_number} is {factorial_result}.")


# ========================
# Section 5: Functions
# ========================


def add_numbers(left, right):
    """
    Return the sum of two values.

    Args:
        left (int | float): First value.
        right (int | float): Second value.

    Returns:
        int | float: Sum result.
    """
    return left + right


def greet_user(name="Guest"):
    """
    Return a greeting message.

    Args:
        name (str): Optional name to greet.

    Returns:
        str: Greeting text.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(add_numbers(10, 5))

    print(greet_user("Eli"))

    print(greet_user())