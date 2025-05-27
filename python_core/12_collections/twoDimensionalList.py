# 0ne-dimensional lists

fruits = ['apple', 'orange', 'banana', 'coconut']
vegetables = ['celery', 'carrots', 'potatoes']
meats = ['chicken', 'fish', 'turkey']


# Two-dimensional list
groceries = [fruits, vegetables, meats]


print(fruits)
print(fruits[0])

print(groceries)
print(groceries[0])
print(groceries[0][0])
print(groceries[1][0])
print(groceries[2][0])

closet = [['pants', 'shirt', 'dress'],
          ['high-hills', 'snickers'],
          ['hat', 'sunglasses', 'purse']]
print(closet)

for collection in groceries:
    for food in collection:
        print(food, end = ' ')
    print()
