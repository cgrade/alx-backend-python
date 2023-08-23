#!/usr/bin/env python3
"""
This module contains variables that are corretly typed
annotated
"""

import typing


re = typing.List[typing.Tuple[typing.Sequence, int]]


def element_length(lst: typing.Iterable[typing.Sequence]) -> re:
    """
    a func that take `lst: list` as param and returns each element of
    the list and it's length
    """
    return [(i, len(i)) for i in lst]
