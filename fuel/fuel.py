### Change fraction as input to percentage as output ###


def main():
    numerator, denominator = get_fraction("Fraction: ")
    percentage = (numerator * 100) / denominator
    print(f"{percentage}%")
    

def get_fraction(text):
    while True:
        try:
            numerator, denominator = int(input(text).slice("/"))
            
            if numerator > denominator:
                pass
            elif denominator == 0:
                pass
            else:
                break                
        except ValueError:
            pass
        else:
            break
    return numerator, denominator
    
    
main()