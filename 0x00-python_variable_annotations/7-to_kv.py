#!/usr/bin/env python3
"""
A module that contains a type annotated func `to-kv`
which takes  param and return a tuple
"""

import typing


tup = typing.Tuple[str, float]


def to_kv(k: str, v: typing.Union[int, float]) -> tup:
    """
    a func that takes in `str: k` and `int | float: v` to return
    A tuple (k, v)
    """
    return (k, v**2)
