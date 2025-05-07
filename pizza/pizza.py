# Pizza Py - provide *.csv file as CLA

import sys

from tabulate import tabulate


def main():
    # Check for number and type of CLA
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    
    # Print file as grid
    try:
        with open(sys.argv[1]) as file:
            print(tabulate(file, headers="firstrow" , tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not")
        
        
if __name__ == "__main__":
    main()