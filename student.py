class Student:
    ...
    



def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = Student()
    
    


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