#!/usr/bin/env python3
"""Module that takes an integer and return asycnio.Task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task that wraps the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: An asyncio Task object that schedules
                        the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
