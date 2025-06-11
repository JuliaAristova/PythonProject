
class Student:
    ...                                    # ... - placeholder
    def __init__(self, name, house, patronus):       # constructor  (dunder method - double underscore)
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin" ]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} is from {self.house}"

    def charm(self):                # by convention any method inside the class must have at least 1 argument - self
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐕"
            case _:
                return "🪄"


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)         # constructor call, instantiate Student object

def main():
   student = get_student()
   #print(f"{student.name} is from {student.house}")
   print(student)
   print("Expecto Patronum!")
   print(student.charm())

if __name__=='__main__':
   main()

