# calculate hypotenuse
import math

a = float(input("Enter the length of one side: "))
b = float(input("Enter the length of one other side: "))
c = round( math.sqrt(pow(a,2 ) + pow(b, 2)),2)

print(f"Hypotenuse = {c}")