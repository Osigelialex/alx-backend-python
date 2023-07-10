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
    tasks = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
