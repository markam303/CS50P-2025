### Check if input is valid license plate for Massachusetts ###


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Check plates are valid
def is_valid(plate):
    check_2_first_letters(plate)
    check_lenght(plate)
    check_numbers(plate)
    check_marks(plate)
    return 0

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
    for i in plate:
        if i.isdigit() and (i - 1).isalpha():
            if i == 0:
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