#!/usr/bin/env python3
"""
The basics of async
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """returns time waited"""
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
