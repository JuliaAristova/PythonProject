# permutation refers to an arragment of elements
# [ 3, 2, 1 ] is a permutation of [ 1, 2, 3 ]
import  numpy as np
from numpy import random

# shuffle() - changing arragments of elements in-place. It makes changes to the original array

arr = np.array([1, 2, 3, 4, 5])
print(f"Original array: {arr}")

random.shuffle(arr)
print(f"Shuffled array: {arr}")

# permutation() - rearranges, leaves the original array unchanged
permArr = random.permutation(arr)
print(f"Permutated array: {permArr}")

print(arr)