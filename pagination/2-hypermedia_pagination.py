#!/usr/bin/env python3
"""Module to implement pagination"""
import csv
import math
from typing import List, Tuple


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
        """
        Get data for page

        Args:
            page (int): Page number.
            page_size (int): The number of items per page.
        """
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        data = self.dataset()
        start_index, end_index = index_range(page, page_size)

        return data[start_index:end_index] if start_index < len(data) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict[str, any]:
        """
        Get data for page

        Args:
            page (int): Page number.
            page_size (int): The number of items per page.

        Returns:
            Dict: Dictionary of page_size, page, next_page,
                prev_page, total_pages, data
        """
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        data = self.dataset()
        start_index, end_index = index_range(page, page_size)
        page_data = (data[start_index:end_index]
                     if start_index < len(data)
                     else [])
        total_pages = math.ceil(len(data) / page_size)

        return {
            "page_size": len(page_data),
            "page": page,
            "next_page": page + 1 if page < total_pages else None,
            "data": page_data,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indexes.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index
