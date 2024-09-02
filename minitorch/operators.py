"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def mul(a: float, b: float) -> float:
    """
    Multiplies two numbers.

    Args: 
        a: a floating point number
        b: a floating point number

    Returns:
        floating point number
    """
    return a * b

def id(a: float) -> float:
    """
    Returns the input unchanged.

    Args:
        a: a floating point number

    Returns:
        a floating point number
    """
    return a

def add(a: float, b: float) -> float:
    """
    Adds two numbers.

    Args:
        a: a floating point number
        b: a floating point number

    Returns:
        a floating point number
    """
    return a + b

def neg(x: float) -> float:
    """
    Negates a number.

    Args: 
        x: a floating point number

    Returns:
        a floating point number
    """
    return -1*x

def lt(a: float, b: float) -> bool:
    """
    Checks if one number is less than the other.

    Args:
        a: a floating point number
        b: a floating point number

    Returns:
        boolean value
    """
    return a < b

def eq(a: float, b: float) -> bool:
    """
    Checks if two numbers are equal.

    Args: 
        a: a floating point number
        b: a floating point number

    Returns:
        a floating point number
    """
    return a == b

def max(a: float, b: float) -> bool:
    """
    Returns the larger of two numbers.

    Args:
        a: a floating point number
        b: a floating point number

    Returns:
        a floating point number
    """
    return a if a > b else b

def is_close(a: float, b: float) -> bool:
    """
    Checks if two numbers are close in value.

    Args: 
        a: a floating point number
        b: a floating point number

    Returns:
        a floating point number
    """
    return abs(a, b) < 1e-2

def sigmoid(x: float) -> float:
    """
    Calculates the sigmoid function.

    Args:
        x: a floating point number

    Returns:
        a floating point number
    """
    return 1/(1+exp(-1*abs(x)))

def relu(x: float) -> float:
    """
    Applies the ReLU activation function.

    Args:
        x: a floating point number

    Returns:
        a floating point number
    """
    return max(0.0, x)

def log(x: float) -> float:
    return math.log(x)

def exp(x: float) -> float:
    return exp(x)

def inv(x: float) -> float:
    return x**-1

def log_back(a: float, b: float) -> float:
    return exp(a) * b

def inv_back(a: float, b: float) -> float:
    return (-1)*(a**-2) * b

def relu_back(a: float, b:float) -> float:
    return 1*b if a > 0 else 0

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
