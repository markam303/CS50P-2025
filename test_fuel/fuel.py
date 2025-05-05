### Change fraction as input to percentage as output ###


def main():
    percentage = convert("Fraction: ")
    percentage = round(percentage)
    print(gauge(percentage))
    
    
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
    while True:
        try:
            numerator, denominator = input(text).split("/")
            numerator = int(numerator)
            denominator = int(denominator)
            if numerator <= denominator: 
                percentage = round(((numerator * 100) / denominator))  
                return percentage
        except (ValueError, ZeroDivisionError):
            pass

    
main()