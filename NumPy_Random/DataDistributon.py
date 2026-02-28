# Data distribution - is a list of all possible values, and how ofen each value occurs
# random distributions is a set of random numbers that follow a certain probability density function
# Probability Density Function - describes a continous probability (probability of all values in an array)
# choice() - allows to specify the probability for each value
# probability s set by a number 0 and 1
# 0 - value will never occur
# 1 - value will always occur
from  numpy import  random

# generate 100 values from the provided numbers and their corresponding probabilty (sum of p = 1)
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)

y = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(y)
