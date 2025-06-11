'''
object - a 'bundle' of related attributes(variables) and methods(functions)
    Ex., phone, cup, book
    You need a 'class' to create many objects

class - blueprint used to gesign the structure and layout of an object

class variables - shared among all instances of a class
    defined outside the constructor
    allow you to share data among all objects created from that class
'''

class Car:
    #constructor
    def __init__(self, model, year,color, for_sale):                 #self - this object - this car
        self.model = model                                           # instant variables - defined inside the construcor
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"Your stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


    #dunder method
    def __str__(self) -> str:
        return (f'Model: {self.model}, \nYear: {self.year}, \nColor: {self.color}, \nFor sale: {self.for_sale}')

    def __add__(self, other) -> str:
        return f'{self.model} & {other.model}'