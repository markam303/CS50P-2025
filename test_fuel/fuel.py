### Change fraction as input to percentage as output ###


def main():
    while True:
        try:
            text = input("Fraction: ")
            percentage = convert(text)
            print(gauge(percentage))
            return 0
        except (ValueError, ZeroDivisionError, TypeError):
            pass

    
    
def gauge(percentage):
    # Print empty or full rather than %
    if 0 <= percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return f"{percentage}%"
    

# Function to get fractions from users; designed to handle potential Errors
def convert(text):
    try:
        numerator, denominator = text.split("/")
        numerator = int(numerator)
        denominator = int(denominator)
    except ValueError:
        raise ValueError

    if denominator == 0:
        raise ZeroDivisionError
    else:
        percentage = round(((numerator * 100) / denominator))
        
    return percentage



if __name__ == "__main__":    
    main()