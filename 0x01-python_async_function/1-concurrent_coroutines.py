#!/usr/bin/env python3
"""
This module contain the solution to task 1: concurrent routines
that describe how to run multiple coroutines at the same time
it uses the asyncio, random and typing module to Answer this
Assessment.
"""

import typing
import asyncio
import random as r


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    A func that runs a coroutine "wait_random" n times within
    max_delay amount of time, and returns the list of the delays
    """
    list_of_delays: typing.List[float] = []
    for _ in range(n):
        worker = asyncio.create_task(wait_random(max_delay))
        rs = await worker
        list_of_delays.append(rs)

    sorts: typing.List[float] = []

    # loop tru the list_of_delays
    while list_of_delays:
        smallestNum = min(list_of_delays)
        sorts.append(smallestNum)
        list_of_delays.remove(smallestNum)
    return sorts
