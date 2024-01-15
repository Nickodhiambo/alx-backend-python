#!/usr/bin/env python3
"""An annotated function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that returns the product of
    a float and the multiplier parameter
    """
    def multiplier_function(x: float) -> float:
        """Returns the product of floats"""
        return (x * multiplier)
    return multiplier_function
