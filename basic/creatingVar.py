#A variable is created the moment you first assign a value to it
x = 1               #x is int
y = 'Anna'          #single or double quotes

x = "Peter"         #x is redeclared, type is changed to str

print(x)
print(y)
print(x)

#cast
y = float(5)
print(y)

#get type
print(type (x))
print(type (y))

#assigning multiple variables on one line
d, e, f = 'Orange', 'Banana', 'Apple'
print(d, e, f)
print(d+ ' ' + e + ' ' + f)

#one value to multiple variables
a1 = a2 = a3 = "Grape"
print(a1, a2, a3)

#unpacking - assigning values from a collection of values
fruits = ['Orange', 'Banana', 'Apple']
f1, f2, f3 = fruits
print(f1)
print(f2)
print(f3)

i = 5
s = 'John'
print(i, s)
#print(i + s) TypeError
print(str(i), s)