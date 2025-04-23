### Check if input is valid license plate for Massachusetts ###


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    check_2_first(plate)
    check_last(plate)
        


main()