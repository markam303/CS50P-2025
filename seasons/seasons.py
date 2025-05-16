from datetime import date
import sys
import re


def main():
    birthday = input("Date of Birthday: ")
    birthday = date.fromisoformat(birthday)
    today = date.today()
        

...


if __name__ == "__main__":
    main()