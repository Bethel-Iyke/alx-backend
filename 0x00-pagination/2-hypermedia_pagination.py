#!/usr/bin/env python3
"""  function that takes two integer arguments page and page_size. """


from typing import Tuple
import csv
import math
from typing import List


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
        """ method that takes integer argument"""
        assert isinstance(
            page, int) and page > 0, "check argument is int and > 0"
        assert isinstance(
            page_size, int) and page_size > 0, "check argument is int and > 0"
        dataset = self.dataset()
        start_page, ending_page = index_range(page, page_size)
        if start_page >= page_size:
            return []
        return dataset[start_page:ending_page]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Takes page and page size and
        returns a dict of some keys and values."""
        data = self.get_page(page, page_size)
        start_page, ending_page = index_range(page, page_size)
        former_page = None
        if former_page is not None and former_page > 0:
            former_page = page - 1
        page_next = None
        if page_next is not None and page_next < len(self.dataset()):
            page_next = page + 1
        num_page = len(self.dataset())
        num_full_page, remainder = divmod(num_page, page_size)
        total_page = num_full_page + bool(remainder)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page_next,
            "prev_page": former_page,
            "total_pages": total_page}


def index_range(page, page_size):
    """function that takes page and page size as arguments """
    start_page = (page - 1) * page_size
    ending_page = (page * page_size)
    size = (start_page, ending_page)
    return size
