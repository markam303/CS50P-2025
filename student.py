class Student:
    def __init__(self, name, house):  # patronus
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        # self.patronus = patronus
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter
    def house(self):
        return self.house
    
    # Setter
    def house(self, house):
        self.house = house

# Function inside class
"""     def charm(self):
        match self.patronus:
            case "Stag":
                return ":horse:"
            case "Otter":
                return ":otter"
            case "Jack Russell terrier":
                return ":dog:"
            case _:
                return "emoji_wand_default"       """  


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    print(student)
    print("Expecto Patronum!")
    print(student.charm())
    
 
# Return class
def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)



# Return class
""" def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student    """ 


# Return dictionary
""" def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house} """


# Return list
""" def get_student():
    name = input("Name ")
    house = input("House ")
    return [name, house] """


# Return tuple
""" def get_student():
    name = input("Name ")
    house = input("House ")
    return name, house """


# Return values separately
""" def get_name():
    return input("Name: ")

def get_house():
    return input("House ") """


if __name__ == "__main__":
    main()