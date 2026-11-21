"""Play a number guessing game with a limited number of attempts."""

import random

MIN_NUMBER = 1
MAX_NUMBER = 10
MAX_ATTEMPTS = 5

def compare_guess(guess: int, secret_number: int) -> str:
    """Return whether a guess is low, high, or correct."""
    if guess < secret_number:
        return "low"
    if guess > secret_number:
        return "high"
    return "correct"

def read_guess() -> int:
    """Read and validate one guess from the player."""
    while True:
        try:
            guess = int(input(f"Enter your guess ({MIN_NUMBER}-{MAX_NUMBER}): "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if MIN_NUMBER <= guess <= MAX_NUMBER:
            return guess
        print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")

def play_game(secret_number: int | None = None) -> bool:
    """Run one game and return True when the player wins."""
    if secret_number is None:
        secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    elif not MIN_NUMBER <= secret_number <= MAX_NUMBER:
        raise ValueError("Secret number is outside the allowed range.")

    print("========== NUMBER GUESSING GAME ==========")
    print(
        f"Guess the number between {MIN_NUMBER} and {MAX_NUMBER}. "
        f"You have {MAX_ATTEMPTS} attempts."
    )

    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = read_guess()
        result = compare_guess(guess, secret_number)

        if result == "correct":
            print(f"Correct! You guessed the number in {attempt} attempt(s).")
            return True

        direction = "low" if result == "low" else "high"
        attempts_left = MAX_ATTEMPTS - attempt
        print(f"Too {direction}. Attempts remaining: {attempts_left}")

    print(f"Game over! The number was {secret_number}.")
    return False

if __name__ == "__main__":
    play_game()
