'''
Membership operators - used to test whether a value or variable
    is found in a sequence (string, list, tuple, set,or dictionary)
1. IN
2. NOT IN
'''

word = 'APPLE'
letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a '{letter}' in the word")
else:
    print(f"{letter} is not found")

students = {"Spongebob", "Parrick", "Sandy"}

student = input("Enter the name of a student: ")

if student not in students:
    print(f"{student} is not found")
else:
    print(f"{student} is a student")


grades = { "Sandy" : "A",
           "Squidward" : "B",
           "Spongebob" : "C",
           "Patrick" : "D" }
student = input("Enter the name of a student: ")

if student in students:
    print(f"{student}'s grade is {grades[student]}.")
else:
    print(f"{student} is not found")


# check email is valid
email = "Spongebob2025@gmail.com"

if '@' in email and '.' in email:
    print("Valid email")
else:
    print("Invalid email")