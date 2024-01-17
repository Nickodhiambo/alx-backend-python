#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a measure_runtime
coroutine that will execute async_comprehension four times in parallel
using asyncio.gather.
measure_runtime should measure the total runtime and return it
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """A coroutune that executes 'async_comprehension' 4 times in parallel
    and measures the total runtime"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    stop_time = time.time()
    return (stop_time - start_time)
