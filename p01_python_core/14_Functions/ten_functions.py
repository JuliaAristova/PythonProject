name = "Tom"
age = 30

# 1 - PRINT

print('Name:', name, "\nAge:" , age)
print('Java', 'Python', 'JavaScript', sep=' | ')

print(f"{name} - {age}")

fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit, end =" ")

# 2 - HELP - return documentation, describes user-defined function
#help(print)

def add_func(a, b):
    """
    a: value 1
    b: value 2
    returns a + b
    """
    return a+b

help(add_func)

# 3 - RANGE
rng = range(10)   # 10 is not included
print(list(rng))

rng2 = range(2, 8) # start, stop -excluded
print(list(rng2))

rng3 = range(1,11, 2) # start, stop, step
print(list(rng3))

rng4 = range(10, -10, -2)
print(list(rng4))

# 4 - MAP
strings = ['Java', 'Python', 'C', 'JavaScript']

lengths = map(len, strings)
print(list(lengths))

strings2 = map(lambda s: s + " language", strings)
print(list(strings2))


def concat_lang(string):
    return string + ' programming language'

strings3 = map(concat_lang, strings)
print(list(strings3))

# 5 - FILTER

def longer_than_4(string):
    return len(string) > 4

lan = filter(longer_than_4, strings)
print(list(lan))

lan2 = filter(lambda s: len(s) > 4, strings)
print(list(lan2))

# 6 - SUM

numbers = {1 ,4, 8,23, 59}
print(f"Sum = {sum(numbers)}")
print(sum(numbers, start=10))
print(sum(numbers, start=-10))

# 7 - SORT

nums = [4, 5, 2, 3, -1, 0, 9]

sorted_nums = sorted(nums)
print(sorted_nums)

print(sorted(nums, reverse=True))

people = [
    {"name": "Alice", "age": 30 },
    {"name": "David", "age": 25 },
    {"name": "Bob", "age": 35 },
    {"name": "Charlie", "age": 20 }
]
sorted_people_age = sorted(people, key = lambda  person : person["age"])
print(sorted_people_age)

sorted_people_name = sorted(people, key = lambda  person : person["name"], reverse=True)
print(sorted_people_name)

# 8 - ENUMER

tasks = ["Write report", "Attend meeting", "Review code", "Submit timesheet"]
'''
for index in range(len(tasks)):
    task = tasks[index]
    print(f"{index + 1}. {task}")
'''

print(list(enumerate(tasks)))

for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")

# 9 - ZIP

names = ["Alice", "Bob", "Charlie", "David", "Tim"]
ages = [30, 25, 35, 20]
'''
for index in range(min(len(names), len(ages))):
    name = names[index]
    age = ages[index]
    print(f"{name} is {age} years old")
'''
combined = list(zip(names, ages))
print(combined)
for name, age in combined:
    print(f"{name} is {age} years old")

# 10 - open
'''
file = open("test.txt", "w")
file.write("Hello world")
file.close()
'''

with open("test.txt", "w") as file:
    file.write("Hello world")