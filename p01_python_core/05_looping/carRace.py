'''
start - to start the car
stop - to stop the car
quit - to exit
'''
print("Car race")
answer = ''
started = False

while True:
    answer = input("Enter a command: ").lower()
    if answer == 'start':
        if started:
            print("Car is already started")
        else:
            print('Car started... Ready to go!')
            started = True
    elif answer == 'stop':
        if not started:
            print('Car is already stopped')
        else:
            started = False
            print("Car is stopped")
    elif answer == 'help':
        print('''
start - to start a car
stop - to stop a car
quit - to quit the game''')
    elif answer == 'quit':
        break
    else:
        print('I do not understand')

