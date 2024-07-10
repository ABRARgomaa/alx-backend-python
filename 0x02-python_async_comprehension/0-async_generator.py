#!/usr/bin/env python3
"""
hi
"""


import asyncio
import random


async def async_generator():
    """
    hi again
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0.0, 10.0)
