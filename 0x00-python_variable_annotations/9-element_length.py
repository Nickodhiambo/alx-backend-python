#!/usr/bin/env python3
"""Annotated function"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a tuple constituting a string and its length"""
    return [(i, len(i)) for i in lst]
