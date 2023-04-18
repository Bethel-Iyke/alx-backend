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


def index_range(page, page_size):
    """function that takes page and page size as arguments """
    start_page = (page - 1) * page_size
    ending_page = (page * page_size)
    size = (start_page, ending_page)
    return size
