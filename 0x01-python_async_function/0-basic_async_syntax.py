#!/usr/bin/env python3
"""A simple coroutine using the random module to
generate a random wait time
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Takes in an int parameter with a default value of 10
    and returns a random wait time
    """
    wait_period = random.random() * max_delay
    await asyncio.sleep(wait_period)  # Simulates a non-blocking IO operation
    return (wait_period)
