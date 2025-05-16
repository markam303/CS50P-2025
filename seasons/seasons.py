from datetime import date
import sys
import inflect



def main():
    birthday = get_date("Date of Birthday: ")
    today = date.today()
    delta = today - birthday
    delta = delta.total_seconds()
    minutes = int(convert_to_min(delta))
    print("Minutes:", minutes)
    p = inflect.engine()
    print(p.number_to_words(minutes), p.plural("minute", count=minutes))


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