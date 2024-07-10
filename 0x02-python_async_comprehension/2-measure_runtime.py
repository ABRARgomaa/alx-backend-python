#!/usr/bin/env python3
"""
async
"""


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    async
    """
    time1 = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    time2 = time.time()
    t = time2 - time1
    return t
