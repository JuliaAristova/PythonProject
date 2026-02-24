import  numpy
from scipy import stats


speed = [ 99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

#Mean - average value
avgSpeed = numpy.mean(speed);
print(f"Average speed: {avgSpeed}")

#Median - value in the middle after you have sorted all the values
speed.sort()
print(speed)

medianSpeed = numpy.median(speed)
print(f"Median speed: {medianSpeed}")

#Mode - value that appears the most number of times
#The mode() method returns a ModeResult object that contains the mode number (86),
# and count (how many times the mode number appeared (3)).

modeSpeed = stats.mode(speed)
print(f"Mode speed: {modeSpeed}")