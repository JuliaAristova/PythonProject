# Standard Deviation - a number that describes how spread out the values are
# low - most of the numbers are close to the mean (avg)
# high - values are spread out over a wider range

import numpy

speed = [ 86, 87, 88, 86, 87, 85, 86]

stDev1 = numpy.std(speed)
print (f"Average: {numpy.mean(speed)}")
print (stDev1)

speed2 = [ 32, 111, 138, 28, 59, 77, 97]
stDev2 = numpy.std(speed2)
print (f"Average: {numpy.mean(speed2)}")
print (stDev2)
