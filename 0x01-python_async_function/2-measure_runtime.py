#!/usr/bin/env python3
"""
hi
"""


import time
import asyncio

wait_n = __import__('1-concurrent_coroutines.py').wait_n


def measure_time(n, max_delay) -> float:
    """
    hi again
    """
    time1 = time().time()
    asyncio.run(wait_n(n, max_delay))
    time2 = time().time()
    ftime = time2 - time1
    av = ftime / n
    return av
