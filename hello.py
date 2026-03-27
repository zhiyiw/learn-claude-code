"""A simple module that prints a greeting message."""


def greet(name: str = "World") -> None:
    """Print a greeting message to the console.

    Args:
        name: The name of the person to greet. Defaults to "World".
    """
    print(f"Hello, {name}!")


if __name__ == "__main__":
    greet()
