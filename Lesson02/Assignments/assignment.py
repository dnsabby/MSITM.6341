"""
Lesson 2 Assignment: Rock-Paper-Scissors
========================================

Synchronized topics:
- Collections, conditionals, loops, and functions
- Translating pseudo-code into runnable logic

Important:
- This file is a scaffold only.
- Implement the TODO logic yourself.
"""

import random


# =============================
# Assignment Prompt
# =============================
"""
Build a Rock-Paper-Scissors game where a user plays against the computer.

Required behavior:
1. Validate user input.
2. Generate random computer choices.
3. Decide the winner for each round.
4. Support multiple rounds.
5. Track and print final score.
"""


# =============================
# Pseudo-code
# =============================
"""
1. Start program and show game rules.
2. Create a list: ["Rock", "Paper", "Scissors"].
3. Repeat until player quits:
   a. Ask player for a choice.
   b. Validate input.
   c. Randomly choose computer option.
   d. Compare choices and determine winner.
   e. Update score counters.
4. Print final score summary.
"""


def play_round(user_choice, computer_choice):
    """
    Determine the outcome of one game round.

    Args:
        user_choice (str): Player choice.
        computer_choice (str): Computer choice.

    Returns:
        str: "win", "lose", or "tie".
    """
    # TODO: Implement round outcome logic.
    pass


def get_user_choice(valid_choices):
    """
    Collect and validate one user choice.

    Args:
        valid_choices (list[str]): Allowed options.

    Returns:
        str: Valid player choice.
    """
    # TODO: Prompt user until a valid option is entered.
    pass


def run_game():
    """
    Manage the full multi-round game flow.

    Returns:
        None
    """
    choices = ["Rock", "Paper", "Scissors"]
    user_score = 0
    computer_score = 0

    # TODO: Implement main gameplay loop and score tracking.
    # TODO: Print a final summary when user exits.
    _ = random.choice(choices)  # Starter line to show random usage.
    _ = user_score, computer_score
    pass


if __name__ == "__main__":
    # TODO: Call `run_game()`.
    pass
