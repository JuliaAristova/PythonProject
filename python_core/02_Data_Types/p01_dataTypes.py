'''
Text type           str
Numeric types       int, float, complex
Sequence types      list, tuple, range
Mapping type        dict
Set types           set, frozenset
Boolean type        bool
Binary types        bytes, bytearray, memoryview
None type           NoneType
'''

#Text type = str
a = "Python"
b = 'Java'
print('x =', a, type(a))
print('x =', b, type(b))
b2 = str("Hello World")

print("-------------------")
#Numeric type: int, float, complex
c = 5
c2 = int(10)
d = 5.0
d2 = float(20.5)
e = 1j
e2 = complex(1j)

print('x =', c, type(c))
print('x =', d, type(d))
print('x =', e, type(e))

print("-------------------")

#Sequence type: list, tuple, range
f =  ["apple", "banana", "cherry"]
g = ("apple", "banana", "cherry")
h = range(6)
f2 =  list(("apple", "banana", "cherry"))
g2 = (tuple(("apple", "banana", "cherry")))

print('x =', f, type(f))
print('x =', g, type(g))
print('x =', h, type(h))

print("-------------------")

#Mapping type: dict
i = {"name" : "John", "age" : 36}
i2 = dict(name = "John", age = 36)
print('x =', i, type(i))

print("-------------------")

#Set types: set, frozenset
j = {"apple", "banana", "cherry"}
k = frozenset({"apple", "banana", "cherry"})
j2 = set(("apple", "banana", "cherry"))
k2 = frozenset(("apple", "banana", "cherry"))

print('x =', j, type(j))
print('x =', k, type(k))

print("-------------------")

#Boolean: bool
l  = True
l2 = bool(5)

print('x =', l, type(l))

print("-------------------")

#Binary types: bytes, bytearray, memoryview
m = b"Hello"
n = bytearray(5)
o = memoryview( bytes(5))
m2 = bytes(5)
n2 = bytearray(5)
o2 = memoryview(bytes(5))

print('x =', m, type(m))
print('x =', n, type(n))
print('x =', o, type(o))

#Nonetype: NoneType
p = None
print('x =', p, type(p))

#Python always chooses the more economical form of the number's presentation
print(0.0000000000000000000001)
print(6.62607E-34)

print(True > False)  #1 > 0
print(True < False)

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
# 5 *(12+100)/26))//2

print((2 % -4), (2 % 4), (2 ** 3 ** 2))