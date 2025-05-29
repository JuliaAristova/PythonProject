price = 1000000

credit = input("Enter credit (good or bad): ")

if(credit == 'good'):
    downpayment = price*0.1
else:
    downpayment = price*0.2
print(f"Downpayment = ${downpayment}")