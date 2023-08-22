#!/usr/bin/env python3
"""A a module that conatains a type-annotated func that take
Float as param and returns it's str repr,
"""

import typing


def to_str(n: float) -> str:
    """A func that take float as param and returns str."""
    return n.__str__()
