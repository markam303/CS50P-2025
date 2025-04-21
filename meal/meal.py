### Input time in 24h time ###

def main():
    time = input("What time is it? ").strip()
    
    convert(time)
    
    if time > 7 and time < 8:
        print("breakfast time")
    elif time > 12 and time < 13:
        print("lunch time")
    elif time > 18 and time < 19:
        print("dinner time")
    else:
        print("")
    
def convert(time):
    hour, min = time.split(":")
    hour = float(hour)
    min = float(min)
    min = min / 60
    

if __name__ == "__main__":
    main()