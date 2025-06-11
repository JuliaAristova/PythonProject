'''

names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"Hello, {name}")
'''
name = input("What's your name? ")

'''
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
'''
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
'''
with open("names.txt", 'r') as file:
    for line in file:
        print("Hello,", line.rstrip())


names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names):          # sorted(names, reverse=True)
    print(f"Hello, {name}")
'''
with open("names.txt") as file:
    for line in sorted(file):
        print(f"Hello,", line.strip())