kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
#pass the whole result to the print() function as one string - str()
#print("Hypotenuse length is " + (leg_a**2 + leg_b**2) ** .5) - TypeError: can only concatenate str (not "float") to str
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))