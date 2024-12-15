#!/usr/bin/env python3
"""Module to add list of int and float numbers"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of all the numbers in the list as a float.
    """
    return sum(mxd_lst)
