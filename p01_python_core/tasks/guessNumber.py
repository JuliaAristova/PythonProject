secret_number = 9
guess_count = 0
guess_limit = 3

print("You have 3 attempts to guess the number (0-10)")

while guess_count < guess_limit:
    guess = int(input("Make a guess: "))
    if guess == secret_number:
        print ("You won!")
        break
    guess_count += 1
else :                              #while have else, executed if break is not executed
    print("You failed!")