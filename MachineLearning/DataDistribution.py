import numpy
import matplotlib.pyplot as plt

# create an array containing 250 random floats between 0 and 5
arr = numpy.random.uniform(0.0, 5.0, 250)
print(arr)

# create a histogram - 1 bar - how many values between 0 and 1;
# 2 bar - how many values between 1 and 2, etc
# 5 0 number of bars

plt.hist(arr, 5)
plt.show()

