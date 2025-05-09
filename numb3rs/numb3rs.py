""""Validate IP adress (user's input)"""

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"\d[0-255]\.\d[0-255]\.\d[0-255]\.\d[0-255]", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()