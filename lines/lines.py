# Count number of lines in *.py file, provided as CLI argument

import sys


def main():
    # Check for number and type of arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    
    
    


if __name__ == "__main__":
    main()