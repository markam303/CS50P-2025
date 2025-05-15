class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    print(student)

 
# Return class
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)



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