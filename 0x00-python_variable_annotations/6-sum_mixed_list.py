#!/usr/bin/env python3
"""A module that contains a type annotated func
that takes in list of float an return their sum
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """A func that takes in list of float as param and return
    float"""
    sum: float = 0.0
    for elem in mxd_lst:
        sum += elem
    return sum
