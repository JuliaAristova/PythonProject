
# Format specifier - {:flag} format a value based on what flags are inserted
'''
.(number)f  = round to that many decimal places (fixed pont)
:(number)   = allocate that many spaces
:03         = allocate and zero pad that many spaces
:<          = left justify
:>          = right justify
:^          = center align
:+          = use a plus sugn to indicate positive value
:=          = place sign to leftmost position
:           = insert a space before positive numbers
:,          = comma separator
'''

print(f"The price is ${2+3}")
print(f"The price is ${(2+3):.2f}")

price1 = 3000.12159
price2 = -9870.65
price3 = 1200.34

print(f"price1 is ${price1:.2f}")
print(f"price2 is ${price2:.1f}")
print(f"price2 is ${price2:.2f}")
print(f"price2 is ${price2:.3f}")
print(f"price3 is ${price3:.2f}")
print(f"price3 is ${price3:10}")            # allocated 10 spaces to display the price

print(f"price1 is ${price1:012}")
print(f"price1 is ${price2:012}")
print(f"price3 is ${price3:012}")

print(f"price1 is ${price1:>12}")
print(f"price1 is ${price2:>12}")
print(f"price3 is ${price3:>12}")

print(f"price1 is ${price1:<12}")
print(f"price1 is ${price2:<12}")
print(f"price3 is ${price3:<12}")

print(f"price1 is ${price1:^12}")
print(f"price1 is ${price2:^12}")
print(f"price3 is ${price3:^12}")

print(f"price1 is ${price1:+}")
print(f"price1 is ${price2:+}")
print(f"price3 is ${price3:+}")

print(f"price1 is ${price1: }")
print(f"price1 is ${price2: }")
print(f"price3 is ${price3: }")

print(f"price1 is ${price1:,}")
print(f"price1 is ${price2:,}")
print(f"price3 is ${price3:,}")

#mixing
print(f"price1 is ${price1:+,.2f}")
print(f"price1 is ${price2:+,.2f}")
print(f"price3 is ${price3:+,.2f}")