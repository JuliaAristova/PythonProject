n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

largest = n1
if n2 > largest: largest = n2
if n3 > largest: largest = n3
print(largest)

largest = max(n1, n2, n3)
print("largest number is", largest)