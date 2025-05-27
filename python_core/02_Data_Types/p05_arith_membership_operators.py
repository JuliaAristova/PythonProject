# math - provides number of functions
import math

print(10 + 3)
print(10 - 3)

print(10 * 3)
print(10 ** 3)  # power

print(10 / 3)
print(10 // 3)      # integer division
print(10 % 3)       # remainder

print("ENHANSMENT OPERATOR")
x = 10
x += 3
print(x)
x -= 1
print(x)

print("OPERATORs PRECEDENCE")
'''
parentheses
exponent **
multiplication/division
sum/subtractions 
'''
x = 10 + 3 * 2 ** 2   # 10 + 3 * 4  - ** - higher precedence
print(x)

x = (3 + 2) * 10 - 3
print(x)

print("MEMBERSHIP OPERATORS")
# Memebership oerators
if 'apple' in (('banana', 'apple', 'orange')):
    print('apple is there')

if 'a' in ('apple'):
    print("'a' is in apple")

if 'coconut' not in (('banana', 'apple', 'orange')):
    print('coconut is not there')

#import math
print("Build in math functions")
x = 2.9
print(round(x))
print(round(2.1))

print(abs(-3.14))
print(pow(4, 3))

print(max(9, 1, 34))
print(min(9, 1, 34))

print(round(1.1))
print(math.ceil(1.1))       # 2 - rounds up
print(math.floor(3.7))      # rownds down

print(math.pi)
print(math.e)
print(math.sqrt(9))