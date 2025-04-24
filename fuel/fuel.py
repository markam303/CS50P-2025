### Change fraction as input to percentage as output ###


def main():
    numerator, denominator = get_fraction("Fraction: ")
    percentage = (numerator * 100) / denominator
    print(f"{percentage}%")
    

def get_fraction(text):
    while True:
        try:
            numerator, denominator = input(text).split("/")
            numerator = int(numerator)
            denominator = int(denominator)  
        except (numerator, denominator == 0):
            pass        
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    return numerator, denominator
    
    
main()