'''
module - a file containing code you want to include in your program
    use 'import' to include a module (built-in or your own)
    useful to break up a large program reusable separate files
'''

# to see available modules
#print(help("modules"))

# to get more details about particular module
#print(help("math"))

# to include module
import math
import datetime as dt
from math import  e

import example

print(math.pi)
print(e)
x = dt.datetime.now()
print(x)

# var e declared here and we  have e imported from math - it will be overridden
a, b, c, d, e = 1, 2, 3, 4, 5
print(e ** a)
print(e ** b)
print(e ** c)
print(e ** d)
print(e ** e)

print("________")
print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)

# using methods from module - example
result = example.pi
result = example.area(3)
print(result)

print(example.cube(5))
print(example.square(45))
print(example.circumference(3.4))

