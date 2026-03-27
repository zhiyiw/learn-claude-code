"""A simple utility module with basic functions."""

from typing import Union


def greet(name: str) -> str:
    """Return a greeting message for the given name.

    Args:
        name: The name to include in the greeting.

    Returns:
        A greeting string in the format "Hello, {name}!"
    """
    return f"Hello, {name}!"


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers and return the result.

    Args:
        a: The first number to add.
        b: The second number to add.

    Returns:
        The sum of a and b.
    """
    return a + b


if __name__ == "__main__":
    # Basic tests for the module functions
    print("Testing greet() function:")
    test_names = ["World", "Alice", "Bob"]
    for name in test_names:
        print(f"  {greet(name)}")

    print("\nTesting add_numbers() function:")
    test_pairs = [(1, 2), (3.5, 4.5), (10, -5)]
    for a, b in test_pairs:
        result = add_numbers(a, b)
        print(f"  {a} + {b} = {result}")
