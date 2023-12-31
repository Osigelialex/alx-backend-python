#!/usr/bin/env python3
"""
Duck typing iterable object
"""

from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """duck types iterable object"""
    return [(i, len(i)) for i in lst]
