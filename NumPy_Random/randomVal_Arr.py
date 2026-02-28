# random means something that cannot be predicted logically
# pseudo random - random numbers generated through a generation algorithms
# truly random - we need to get the random data from some outside source (keystrokes, mouse movement, data on networks, etc.)

# we use pseudo random

from numpy import random

# generate random integer
intRandom = random.randint(100)
print(intRandom)

# generate random float
floatRandom = random.rand()
print(floatRandom)

# generate 1-D array containing 5 random integers from 0 to 100
intArr = random.randint(100, size=(5))
print(intArr)

floatArr = random.rand(5)
print(floatArr)

# generate 2-D array with 3 rows containing 5 integers from 0 to 100
intArr2 = random.randint(100, size=(3, 5))
print(intArr2)

floatArr2 = random.rand(3, 5)
print(floatArr2)

# generate random number from an array
x = random.choice([3, 5, 7, 9])
print(x)

# generate array of values
y = random.choice([3,5,7,9], size=(3, 5))
print(y)
