import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.search(r"\s?um(?:,\?!)?\s?", s, re.IGNORECASE)
    count = 0
    for match in matches:
        count += 1
    


...


if __name__ == "__main__":
    main()