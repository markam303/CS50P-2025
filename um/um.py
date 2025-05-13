import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\s?um(?:,\?\.!)?\s?"
    matches = re.findall(pattern, s, re.IGNORECASE)
    count = 0
    for match in matches:
        count += 1
    return count
    


...


if __name__ == "__main__":
    main()