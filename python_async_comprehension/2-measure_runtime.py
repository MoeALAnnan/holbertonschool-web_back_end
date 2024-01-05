#!/usr/bin/env python3
"""
Run time for four parallel comprehension
"""

import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times
    in parallel using asyncio.gather,
    and measures the total runtime
    """
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = asyncio.get_running_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
