""""Validate IP adress (user's input)"""

import re
import sys


def main():
    address = input("IPv4 Address: ")
    print(validate(address))


def validate(ip):
    return re.search(r"[0-255]\.[0-255]\.[0-255].[0-255]")


    


if __name__ == "__main__":
    main()