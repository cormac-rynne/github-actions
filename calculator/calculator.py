# calculator.py
import numpy as np


def add(a, b):
    return np.add(a, b)


def subtract(a, b):
    return np.subtract(a, b)


def multiply(a, b):
    return np.multiply(a, b)


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return np.divide(a, b)


def test():
    print(
        "This line is intentially too long, designed to trigger the flake8 line length. The quick brown fox jumped over the lazy dog"
    )


def nothing():
    return 1
