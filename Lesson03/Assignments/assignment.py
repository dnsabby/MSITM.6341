"""
Lesson 3 Assignment: OOP and Modules Refactor
=============================================

Synchronized topics:
- Classes and objects
- Encapsulation
- Modules and imports

Objective:
- Refactor a command-line game (or similar app) using class-based design
  and separate modules.
"""

# =============================
# Assignment Prompt
# =============================
"""
Create an object-oriented version of your previous game/app:
1. Build a class that controls game state (scores, rounds, options).
2. Build a helper module for utility functions (validation, formatting, etc.).
3. Keep your main file focused on program flow only.
4. Add simple text logging for each round to a file.
"""


class GameManager:
    """
    Manage game state and round flow.
    """

    def __init__(self):
        """Initialize game configuration and score tracking."""
        # TODO: Add attributes for score, valid choices, and round count.
        pass

    def play_round(self, user_choice):
        """
        Process one round and update state.

        Args:
            user_choice (str): Player input.

        Returns:
            str: Round result string.
        """
        # TODO: Add round logic and return a result.
        pass

    def summary(self):
        """
        Return final game summary text.

        Returns:
            str: Summary for player and computer score.
        """
        # TODO: Build and return summary message.
        pass


class Logger:
    """
    Simple text logger for assignment events.
    """

    def __init__(self, filename):
        """
        Store output log filename.

        Args:
            filename (str): Log file path.
        """
        self.filename = filename

    def write_line(self, message):
        """
        Append one message line to the log file.

        Args:
            message (str): Text line to write.
        """
        # TODO: Append message to file using `with open(..., "a")`.
        pass


def main():
    """
    Entry point for your class-based assignment.
    """
    # TODO: Initialize GameManager and Logger.
    # TODO: Build input loop and call play_round().
    # TODO: Print final summary.
    pass


if __name__ == "__main__":
    main()
