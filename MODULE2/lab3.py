"""Generate the Fibonacci series using recursion."""

from functools import lru_cache

MAX_TERMS = 100

@lru_cache(maxsize=None)
def fibonacci(index: int) -> int:
    """Return the Fibonacci number at index using recursion."""
    if index < 0:
        raise ValueError("Fibonacci index cannot be negative.")
    if index <= 1:
        return index
    return fibonacci(index - 1) + fibonacci(index - 2)

def main() -> None:
    """Read a term count and print the recursive Fibonacci series."""
    number_of_terms = int(input("Enter the number of terms: "))

    if number_of_terms <= 0:
        print("Please enter a positive number of terms.")
        return
    if number_of_terms > MAX_TERMS:
        print(f"Please enter no more than {MAX_TERMS} terms.")
        return

    series = [fibonacci(index) for index in range(number_of_terms)]
    print("Fibonacci series:")
    print(*series)

if __name__ == "__main__":
    main()

