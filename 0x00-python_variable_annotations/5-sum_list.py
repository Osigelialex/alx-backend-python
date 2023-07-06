#!/usr/bin/env python3
"""
Contains function to sum a list

function:
 * sum_list: sums up a list    
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums up a list of floats"""
    total_sum: float = 0.0
    for i in input_list:
        total_sum += i
    return total_sum
