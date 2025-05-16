from datetime import date, timedelta
import sys



def main():
    birthday = get_date("Date of Birthday: ")
    today = date.today()
    delta = today - birthday
    delta = delta.total_seconds()
    print(convert_to_min(delta))


def get_date(s):
    try:
        d = date.fromisoformat(input(s))
    except ValueError:
        sys.exit("Invalid date")
    return d
    

def convert_to_min(seconds):
    return (seconds / 60)
    
    


if __name__ == "__main__":
    main()