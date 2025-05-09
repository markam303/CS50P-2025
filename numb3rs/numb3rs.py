""""Validate IP adress (user's input)"""

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Check if IP address is in correct range
    match = re.fullmatch(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", ip)
    if not match:
        return False
    
    groups = match.groups()
    
    for group in groups:
        if len(group) > 1 and group.startswith("0"):
            return False
        
        if not 0 <= int(group) <= 255:
            return False
    
    return True


if __name__ == "__main__":
    main()