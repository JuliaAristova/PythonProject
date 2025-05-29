'''
validate user input
1. username is not more than 12 characters
2. username must not contain spaces
3. username must not contain digits
'''

response = input("Enter username: ")

if len(response) > 12:
    print("Your username cannot be more that 12 characters")

elif(response.find(" ") != -1):
    print("Your username cannot contain spaces")
elif(not response.isalpha()):
    print("Your username cannot contain digits")
else:
    print(f"Welcome {response}")