#!/usr/bin/env python3

class Shoe:
    # lib/shoe.py


    def __init__(self, brand="Adidas", size=9, color="Black", material="Leather"):
        self.brand = brand
        self.size = size
        self.color = color
        self.material = material
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value > 0:
            self._size = value
        else:
            raise ValueError("Size must be a positive integer.")

    def repair(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
    pass