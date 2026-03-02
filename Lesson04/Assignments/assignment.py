"""
Lesson 4 Group Assignment: Hangman
==================================

Synchronized topics:
- Functions and modular design
- Loops, conditionals, and input validation

Important:
- Work in groups of 2-5.
- This file is a scaffold only.
"""

# =============================
# Assignment Directions
# =============================
"""
Build a Hangman game with module-based structure.

Required components:
1. A main script that controls gameplay.
2. A helper module containing reusable functions.
3. Pseudo-code comments describing each function.
4. A replay option.
"""


# =============================
# Pseudo-code Outline
# =============================
"""
1. Choose a secret word from a list.
2. Initialize guessed letters and remaining tries.
3. Show current hidden word state.
4. Ask user for one letter.
5. Validate guess and update game state.
6. Repeat until win or lose.
7. Ask whether to play again.
"""


def choose_word(word_list):
    """
    Select a secret word.

    Args:
        word_list (list[str]): Candidate words.

    Returns:
        str: Secret word.
    """
    # TODO: Return one word from the list.
    pass


def display_word(secret_word, guessed_letters):
    """
    Build display text with underscores for missing letters.

    Args:
        secret_word (str): Target word.
        guessed_letters (set[str]): Guessed characters.

    Returns:
        str: Display form of the word.
    """
    # TODO: Build and return masked word string.
    pass


def process_guess(secret_word, guessed_letters, guess, tries_left):
    """
    Update state based on a user guess.

    Args:
        secret_word (str): Target word.
        guessed_letters (set[str]): Existing guesses.
        guess (str): New guess from user.
        tries_left (int): Remaining attempts.

    Returns:
        tuple[set[str], int]: Updated guessed set and tries left.
    """
    # TODO: Update guessed letters and tries.
    pass


def play_hangman():
    """
    Coordinate one full game round.
    """
    # TODO: Implement the game loop.
    pass


if __name__ == "__main__":
    # TODO: Add replay loop calling play_hangman().
    pass
