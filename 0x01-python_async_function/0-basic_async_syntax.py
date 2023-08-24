#!/usr/bin/env python3
"""
This module uses the Async/await key word of asyncio package and
the random module, to create coroutine "wait_random" to wait for
events to happen within a certain wait period.
"""


import asyncio
import random as r
import typing


async def wait_random(max_delay: int = 10) -> float:
    """
    an Async function that takes in an integer "max_delay" and wait
    between 0 and max_delay then returns the param "max_delay"
    """
    wt: float = r.uniform(0, max_delay)
    await asyncio.sleep(wt)
    return wt
