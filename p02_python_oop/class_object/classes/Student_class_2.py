class Student:


#properties - control over object creating

    def __init__(self, name, house):
        self.name = name
        self.house = house          #will call setter method

    def __str__(self):
        return f"{self.name} from {self.house}"

    #getters
    @property
    def name(self):
        return self._name

    @property
    def house(self ):
        return self._house

    #setters

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name;

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin" ]:
            raise ValueError("Invalid house")
        self._house = house

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

def main():
   student = get_student()
   # student.house = "Number 4, Privet Drive" -- wil gige ValueError
   student._house = "Number 4, Privet Drive"  # will change = by convention _field - do not change in the code - honor system
   print(student)



if __name__=='__main__':
   main()
