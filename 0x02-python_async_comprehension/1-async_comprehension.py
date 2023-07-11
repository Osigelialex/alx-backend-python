#!/usr/bin/env python3
"""Async generators"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """performs an async comprehension"""
    return [i async for i in async_generator()]
