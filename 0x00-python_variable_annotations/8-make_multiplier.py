#!/usr/bin/env python3
"""
def make_multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    retrun fun
    """
    def mul(x: float) -> float:
        return multiplier * x
    return mul
