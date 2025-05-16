from datetime import date, timedelta
import sys



def main():
    birthday = get_date("Date of Birthday: ")
    today = date.today()
    delta = today - birthday

    print(delta)


def get_date(s):
    try:
        d = date.fromisoformat(input(s))
    except ValueError:
        sys.exit("Invalid date")
    return d
    

def convert_to_min(days):
    return days
    


if __name__ == "__main__":
    main()