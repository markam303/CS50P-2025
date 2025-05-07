# Scourgify - sorting csv file to easily mail merge
"""Provide one csv file to sort as first argument and new filename as second argument"""

import sys

import csv

def main():
    # Check for number of CLA and its type
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Wrong file format")
    
    list = []
    with open(sys.argv[1]) as file_input:
        reader = csv.DictReader(file_input)
        for row in reader:
            list.append(row)
    
    
    with open(sys.argv[2], "w") as file_output:
        writer = csv.DictWriter(file_output, fieldnames=["first", "last", "house"])
        for _ in list:
            last, first, house = list.strip('"').split(",")
            writer.writeheader()
            writer.writerow({"first": first, "last": last, "house": house})
        
    
if __name__ == "__main__":
    main()