def main():
    '''
    name = get_name()
    house = get_house()
    print(f"{name} is from {house}")

    student =  get_student_l()
    if student[0] == "Padma":
        student[1] = "Revenclaw"
    print(f"{student[0]} is from {student[1]}")
    '''

    student = get_student()

    if student["name"] == "Padma":
        student["house"] = "Revenclaw"

    print(f"{student['name']} is from {student['house']}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")


def get_student_l():

    name = input("Name: ")
    house = input("House: ")
   # return name, house              # returns  tuple (unmutable), you can add (name, house)
    return [name, house]            # returns a list


def get_student():
    '''
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student
    '''
    name = input("Name: ")
    house= input("House: ")
    return {"name": name, "house": house}

if __name__ == '__main__':
    main()