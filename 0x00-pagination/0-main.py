#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(2, 10)
print(type(res))
print(res)

res = index_range(page=5, page_size=15)
print(type(res))
print(res)
