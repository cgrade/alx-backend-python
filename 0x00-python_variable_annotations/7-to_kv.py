#!/usr/bin/env python3
"""
A module that contains a type annotated func `to-kv`
which takes  param and return a tuple
"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, int | float]:
    """
    a func that takes in `str: k` and `int | float: v` to return
    A tuple (k, v)
    """
    return (k, v)
