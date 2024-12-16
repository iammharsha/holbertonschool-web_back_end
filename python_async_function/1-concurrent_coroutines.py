#!/usr/bin/env python3
"""Module to execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random 'n' times with the specified max_delay and
    return the list of delays in ascending order without using sort().

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays: List[asyncio.Task[float]] = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    results = []
    for completed_task in asyncio.as_completed(delays):
        result = await completed_task
        results.append(result)

    return results
