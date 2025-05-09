""""Validate IP adress (user's input)"""

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    
    match = re.search(r"^(.)\.(.)\.(.)\.(.)$", ip)
    if match:
        if match.groups(1) in [0-256]:
            return True
        if match.groups(2) in [0-256]:
            return True
        if match.groups(3) in [0-256]:
            return True
        if match.groups(4) in [0-256]:
            return True
    else:
        return False


if __name__ == "__main__":
    main()