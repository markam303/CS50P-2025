# Count number of lines in *.py file, provided as CLI argument

import sys


def main():
    # Check for number and type of arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        pass
    

def check_extension(str):
    try:
        a, b = str.split(".")
    except ValueError:
        return False
    if b == "py":
        return True
    else:
        return False

if __name__ == "__main__":
    main()