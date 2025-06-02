'''
Variable - container for a value (string, integer, float, boolean)
A variable is created the moment you first assign a value to it
var name starts with letter or _, can contain numbers
'''
x = 1               #x is int
y = 'Anna'          #string - single or double quotes
z = 10.99           #float
can_swim = True

print(x, y, z, can_swim)


print(f"Hello {y}")
print(f"x value is {x}")
print(f"z is float - {z}")
print(f"I can swim - {can_swim}")

#changing type of variable
#get type
print(type(x))
x = "Peter"
print(x)
print(type(x))

#cast
y = float(5)
print(y)
print(type (y))

#assigning multiple variables on one line
d, e, f = 'Orange', 'Banana', 'Apple'
print(d, e, f)
print(d, e, f, sep="*", end="")
print()
print(d+ ' ' + e + ' ' + f)

#one value to multiple variables
a1 = a2 = a3 = "Grape"
print(a1, a2, a3)

#unpacking - assigning values from a collection of values
fruits = ['orange', 'banana', 'apple']
f1, f2, f3 = fruits
print(f1)
print(f2)
print(f3)

i = 5
s = 'John'
print(i, s)
#print(i + s) TypeError
print(f"{i} {s}")
print(str(i), s)


a = "Hello"
b = "World"
print("Hello", "World")         # Hello World
print(a + b)                    #HelloWorld