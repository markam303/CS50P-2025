# Pizza Py - provide *.csv file as CLA

import sys

from tabulate import tabulate


def main():
    # Check for number and type of CLA
    if not len(sys.argv[1]) == 2:
        sys.exit("Provide only one *.csv file")
    elif not sys.argv[1].endswith(".csv"):
        sys.excit("Wrong file format")
    
    try:
        ...
    except FileNotFoundError:
        sys.exit("File not")
if __name__ == "__main__":
    main()