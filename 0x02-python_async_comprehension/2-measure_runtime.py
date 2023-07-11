#!/usr/bin/env python3
"""measures runtime for four parallel comprehensions"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension using asyncio.gather"""
    start = time.perf_counter()
    coro = [async_comprehension() for i in range(4)]
    await asyncio.gather(*coro)
    end = time.perf_counter() - start
    return end
