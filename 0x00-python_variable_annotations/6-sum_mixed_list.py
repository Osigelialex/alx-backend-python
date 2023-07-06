#!/usr/bin/env python3
"""
Contains function to sum a list of integers and floats

function:
 * sum_mixed_list: sums up a list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums up a list of integers and floats"""
    total_sum: float = 0.0
    for i in mxd_lst:
        total_sum += i
    return total_sum
