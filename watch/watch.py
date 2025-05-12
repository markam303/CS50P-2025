"""Input embedded youtube iframe and output shareable youtube link"""

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search("<iframe[^>]*src")


...


if __name__ == "__main__":
    main()