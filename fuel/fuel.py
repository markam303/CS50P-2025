### Change fraction as input to percentage as output ###


def main():
    fraction = get_int("Fraction: ")
    numerator, denominator = fraction.slice("/")



def get_int(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            pass


main()