#!/usr/bin/python3
"""square module"""


class Square():
    """square class"""
    width = 0
    height = 0

    def __init__(self, width, height):
        """class constructor"""
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """perimeter of a square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """updating __str__"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(12, 9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
