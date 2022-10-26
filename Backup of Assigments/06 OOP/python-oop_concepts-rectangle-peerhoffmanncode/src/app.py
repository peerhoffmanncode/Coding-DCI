import unittest
import math

from check import print_rectangle_properties


class Rectangle:
    """class representing a rectangle"""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_area(self) -> float:
        """return the area of the rectangle"""
        return self.width * self.height

    def get_perimeter(self) -> float:
        """return the perimeter of the rectangle"""
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self) -> float:
        """return the diagonal of the rectangle"""
        return math.sqrt(pow(self.width, 2) + pow(self.height, 2))

    def get_width(self) -> float:
        """return the width of the rectangle"""
        return self.width

    def get_height(self) -> float:
        """return the hight of the rectangle"""
        return self.height


def main():
    rect_a = Rectangle(9.0, 12.0)
    rect_b = Rectangle(17.0, 13.0)

    ### official test cases
    print_rectangle_properties(rect_a)
    print_rectangle_properties(rect_b)

    ### in-official test cases
    rect_c = Rectangle(3.5, 4321.0)
    rect_d = Rectangle(1234.0, 3.333333)
    print_rectangle_properties(rect_c)
    print_rectangle_properties(rect_d)


if __name__ == "__main__":
    main()
