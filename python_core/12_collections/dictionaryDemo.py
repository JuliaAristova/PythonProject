# dictionary - a collection of { key : value } pairs
#              ordered and changeable; no duplicates

capitals = {'USA' : 'Washington, D.C',
            'India' : 'New Delhi',
            'China' : 'Beijing',
            'Russia' : 'Moscow' }

'''
print(dir(capitals))
print(help(capitals))
'''
print(capitals.get('USA'))
print(capitals.get('India'))

if (capitals.get('Japan')):
    print("This capital exist")
else:
    print("This capital does not exist")

capitals.update({'Germany' : 'Berlin'})
print(capitals)

capitals.update({'USA' : 'Washington, DC'})
print(capitals)

capitals.pop('China')
print(capitals)

capitals.popitem()  # removes last pair
print(capitals)

# to get all keys
keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

#  to get all values
values = capitals.values()
print(values)
for value in values:
    print(value)

# to get all items
items = capitals.items()
print(items)
for item in items:
    print(item)

for key, value in capitals.items():
    print(key, '-', value)

capitals.clear()
print(capitals)