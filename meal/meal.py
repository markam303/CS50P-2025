### Input time in 24h time and 12h time ###

def main():
    time = input("What time is it? ").strip()
    
    try:
        time, am_pm = time.split(" ")
        
        time = convert(time)
        
        if am_pm == "a.m." or am_pm == "A.M.":
            if time >= 7.00 and time <= 8.00:
                print("breakfast time")
            elif time >= 12.00:
                print("lunch time")
            else:
                return 0
        elif am_pm == "p.m." or am_pm == "P.M.":
            if time >= 6.00 and time <= 7.00:
                print("dinner time")
    except ValueError:
        time = convert(time)
    
        if time >= 7.00 and time <= 8.00:
            print("breakfast time")
        elif time >= 12.00 and time <= 13.00:
            print("lunch time")
        elif time >= 18.00 and time <= 19.00:
            print("dinner time")
        else:
            return 0
        

    
def convert(time):
    hour, min = time.split(":")
    hour = float(hour)
    min = float(min)
    min = min / 60
    return float(hour + min)
    

if __name__ == "__main__":
    main()