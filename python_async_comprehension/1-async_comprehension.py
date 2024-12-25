#!/usr/bin/env python3
"""Async Comprehension"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over the async_generator coroutine.

    Returns:
        List[float]: A list of 10 random float numbers.
    """
    return [value async for value in async_generator()]
