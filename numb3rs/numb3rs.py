""""Validate IP adress (user's input)"""

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    return re.search(r"[0-255]\.[0-255]\.[0-255].[0-255]", ip)



if __name__ == "__main__":
    main()