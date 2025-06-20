# Pizza Py - provide *.csv file as CLA

import sys

import csv

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
            reader = csv.reader(file)  
            table = tabulate(reader, headers="firstrow" , tablefmt="grid")
            print(table)
            
    except FileNotFoundError:
        sys.exit("File not")
        
        
if __name__ == "__main__":
    main()