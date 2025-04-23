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
    check_last(plate)

# Check for lenght, if between 2-6 characters        
def check_lenght():
    ...

# Check if first 2 chars are letters
def check_2_first_letters(plate):
    ...

# 



main()