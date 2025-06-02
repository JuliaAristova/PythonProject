'''
Iterables - an object/collection that can return its elements one at a time,
    allowing it to be iterated over in a loop
'''
for i in range(3):
    print(i)

# list
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number, end=" ")
print()

for number in reversed(numbers):
    print(number, end=" - ")
print()

students = ["Hermione", "Harry", "Ron"]
for student in students:
    print(student)

for i in range(len(students)):
    print(i+1, students[i])
# tuple
numbers = (6,7,8,9,0)

for number in numbers:
    print(number, end=" ")
print()

for number in reversed(numbers):
    print(number, end=" - ")
print()

# set  - unordered
fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print( fruit, end = " ")    # order is not supported
print()

# reversed(fruits):   TypeError: 'set' object is not reversible

# string

name = 'Julia Aristova'

for char in name:
    print(char, end = ' ')
print()

for char in reversed(name):
    print(char, end = ' ')
print()
# dictionary

my_dictionary = {"A" : 1, "B" : 2, "C" : 3}

# print keys
for key in my_dictionary:
    print(key, end = ' ')
print()

for key in my_dictionary.keys():
    print(key, end = ' ')
print()

# print values
for value in my_dictionary.values():
    print(value, end = ' ')
print()

# print key and value
for key,value in my_dictionary.items():
    print(f"{key} - {value}")
print()
