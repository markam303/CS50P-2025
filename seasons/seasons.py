from datetime import date
import sys
import inflect



def main():
    try:
        birthday = get_date("Date of Birthday: ")
    except ValueError:
        sys.exit("Invalid date")
        
    today = date.today()
    delta = today - birthday
    
    delta = delta.total_seconds()
    minutes = convert_to_min(delta)
    print(minutes)
    speller = minute_speller(minutes)
    print(speller)
    
    
def minute_speller(minutes):    
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="").capitalize()
    plural_minutes = p.plural_noun("minute", count=minutes)
    return f"{words} {plural_minutes}"


def get_date(s):
    return date.fromisoformat(input(s))

    

def convert_to_min(seconds):
    return int(seconds / 60)
    

if __name__ == "__main__":
    main()