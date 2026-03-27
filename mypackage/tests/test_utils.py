"""Unit tests for the utils module."""

import pytest
from mypackage.utils import add, multiply, greet


class TestAdd:
    """Tests for the add function."""

    def test_add_positive_numbers(self) -> None:
        assert add(2, 3) == 5

    def test_add_negative_numbers(self) -> None:
        assert add(-1, -1) == -2

    def test_add_mixed_numbers(self) -> None:
        assert add(-1, 1) == 0


class TestMultiply:
    """Tests for the multiply function."""

    def test_multiply_positive_numbers(self) -> None:
        assert multiply(2, 3) == 6

    def test_multiply_by_zero(self) -> None:
        assert multiply(5, 0) == 0

    def test_multiply_negative_numbers(self) -> None:
        assert multiply(-2, -3) == 6


class TestGreet:
    """Tests for the greet function."""

    def test_greet_default_name(self) -> None:
        assert greet() == "Hello, World!"

    def test_greet_custom_name(self) -> None:
        assert greet("Alice") == "Hello, Alice!"
