#!/usr/bin/env python3
"""
This Module contain solution to ALX tasks measure_runtime:
it measure the runtimne of a concurrent coroutine and returns
the total time.
"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    a func that measures the execution time of a concurrent
    coroutines
    """
    start_time = time.perf_counter()
    task = await wait_n(n, max_delay)
    stop_time = time.perf_counter()
    total_time = stop_time - start_time
    return total_time
