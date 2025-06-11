import csv

with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

print("*********************")

with open("students.csv") as file:
    for line in file:
        name, house  = line.rstrip().split(",")
        print(f"{name} is in {house}")

print("*********************")
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} in {house}")

for student in sorted(students):
        print(student)


print("*********************")
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):              # sorted calls for get_name
        print(f"{student['name']} is in {student['house']}")

print("*********************")

for student in sorted(students, key=lambda student: student["house"], reverse=True):
        print(f"{student['name']} is in {student['house']}")

print("*********************")

students = []

with open("students2.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['home']}")

print("*********************")

students = []

with open("students3.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)
       # students.append({"name": row["name"], "home": row["home"], "house": row["house"]})

for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}, in house {student['house']}")