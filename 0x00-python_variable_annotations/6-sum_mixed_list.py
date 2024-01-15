#!/usr/bin/env python3
"""An annotated mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a mixed list and returns sum as a float"""
    return sum(mxd_lst)
