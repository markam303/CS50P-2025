"""
Counts the number of times the word 'um' appears in a string,
possibly surrounded by spaces or punctuation.
"""

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum[.,!?]*\b"
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)
    


...


if __name__ == "__main__":
    main()