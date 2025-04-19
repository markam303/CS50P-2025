def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars_stripped_to_numbers = d.strip("$")
    return float(dollars_stripped_to_numbers)


def percent_to_float(p):
    percents_stripped_to_numbers = p.strip("%")
    return float(percents_stripped_to_numbers) / 100


main()