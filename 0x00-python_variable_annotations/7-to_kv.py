#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""

from typing import List, Union, Tuple

def to_kv(k: str, v: List[Union[int, float]]) -> Tuple[str, float]:
    """returns a tuple containing arguments"""
    return (k, v ** 2)
