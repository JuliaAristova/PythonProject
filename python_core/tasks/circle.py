# c = 2 pi r
import math

radius = float(input("Enter the radius of a circle: "))
c = round(2 * math.pi * radius, 2)

print(f"Circumference = {c}")

area = round(math.pi * pow(radius, 2), 2)
print(f"Area = {area} ")