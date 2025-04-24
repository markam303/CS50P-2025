### Change fraction as input to percentage as output ###


def main():
    percentage = get_fraction("Fraction: ")
    
    print(f"{percentage}%")
    

def get_fraction(text):
    while True:
        try:
            numerator, denominator = input(text).split("/")
            numerator = int(numerator)
            denominator = int(denominator)
            if numerator < denominator:   
                return ((numerator * 100) / denominator)
        except (ValueError, ZeroDivisionError):
            pass

    
    
main()