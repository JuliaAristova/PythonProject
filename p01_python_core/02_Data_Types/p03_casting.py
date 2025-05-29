#Typecasting - the process of converting a variable from one data type to another
# str(), int(), float(), bool()
# complex number cannot be cast to another type
# type() to check

# int() construct int from int, float, string


cmplx = complex(5)
# cmplx = int(cmplx)  - not allowed

a = int(5)
b = int(5.9)   #removes all decimal
c = int("7")

print(a, b, c)

# float() construct float from int, float, string
d = float(5)
e = float(5.9)   #removes decimal
f = float("7.4")

print(d, e, f)

# str() construct string from int, float, string
h = str (5)
i = str(5.9)   #removes decimal
g = str("7.4")

print(h, i, g)

#bool() con
name = "Anna"
print(bool(name))
print(bool(""))         # to check if input is entered




