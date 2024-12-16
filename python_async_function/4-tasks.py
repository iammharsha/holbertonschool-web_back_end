#!/usr/bin/env python3
"""Module to execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random 'n' times with the specified max_delay
    and return the list of delays in ascending order without using sort.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays: List[float] = []
    tasks: List[asyncio.Task] = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
