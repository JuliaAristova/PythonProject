# Create an array with values concentrated aroung a given value
# normal data distribution  Gaussian data distribution
# bell cirve
import numpy
import matplotlib.pyplot as plt

# create an array with 100 000 values
# mean = 5; standard deviation = 1
arr = numpy.random.normal(5.0, 1.0, 100000)
#print(arr)

# create a histogram with 100 bars
plt.hist(arr, 100)
plt.show()