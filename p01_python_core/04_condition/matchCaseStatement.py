'''
Match-case statement (switch) - al alternative to using many 'elif' statements
    Execute some code of a value matches a 'case'
    Benefits: cleaner and syntax is more readble
'''

def day_of_week(day):
    if day == 1:
        return "It is Sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It is Tuesday"
    elif day == 4:
        return "It is Wednesday"
    elif day == 5:
        return "It is Thursday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is Saturday"
    else:
        return "Not a valid day"

print(day_of_week(4))

def days_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:                                 # == else
            return "Not a valid day"

print(days_of_week(7))

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return "It is a weekend"
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "It is not a weekend"
        case _:
            return "It is not a valid day"

print(is_weekend("Saturday"))
print(is_weekend("Sunday"))
print(is_weekend("Monday"))
print(is_weekend("Wednesday"))
print(is_weekend("Pizza"))
