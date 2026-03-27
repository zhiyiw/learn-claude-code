"""Utility functions for basic operations."""


def add(a: int, b: int) -> int:
    """Return the sum of two integers.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        The sum of a and b.
    """
    return a + b


def multiply(a: int, b: int) -> int:
    """Return the product of two integers.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        The product of a and b.
    """
    return a * b


def greet(name: str = "World") -> str:
    """Generate a greeting message.

    Args:
        name: The name to include in the greeting. Defaults to "World".

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"
