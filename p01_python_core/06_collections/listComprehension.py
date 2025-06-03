'''
List comprehension - a consize way to create lists in Python
    Compact and easier to read than traditional loops
    [ expression FOR value IN iterable if condition ]

'''

doubles = []

for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

# list comprehension
doublesN = [ x*2 for x in range (1, 11)]

print(doublesN)

triples = [ x*3 for x in range(1, 11)]
print(triples)

fruits = ['apple', 'orange', 'banana', 'coconut']

fruits = [ s.upper() for s in fruits]
print(fruits)

fruits_chars = [fruit[0] for fruit in fruits]
print(fruits_chars)

numbers = [1, -2, 3, -4, 5, -6, 8, -7, 11]

positive_numbers = [ num for num in numbers if num >= 0]
print(positive_numbers)

negative_numbers = [ num for num in numbers if num < 0]
print(negative_numbers)

even_numbers = [num for num in numbers if num%2==0]
print(even_numbers)

odd_numbers = [num for num in numbers if num%2==1]
print(odd_numbers)

# grades >= 60 - passing
grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)

names = ['anna', 'brenda', 'tom']
name_cap = [name.upper() for name in names]
print(name_cap)
