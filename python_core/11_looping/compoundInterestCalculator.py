# Python Compound Interest Calculator
'''
A = P(1 + r/n)**t
A - final amount
P - Initial principal balance
r - interest rate
t - number of time periods elapsed
'''


principle = 0
rate = 0
time = 0

'''
while principle <= 0:
    principle = float(input("Enter a principle amount: "))
    if(principle <= 0):
        print("Principle can't be less than or equal to zero")
        principle = float(input("Enter a principle amount: "))
'''
while True:
    principle = float(input("Enter a principle amount: "))
    if(principle < 0):
        print("Principle can't be less than zero")
    else:
        break


while True:
    rate = float(input("Enter a interest rate: "))
    if(rate < 0):
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter time in years: "))
    if(time < 0):
        print("Time can't be less than zero")
    else:
        break

print(f"Principle = {principle}")
print(f"Interest rate = {rate}")
print(f"Time periods = {time}")

finalAmount = principle * pow( (1 + rate/100), time)

print(f"Final amount after {time} year(s) = ${finalAmount:0.2f}")

