import numpy

# 1. Find the mean
# 2. For each value find the difference from he mean
# 3. For each difference find the square value

speed = [32,111,138,28,59,77,97]
varSpeed = numpy.var(speed)
print(f"Variance: {varSpeed}")

stDev = numpy.sqrt(varSpeed)
print(f"Standard deviation: {stDev}")

standDev = numpy.std(speed)
print(f"Standard deviation: {standDev}")