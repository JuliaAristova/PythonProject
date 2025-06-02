'''
Polymorphism - Greek - "HAve many forms or faces"
    Poly = many
    Morphe = form

TWO ways to achieve polyporphism
1. Inheritance - an object could be treated of the same type as a parent class
2. "Duck typing" = object must have necessary attributes/methods

'''
from abc import ABC, abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, hight):
        self.base = base
        self.height = hight

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):

    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

circle = Circle(2)  # circle is a Circle and a Shape

square = Square(2)

shapes = [Circle(4), Square(5), Triangle(6, 7)]

for shape in shapes:
    print(shape.area())


shapes2 = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni",15)]

for shape in shapes2:
    print(shape.area())