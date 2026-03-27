"""
module.py - Core functionality for new_module.

This module provides utility functions including greeting, arithmetic operations,
and data processing capabilities. It demonstrates proper Python documentation
and coding practices.

Functions:
    greet(name): Return a personalized greeting message.
    add_numbers(a, b): Add two numbers and return the result.
    calculate_average(numbers): Calculate the average of a list of numbers.
"""

from typing import List, Union


def greet(name: str) -> str:
    """
    Generate a personalized greeting message.

    Args:
        name (str): The name to include in the greeting. Should be a non-empty string.

    Returns:
        str: A formatted greeting message.

    Raises:
        ValueError: If the name is empty or contains only whitespace.

    Examples:
        >>> greet("Alice")
        'Hello, Alice! Welcome!'
        >>> greet("Bob")
        'Hello, Bob! Welcome!'
    """
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("Name cannot be empty or whitespace only")
    
    return f"Hello, {cleaned_name}! Welcome!"


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers together.

    Args:
        a (int | float): The first number to add.
        b (int | float): The second number to add.

    Returns:
        int | float: The sum of the two input numbers.

    Raises:
        TypeError: If either argument is not a numeric type.

    Examples:
        >>> add_numbers(5, 3)
        8
        >>> add_numbers(2.5, 1.5)
        4.0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    
    return a + b


def calculate_average(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (List[int | float]): A non-empty list of numeric values.

    Returns:
        float: The arithmetic mean of the input numbers.

    Raises:
        ValueError: If the list is empty or contains non-numeric elements.
        TypeError: If the input is not a list.

    Examples:
        >>> calculate_average([1, 2, 3, 4])
        2.5
        >>> calculate_average([10.5, 20.5, 30.0])
        20.333333333333332
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    
    # Validate all elements are numeric
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError(f"All elements must be numbers, got {type(num).__name__}")
    
    return sum(numbers) / len(numbers)


class DataProcessor:
    """
    A class to process and manipulate numeric data.

    This class provides methods for common data processing tasks like filtering,
    sorting, and transforming lists of numbers.

    Attributes:
        data (List[Union[int, float]]): The list of numbers being processed.

    Examples:
        >>> processor = DataProcessor([3, 1, 4, 1, 5])
        >>> processor.get_sorted()
        [1, 1, 3, 4, 5]
        >>> processor.filter_positive()
        [3, 1, 4, 1, 5]
    """

    def __init__(self, data: List[Union[int, float]]):
        """
        Initialize the DataProcessor with a list of numbers.

        Args:
            data (List[int | float]): The initial list of numeric values.

        Raises:
            ValueError: If the input list is empty.
            TypeError: If any element in the list is not numeric.
        """
        if not isinstance(data, list):
            raise TypeError("Data must be a list")
        
        if len(data) == 0:
            raise ValueError("Data list cannot be empty")
        
        for i, item in enumerate(data):
            if not isinstance(item, (int, float)):
                raise TypeError(f"Element at index {i} is not numeric: {type(item).__name__}")
        
        self.data = data.copy()

    def get_sorted(self) -> List[Union[int, float]]:
        """
        Return a sorted copy of the data.

        Returns:
            List[int | float]: A new list containing the sorted numbers in ascending order.
        """
        return sorted(self.data)

    def filter_positive(self) -> List[Union[int, float]]:
        """
        Filter and return only positive numbers from the data.

        Returns:
            List[int | float]: A list containing only the positive values.
        """
        return [num for num in self.data if num > 0]

    def transform(self, multiplier: Union[int, float]) -> List[Union[int, float]]:
        """
        Multiply all numbers by a given factor and return the result.

        Args:
            multiplier (int | float): The value to multiply each element by.

        Returns:
            List[int | float]: A new list with transformed values.

        Raises:
            TypeError: If the multiplier is not numeric.
        """
        if not isinstance(multiplier, (int, float)):
            raise TypeError("Multiplier must be a number")
        
        return [num * multiplier for num in self.data]

    def get_statistics(self) -> dict:
        """
        Calculate basic statistics for the data.

        Returns:
            dict: A dictionary containing count, sum, min, max, and average of the data.
        """
        return {
            "count": len(self.data),
            "sum": sum(self.data),
            "min": min(self.data),
            "max": max(self.data),
            "average": calculate_average(self.data)
        }
