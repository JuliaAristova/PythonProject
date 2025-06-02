'''
super() - function used in a child class to call methods from a parent class (superclass).
    Allows you to extend functionality of the inherited methods.

'''
from random import triangular


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}.")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with the area of {3.14 * self.radius*self.radius} sq.cm.")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with the area of {self.width*self.width} sq.cm.")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, hight):
        super().__init__(color, is_filled)
        self.width = width
        self.hight = hight

    def describe(self):
        print(f"It is a triangle with the area of {self.width*self.hight/2} sq.cm.")
        super().describe()


circle = Circle('red', True, 5)
square = Square('green', True, 7)
triangle = Triangle('blue', False, 4, 8)

circle.describe()
square.describe()
triangle.describe()
