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
    
    # Create temp list of dicts to store information from csv file
    list = []
    
    # Open file and copy it to list if it exists
    try:
        with open(sys.argv[1]) as file_input:
            reader = csv.DictReader(file_input)
            for row in reader:
                list.append(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    
    # Writing to file after sorting First, Last, House
    with open(sys.argv[2], "w", newline="") as file_output:
        writer = csv.DictWriter(file_output, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for line in list:
            last, first = line["name"].split(",")
            house = line["house"]
            writer.writerow({"first": first, "last": last, "house": house})
        return 0
        
    
if __name__ == "__main__":
    main()