#!/usr/bin/env python3
"""
A module that contain a a complex type-annnotated
func that takes in float param and returns a func.
"""

import typing


Cal = typing.Callable[float, float]


def make_multiplier(multiplier: float) -> Cal:
    """
    a func that takes in a float `param` and returns
    a callable that multiply a float by `param`
    """
    def mul(x: float) -> float:
        """
        a func that takes 1 param `x: float` multiply it
        by `multiplier: float` and returns it.
        """
        return x * multiplier
    return mul
