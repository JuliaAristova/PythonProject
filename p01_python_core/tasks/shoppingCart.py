item = input("What do you want to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many woyl you like?: "))
total = quantity * price

print(f"The total price for {quantity} {item}/s is ${total}")