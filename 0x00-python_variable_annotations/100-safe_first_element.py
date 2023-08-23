#!/usr/bin/env python3
"""
this module contains a correct Duck-typing annotation of a func
"""


import typing


re = typing.Union[typing.Any, None]


def safe_first_element(lst: typing.Sequence[typing.Any]) -> re:
    """
    a func that returns the first element of a list.
    """
    if lst:
        return lst[0]
    else:
        return None
