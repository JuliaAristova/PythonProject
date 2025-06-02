import random

x, y, z = 1, 5.0, 1j

print(x, type(x))  #int - positive, negative, unlimited length
print(y, type(y))  #float - positive, negative, 1 or more decimal
print(z, type(z))

#float with power of 10
y2 = -87.7e100

#complex - written with j - imaginary
a = 3 + 5j
b = 5j
c = -5j
print(a, type(a))
print(b, type(b))
print(c, type(c))

#converting (you cannot convert complex number)

x = float(y)
y = int(y)

print(x, type(x))
print(y, type(y))

s = '8'
print(s, type(s))
s = int(s)
print(s, type(s))

d = 5.8
e = 5.1
d2 = int(d)    #5
e2 = int(e)    #5
print(d, d2)
print(e, e2)

print(random.randrange(1,10))

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = round(x+y)
print(f"{z:,}")

print(f"{(x + y):.0f}")

d = round(x/y, 2)
print(d)
print(f"{(x/y):.2f}")