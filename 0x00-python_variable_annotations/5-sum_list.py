#!/usr/bin/env python3
"""
Contains function to sum a list

function:
 * sum_list: sums up a list
"""

from typing import Union, List


def sum_list(input_list: List[Union[int, float]]) -> float:
    """Sums up a list of floats"""
    sum = 0
    for i in input_list:
        sum += i
    return sum
