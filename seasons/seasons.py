from datetime import date, timedelta
import sys
import re


def main():
    birthday = input("Date of Birthday: ")
    birthday = date.fromisoformat(birthday)
    today = date.today()
    delta = today - birthday
    delta2 = delta.minute
    print(delta)
    print(delta2)
 

...


if __name__ == "__main__":
    main()