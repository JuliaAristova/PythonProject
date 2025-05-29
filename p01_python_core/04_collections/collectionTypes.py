'''
collection - single 'variable' used to store multiple values
List - [ ] ordered and changeable; accepted duplicates
Set - { } unordered, immutable; no duplicates; can add/remove values
Tuple = ( ) ordered and unchangeable; accepts duplicates; faster
'''

fruit = 'apple'
print(fruit)

fruit_list = ['apple', 'kiwi', 'banana', 'apple', 'orange']
print(fruit_list)

fruit_set = {'apple', 'kiwi', 'banana', 'orange'}
print(fruit_set)

fruit_tuple = ('apple', 'kiwi', 'banana', 'apple')
print(fruit_tuple)

print(fruit_list[0])
print(fruit_list[::-1])
print(fruit_tuple[2])

print("******")
for fruit in fruit_set:
    print(fruit)
'''
print("*** Methods ***")
print(dir(fruit_list))
print(dir(fruit_set))
print(dir(fruit_tuple))

print(help(fruit_tuple))
'''
print("******")
print(len(fruit_list))
print('apple' in fruit_list)
print('grapes' in fruit_list)