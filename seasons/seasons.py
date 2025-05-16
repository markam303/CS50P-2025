from datetime import date
import sys
import inflect



def main():
    birthday = get_date("Date of Birthday: ")
    today = date.today()
    
    delta = today - birthday
    delta = delta.total_seconds()
    
    minutes = int(convert_to_min(delta))   
    speller = minute_speller(minutes)
    print(speller)
    
    
def minute_speller(minutes):    
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="").capitalize()
    plural_minutes = p.plural_noun("minute", count=minutes)
    return f"{words} {plural_minutes}"


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