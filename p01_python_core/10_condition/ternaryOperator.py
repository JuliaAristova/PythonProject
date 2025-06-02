'''
Conditional expression = A one-line shortcut for the if-else statement (ternaty operator
Print or assign one of two vwlues based on a condition
X if condition is True, else Y
'''

num = 5
a = 6
b = 7
age = 13
temperature = 20
user_role = "guest"

print ("Positive" if num >0 else "Negative")
print("Even" if a%2 == 0 else "Odd")

max_value = a if a > b else b
min_value = a if a < b else b

print("Adult" if age > 18 else "child")
print("Hot" if temperature > 20 else "Cold")
access_level = "admin" if user_role == "admin" else "Limited access"