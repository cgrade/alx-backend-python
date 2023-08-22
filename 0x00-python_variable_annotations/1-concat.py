#!/usr/bin/env python3
"""A modulle that contain a type-annotated function,
that take 2 str: as param and return a concatenated str:"""

import typing


def concat(str1: str, str2: str) -> str:
    """A func that concat 2 param string, following type -
    annotation"""
    return str1 + str2
