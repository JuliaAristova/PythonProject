# Scatter plot = a diagram where each value in the data set is represented by a dot
import matplotlib.pyplot as plt
import numpy.random

# age of each car
#x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

# speed of each car
#y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#plt.scatter(x, y)
#plt.show()

# From diagram - 2 fastest car are both 2 years old, the slowest car is 12 years old

# create and array with a normal data distribution with 1000 values, mean = 5.0, standard deviation = 1.0
a = numpy.random.normal(5.0, 1.0, 1000)

# create and array with a normal data distribution with 1000 values, mean = 10.0, standard deviation = 2.0
b = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(a, b)
plt.show()

# from diagram - dots are concentrated around the value 5 on the xaxis, and 10 on the y-axis