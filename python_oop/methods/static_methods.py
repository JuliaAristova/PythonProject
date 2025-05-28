'''
Static methods = a method that belongs to a class rather than any object
    from that class (instance)
    Usually used for general utility functions

Instance methods - best for operations on instances of the class (objects)
Static methods - best for utility functions that do not need access to class data
'''

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


# static method = class_name.method
print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Rocket Scientist"))

emp1 = Employee("Eugene", "Manager")
emp2 = Employee("Squidward", "Cashier")
emp3 = Employee("Spongebob", "Cook")

# instance methods = object_name.method
print(emp1.get_info())
print(emp2.get_info())
print(emp3.get_info())