#!/usr/bin/env python3
"""Module to add list of float numbers"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return sum of list of float numbers.

    Args:
        input_list (List[float]): The list of numbers.

    Returns:
        float: Sum of float numbers in input_list.
    """
    return sum(input_list)
