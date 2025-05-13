#!/usr/bin/env python3

class Book:
    # lib/book.py


    def __init__(self, title="", author=""):
        self._title = ""
        self._author = ""
        self._page_count = 0

        self.title = title   # uses setter
        self.author = author # uses setter
        self.page_count = 0

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._title = value
        else:
            raise ValueError("Title must be a non-empty string.")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, str):
            self._author = value
        else:
            raise ValueError("Author must be a string.")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int) and value >= 0:
            self._page_count = value
        else:
            raise ValueError("Page count must be a non-negative integer.")

    def turn_page(self):
        print("Flipping the page...")
    pass
    
        