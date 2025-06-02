# input() - a function that prompts the user to enter data
# returns the entered data as a string

if(input("Enter your name: ")):
    print("entered")
else:
    print("Empty")

anything = input()
print("Hmm, anything is", anything)


anything2 = input("Enter a number: ")

#the result of the input() function is a string.
something = int(anything2) ** 2.0
print(anything2, "to the power of 2 is", something)

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5     #* 0.5 - equal to square root
print("Hypotenuse length is", hypo)

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

