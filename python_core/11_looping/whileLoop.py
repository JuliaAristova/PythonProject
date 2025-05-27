# while loop - executes some code WHILE some condition remains true

i = 1
while i <= 5:
    print('*' * i)
    i +=1
print("Done!")

name = input("Enter your name: ")
while  name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")  # strategy to escape, otherwise - infinite loop
else:
    print(f"Hello, {name}")

food = input("Enter a food you like (q - to quit): ")
while not food == 'q':
    print(f"You like {food}")
    food = input("Enter another food you like (q - to quit): ")
print("Bye")

num = int(input("Enter a number beween 1 and 10: "))
while num < 1 or num > 10:
    print(f"Number is not valid.")
    num = int(input("Enter a number beween 1 and 10: "))
print(f"You number is {num}")

