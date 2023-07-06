#!/usr/bin/env python3
"""
task Checking
"""

from typing import List, Tuple, Union


def zoom_array(lst: Union[List[int], Tuple[int, ...]], factor: int = 2) -> Union[List[int], Tuple[int, ...]]:
    """validates type checking"""
    zoomed_in = [
        item
        for item in lst
        for _ in range(factor)
    ]
    return (zoomed_in)


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
