#!/usr/bin/env python3
"""
More involved type annotations
"""

from typing import TypeVar, Union, Mapping, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """more involved type annotation"""
    if key in dct:
        return dct[key]
    else:
        return default
