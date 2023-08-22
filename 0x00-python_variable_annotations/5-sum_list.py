#!/usr/bin/env python3
"""A module that contains a type annotated func
that takes in list of float an return their sum
"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """A func that takes in list of float as param and return
    float"""
    sum: float = 0.0
    for elem in input_list:
        sum += elem
    return sum
