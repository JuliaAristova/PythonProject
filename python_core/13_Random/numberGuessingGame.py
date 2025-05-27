# Number guessing game
import random

lowNum = 1
highNum = 100
attempt = 0
isRunning = True

number = random.randint(lowNum, highNum)
#print(number)
print("***** Python Numer Guessing Game *****")

print(f"Select a number between {lowNum} and {highNum} ")

while isRunning:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        attempt += 1

        if guess < lowNum or guess > highNum:
            print("The number is out of range.")
            print(f"Please select a number between {lowNum} and {highNum}")

        elif guess < number:
            print("Too low! Try again")
        elif guess > number:
            print("Too high! Try again")
        else:
            print(f"Correct! The answere was {guess}.")
            print(f"You guess the number from {attempt} attempt.")
            isRunning = False
    else:
        print("Invalid guess.")
        print(f"Select a number between {lowNum} and {highNum} ")


