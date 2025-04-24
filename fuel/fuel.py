### Change fraction as input to percentage as output ###


def main():
    numerator, denominator = get_fraction("Fraction: ")
    

def get_fraction(text):
    while True:
        try:
            numerator, denominator = int(input(text)).slice("/")
            if numerator > denominator:
                pass
            elif denominator == 0:
                pass                
        except ValueError:
            pass
        else:
            break
    return numerator, denominator
    
    
main()