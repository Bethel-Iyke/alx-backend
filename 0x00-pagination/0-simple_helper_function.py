#!/usr/bin/env python3
"""  function that takes two integer arguments page and page_size. """


from typing import Tuple


def index_range(page, page_size):
    """function that takes page and page size as arguments """
    start_page = (page - 1) * page_size
    ending_page = (page * page_size)
    size = (start_page, ending_page)
    return size
