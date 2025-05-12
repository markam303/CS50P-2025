import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"""
        ^\s*                # Optional leading ws
        (1[0-2]|0?[0-9])    # first hour group with possible leading 0
        (?::([0-5][0-9]))?  # non-capturing group of minutes group (captured minutes itself)
        \s*(AM|PM)          # AM PM with leading ws
        \s*to\s*            # to with leading and trailing ws
        (1[0-2]|0?[0-9])    # second hour group with possible leading 0
        (?::([0-5][0-9]))?  # non-capturing group of minutes group (captured minutes itself) as above
        \s*(AM|PM)          # AM PM with leading ws
        \s*$                # trailing ws
        """
    match = re.match(pattern, s, re.X)
    if not match:
        raise ValueError

    start_hr, start_min, start_period, end_hr, end_min, end_period = match.groups()
    
    if not (1 <= int(start_hr) <= 12) or not (1 <= int(end_hr) <= 12):
        raise ValueError
    
    try:
        start_min = get_min(start_min)
        end_min = get_min(end_min)

    except ValueError:
        raise ValueError
    
    start_24h = convert_hrs(start_hr, start_period)
    end_24h = convert_hrs(end_hr, end_period)
    
    return f"{start_24h:02}:{start_min:02} to {end_24h:02}:{end_min:02}"    
    
        
def convert_hrs(hr, period):
    hr = int(hr)
    if period == "AM":
        return hr if hr != 12 else 0
    else:
        return hr + 12 if hr != 12 else 12   
    
            
def get_min(m):
    if m is None:
        return 0
    if not 0 <= int(m) <= 59:
        raise ValueError
    return int(m)      


if __name__ == "__main__":
    main()