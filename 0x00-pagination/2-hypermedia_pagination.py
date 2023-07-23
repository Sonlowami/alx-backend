#!/usr/bin/env python3
"""Contain a helper function to find starting and ending indices
on a page"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Find the range of indices within the page"""
    start: int = page_size * (page - 1)
    end: int = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get all items on the page"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        self.dataset()

        if start > len(self.__dataset) or end > len(self.__dataset):
            return []
        return self.__dataset[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        """Return hypermedia related to the page"""
        if type(page) is not int or type(page_size) is not int:
            return {}
        content: List[List] = self.get_page(page, page_size)
        total = len(self.__dataset)
        size: int = len(content)
        total_pages = math.ceil(total / page_size)
        next_page = page + 1 if page + 1 < total_pages else None

        return {
                'page_size': size,
                'page': page,
                'data': content,
                'next_page': next_page,
                'prev_page': page - 1 or None,
                'total_pages': total_pages
                }
