is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovelhy day")
print("Enjoy your day")

'''
if name is less that 3 characters long
    name must be at least 3 characters
otherwise if it's more than 50 characters long
    name can be a maximum of 50 characters
otherwise
    name looks good
'''
name = input("Enter you name: ")
if(len(name) < 3):
    print("Name must be at least 3 characters")
elif(len(name) > 50):
  print("Name must be maximum 50 characters")
else:
    print("name looks good")