### Check if input is valid license plate for Massachusetts ###


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    chech_length(plate)
    check_2_first_letters(plate)
    check_last(plate)
        


main()