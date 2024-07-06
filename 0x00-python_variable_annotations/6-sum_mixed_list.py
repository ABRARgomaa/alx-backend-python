#!/usr/bin/env python3
"""
def def sum_mixed_list
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    def def sum_mixed_list
    """
    sum = 0.0
    for n in mxd_lst:
        sum += float(n)
    return sum
