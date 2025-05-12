import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"""
        ^\s*                # Optional leading ws
        (1[0-2]|0?[0-9])    # first hour group with possible leading 0
        (?::([0-5][0-9]))?  # non-capturing group of minutes group (captured minutes itself)
        \s*(AM|PM)        # AM PM with leading ws
        \s*to\s*            # to with leading and trailing ws
        (1[0-2]|0?[0-9])    # second hour group with possible leading 0
        (?::([0-5][0-9]))?  # non-capturing group of minutes group (captured minutes itself) as above
        \s*(AM|PM)        # AM PM with leading ws
        \s*$                # trailing ws
        """
    match = re.search(pattern, s, re.X)
    
            
        
...

if __name__ == "__main__":
    main()