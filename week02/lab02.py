"""Lab 02 function implementations."""


def make_greeting(name: str) -> str:
    """Return a greeting for the supplied name."""
    return f"Hello, {name}!"


def is_even(number: int) -> bool:
    """Return whether the supplied number is even."""
    return number % 2 == 0


def count_vowels(text: str) -> int:
    """Count a, e, i, o, and u without counting y."""
    return sum(character.lower() in "aeiou" for character in text)
