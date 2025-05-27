
weight = int(input("Enter you weight: "))
unit = (input("Enter units pounds (L) or kilograms (K): ")).upper()

if unit == 'L':
    print(f"Your weight is {weight/2.205} kg")
elif unit == 'K':
    print(f"Your weight is {round(weight*2.205)} lbs")
else:
    print("Invalid weight unit")
