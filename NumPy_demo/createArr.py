import numpy as np
from sklearn.utils.fixes import np_version

# to check version
print(np_version)

arr = np.array([1, 2, 3, 4, 5])
print(arr)

print(type(arr))

# use tuple to create a NumPy array

arr2 = np.array((6,7,8,9,10))
print(arr2)

# create 0-D array with value 42
arr0D = np.array(42)
print(arr0D)

# create 1-D (unidimensional) array
arr1D = np.array([1,2,3,4,5])
print(arr1D)

# create 2-D array containing two arrays
arr2D = np.array([[1,2,3],[4,5, 6]])
print(arr2D)

# create 3-D array - array that contains 2D arrayes (matrices) - to represent 3rd order tensor
arr3D = np.array([[[1,2,3],[4,5, 6]], [[1,2,3], [4,5,6]]])
print(arr3D)

# check number of dimensions
print(arr.ndim)
print(arr0D.ndim)
print(arr1D.ndim)
print(arr2D.ndim)
print(arr3D.ndim)

# to create and array with specified number of dimensions
myArr = np.array([1,2,3,4], ndmin=5)
print(myArr)
print('number of dimensions: ', myArr.ndim)
# innermost dimension (5th dim) has 4 elements
# 4th dim has 1 element - vector
# 3rd dim has 1 element that is matrix with the vector
# 2nd dim has 1 element that is 3D array
# 1st dim has 1 element that is 4D array