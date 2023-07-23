#!/usr/bin/env python3
"""Contain a helper function to find starting and ending indices
on a page"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Find the range of indices within the page"""
    start: int = page_size * (page - 1)
    end: int = start + page_size
    return start, end
