'''
Class methods = allow operations repated to the class inself
    Take (cls) as the first parameter, which represents the class itself

Instance methods = best for operations on instances of the class (objects)
Static methods - best for utility functions that do not need access to class data
Class methods - best for class-level data or require access to the class itself
'''

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:      # if there is no student
            return 0
        else:
            return f"Average gpa: {cls.total_gpa/cls.count:.2f}"

print(Student.count)

std1 = Student("Tom", 3.9)
std2 = Student("Jasmine", 3.87)
std3 = Student("Sponebob", 2.08)
std4 = Student("Luise", 3.03)

print(Student.get_count())
print(Student.get_avg_gpa())
