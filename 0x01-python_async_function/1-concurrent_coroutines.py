#!/usr/bin/env python3
"""
This module executeas coroutines asynchronously

functions:
  * async wait_n: coroutine

imports:
  * wait_random
"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawns wait_random n times with specified delay"""
    delays = []

    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    return delays
