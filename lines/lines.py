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
         
    try:
        with open(sys.argv[1]) as file:
            count = 0
            for line in file:
                stripped = line.strip()
                if not stripped:
                    continue
                if stripped.startswith("#"):
                    continue
                count += 1
        print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")
    
        
if __name__ == "__main__":
    main()