#!/usr/bin/env python3
"""
Contains function to sum a list of integers and floats

function:
 * sum_mixed_list: sums up a list
"""

from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """Sums up a list of integers and floats"""
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
