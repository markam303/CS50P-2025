""""Validate IP adress (user's input)"""

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"[0-256]\.[0-256]\.[0-256]\.[0-256]", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()