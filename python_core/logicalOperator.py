"""
AND - True - both conditions are True
OR - True - one of the conditions is True
NOT - inverts the condition (not False, not True)

"""
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligable for loan")

if has_high_income or has_good_credit:
    print("Eligable for loan")

temp = 25
isRaining = False

if temp> 35 or temp <0 or isRaining:
    print("The outdoor event is cancelled")
else:
    print("The event will take place")

