from car import Car

car1 = Car('Mustang', 2024, 'red', False)
car2 = Car("Corvette", 2025, 'blue', True)
car3 = Car("Charger", 2026, "yellow", True)

car4: Car = Car("Toyota", 2025, "white", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car2.describe()
car3.describe()
car4.describe()

car1.drive()
car1.stop()

car2.drive()
car2.stop()

car3.drive()
car3.stop()

print(car4)
print(car1 + car2)