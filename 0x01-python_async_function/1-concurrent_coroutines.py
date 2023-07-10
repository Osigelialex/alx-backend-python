#!/usr/bin/env python3
"""
This module executeas coroutines asynchronously

functions:
  * async wait_n: coroutine

imports:
  * wait_random
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawns wait_random n times with specified delay"""
    # create a task for each coroutine which appends to a
    # list of delays
    delays = []

    for i in range(n):
        delays.append(await wait_random(max_delay))

    return delays
