#string in single or double quotation marks
print("Python")
print('Java')
course = 'Python for Beginners'

print(course[0])
print(course[-2])
print(course[0:2])
print(course[3:])
print(course[:3])

another = course[:]
print(another)

print('''
Hi, John,
    Here is oor first email to you.
    Welcome to the team!
Support Team.
''')
#quotes inside quotes
print("It's all right")
print('It is "Python 3"')
print('It\'s all right')

#multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

b = '''Lorem ipsum dolor sit amet,  \
consectetur adipiscing elit,\tc
sed do eiusmod tempor incididunt\n
ut labore et dolore magna aliqua.'''
print(b)

name = 'Jennifer'
print(name[1:-1]) #ennife

#formatted strings
first_name = 'John'
last_name = 'Smith'

#concatination
message = first_name + ' [' + last_name + '] is a coder'

#Strings are array
#Python does not have char datatype - single char is a string with length 1

a = "Hello, World!"
print(a[1])

#looping
for x in "banana":
    print(x)

#len() - function returns length
print(len(a))

#to check string contains a certain text/character
txt = "The best things in life are free!"
print("free" in txt)
print("spring" in txt)

if "free" in txt:
    print("Yes, 'free' is present")

if "expensive" not in txt:
    print("No, 'expensive' is not present")

print("spring" not in txt)

course = 'Python for Beginners'

print(len(course))

print(course.upper())
print(course.lower())
print(course.title())

#course is not changed
print(course)

print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))
print(course)
print('Python' in  course)

print()