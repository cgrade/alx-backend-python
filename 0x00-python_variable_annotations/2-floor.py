#!/usr/bin/env python3
"""A script that contains type-annotated func
that takes a float `n` as argument and returns
the floor of the float
"""

import math
import typing


def floor(n: float) -> int:
    """A func that takes in `n` float as param
    and return the Float Custom type"""
    return math.floor(n)
