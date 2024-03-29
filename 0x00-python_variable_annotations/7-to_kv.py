#!/usr/bin/env python3
"""A type annotaated tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    result = (k, float(v) ** 2)
    return result
