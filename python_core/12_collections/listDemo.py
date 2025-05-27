#List - [ ] ordered and changeable; accepted duplicates

fruits = ['apple', 'kiwi', 'banana', 'orange', 'pineapple']

print("Iterate - for loop")
for fruit in fruits:
    print(fruit)

print("Print using index")
print(fruits[1])

print("Reassigning")
fruits[0] = 'lemon'
print(fruits)

print("Adding element")
fruits.append('apple')
print(fruits)

print("Removing element")
#fruits.remove('coconut') --> ValueError: list.remove(x): x not in list
fruits.remove('apple')
print(fruits)

print("Inserting element")
fruits.insert(0,'apple')
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

print(fruits.index('apple'))

fruits.append('banana')
print(fruits.count('banana'))
print(fruits.count('melon'))
print(fruits.clear())