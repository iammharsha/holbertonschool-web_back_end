#!/usr/bin/env python3
"""Module to return element length"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element of the input iterable
    and its corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
                                    a sequence and its length as an integer.
    """
    return [(i, len(i)) for i in lst]
