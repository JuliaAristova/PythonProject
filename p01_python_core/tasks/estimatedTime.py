'''
Scenario
Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.
For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
Don'test worry about any imperfections in your code - it's okay if it accepts an invalid time - the most important thing is that the code produce valid results for valid input data.
Test your code carefully. Hint: using the % operator may be the key to success.

Test Data
Sample input:  12  17  59
Expected output: 13:16

Sample input:  23  58  642
Expected output: 10:40

Sample input: 0  1   2939
Expected output: 1:0
'''

# Write your code here.

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

end = mins + dura
e_hour = hour + end//60
if e_hour > 24:
    e_hour = e_hour%24
e_min = end%60
print(e_hour, ':', e_min, sep='')

print (2//4)

