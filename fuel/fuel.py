### Change fraction as input to percentage as output ###


def main():
    percentage = get_fraction("Fraction: ")
    percentage = round(percentage)
    if 0 <= percentage <= 1:
        print("E")
    elif 99 <= percentage <= 100:
        print("F")
    else:
        print(f"{percentage}%")
    

def get_fraction(text):
    while True:
        try:
            numerator, denominator = input(text).split("/")
            numerator = int(numerator)
            denominator = int(denominator)
            if numerator <= denominator:   
                return ((numerator * 100) / denominator)
        except (ValueError, ZeroDivisionError):
            pass

    
    
main()