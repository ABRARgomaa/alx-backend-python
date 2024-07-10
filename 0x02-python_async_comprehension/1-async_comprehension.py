#!/usr/bin/env python3
"""
hi
"""


import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    hi again
    """
    result = []
    async for i in async_generator():
        result.append(i)
    return(result)
