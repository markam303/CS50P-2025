### Input time in 24h time ###

def main():
    time = input("What time is it? ").strip()
    
    time = convert(time)
    
    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")
    else:
        pass
    
def convert(time):
    hour, min = time.split(":")
    hour = float(hour)
    min = float(min)
    min = min / 60
    return float(hour + min)
    

if __name__ == "__main__":
    main()