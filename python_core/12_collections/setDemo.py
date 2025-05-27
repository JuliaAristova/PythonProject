# Set - { } unordered, immutable; no duplicates; can add/remove values
# good to work with constants

fruits = {'apple', 'kiwi', 'banana', 'orange', 'pineapple'}
'''
print(dir(fruits))
print(help(fruits))
'''

for fruit in fruits:
    print(fruit)                # printed in random order

print(len(fruits))
print('apple' in fruits)
print('coconut' in fruits)

#print(fruits[0]) -->  'set' object is not subscriptable

fruits.add('coconut')
print(fruits)
fruits.add('coconut')
print(fruits)

fruits.remove('orange')
print(fruits)

fruits.pop()        # removes first element, random
print(fruits)

fruits.clear()
print(fruits)