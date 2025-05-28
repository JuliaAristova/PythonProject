# Tuple = ( ) ordered and unchangeable; accepts duplicates; faster than list

fruits = ('apple', 'kiwi', 'banana', 'orange', 'pineapple', 'apple')

'''
print(dir(fruits))
print(help(fruits))
'''

for fruit in fruits:
    print(fruit)

print(len(fruits))
print('apple' in fruits)
print('coconut' in fruits)


print(fruits[0])

print(fruits.index('apple'))
# print(fruits.index('coconut'))  -ValueError: tuple.index(x): x not in tuple

print(fruits.count('apple'))
print(fruits.count('coconut'))

'''
does not have these methods 
fruits.add('coconut')
fruits.append('coconut')
fruits.remove('coconut')
'''

