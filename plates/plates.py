### Check if input is valid license plate for Massachusetts ###


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Check plates are valid
def is_valid(plate):
    if check_2_first_letters(plate): 
        return False 
    if check_lenght(plate):
        return False
    if check_numbers(plate):
        return False
    if check_marks(plate):
        return False
    return True

# Check if first 2 chars are letters
def check_2_first_letters(plate):
    if plate[0:2].isalpha():
        return 0
    else:
        return 1

# Check for lenght, if between 2-6 characters included        
def check_lenght(plate):
    if 2 <= len(plate) <= 6:
        return 0
    else:
        return 2

# Check numbers, last character must be numbers and first number cannot be 0
def check_numbers(plate):
    for char in plate:
        if char.isdigit() and char[-1].isalpha():
            if char == "0":
                return 3
            else:
                continue
    if plate[-1].isalpha():
        return 4
    else:
        return 0
       

# Check for periods, spaces, punctuations - not allowed
def check_marks(plate):
    if plate.isalnum():
        return 0
    else:
        return 5


main()