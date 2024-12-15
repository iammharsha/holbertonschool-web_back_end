#!/usr/bin/env python3
"""Module that multiplies a float by the given multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float
                    and returns the result of multiplying it by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
