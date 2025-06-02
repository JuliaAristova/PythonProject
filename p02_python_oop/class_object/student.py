class Student:

    #class variables; good practice - to access with Class name, not an object
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name                        # self referes to an object itself (ex., student1)
        self.age = age
        Student.num_students += 1               # class variable


student1 = Student('Spongebob', 30)
student2 = Student('Patrick', 35)

print(student1.name, student1.age, Student.class_year, Student.num_students)
print(student2.name, student2.age, Student.class_year, Student.num_students)

student3 = Student("Sophie", 26)
print(student3.name, student3.age, Student.class_year, Student.num_students)


print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)
