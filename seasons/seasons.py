from datetime import date
import sys
import inflect



def main():
    birthday = get_date("Date of Birthday: ")
    today = date.today()
    delta = today - birthday
    delta = delta.total_seconds()
    print("Seconds:", delta)
    print("Minutes:", convert_to_min(delta))
    count = int(convert_to_min(delta))


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