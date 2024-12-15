#!/usr/bin/env python3
"""Module to manipulate string and int/float to tuples"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with the string k and the square of v as a float.

    Args:
        k (str): A string value.
        v (Union[int, float]): An integer or float value.

    Returns:
        Tuple[str, float]: A tuple where the first element is k,
                        and the second element is the square of v as a float.
    """
    return (k, float(v ** 2))
