#List
# - [ ] ordered and changeable (mutable)
# - accepted duplicates
# - can contain different data types

# CREATING lists

fruits = ['apple', 'kiwi', 'banana', 'orange', 'pineapple']
vegetables = list()             # create an empty list
print(vegetables)

list_zeroes = [0]*5
print(list_zeroes)

list_true = [True]*5
print(list_true)

list_combined = list_zeroes + list_true
print("Combined list: ", list_combined)

# ACCESSING ELEMENTS using INDEX

print(">>>Print using index")
print(fruits[1])            # kiwi
print(fruits[-2])           # 0range
# slicing
print("List: " ,fruits)
print(fruits[1:3])          # ['kiwi', 'banana'] - last index in excluded
print(fruits[:3])
print(fruits[2:])
print(fruits[::2])          # step 2; default 1
print(fruits[::-1])         # reverse

# vegetables[0]             IndexError: list index out of range

# ITERATING through the LIST

print(">>>Iterate - for loop")
for fruit in fruits:
    print(fruit)

# REASSIGNING ELEMENTS

print(">>>Reassigning")
fruits[0] = 'lemon'
print(fruits)

# ADDING & INSERTING ELEMENTS

print(">>>Adding element")
fruits.append('apple')          # adds to the end of the list
print(fruits)
vegetables.append('tomato')
vegetables.append('cucumber')


print(">>>Inserting element")
fruits.insert(0,'apple')
print(fruits)
vegetables.insert(2, 'radish')
print(vegetables)

# REMOVING ELEMENTS
print(">>>Removing element")


#fruits.remove('coconut') --> ValueError: list.remove(x): x not in list
print(fruits)

fruits.remove('apple')              # removes first occurrence
#fruits.remove("melon")             ValueError: list.remove(x): x not in list
print(fruits)

fruits.append("last apple")
print("'Last apple' added", fruits)

f = fruits.pop()        # removes last element and return it
print(f)

# LISTs METHODs

print(">>>Check length of list")
print("Length of the list: ", len(fruits))

print(">>>Check element is in the list")
if 'radish' in vegetables:
    print("It is in the list")
else:
    print("It is not in the list")

fruits.sort()
print("Sorted: " , fruits)

nums = [0, 9, -3, 5, -2, 4, 1]
nums_sorted = sorted(nums)
print(nums_sorted)

fruits.reverse()
print("Reversed: ", fruits)

print("Index: ", fruits.index('apple'))

fruits.append('banana')
print("Count elements: ", fruits.count('banana'))
print(fruits.count('melon'))
print("Cleared list: ", fruits.clear())

list_orig = [1, 2, 3, 4, 5]
list_copy = list_orig           # both lists referres to the same memory location
print(list_orig)
print(list_copy)
# both lists will be modified
list_copy.append(6)
print(list_orig)
print(list_copy)

# to make a real copy
print("Copy a list")
l_copy = list_orig.copy()
l_copy2 = list(list_orig)
l_copy3 = list_orig[:]

l_copy.append(7)
l_copy2.append(8)
l_copy3.append(9)

print(list_orig)        # not affected
print(l_copy)
print(l_copy2)
print(l_copy3)