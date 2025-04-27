### Date conversion program from US format to International ###

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input("Date: ")
        try:
            day, month, year = check_format(date)
            if day in list(range(1, 32)):
                break
        except ValueError:
            pass

            
    month, day, year = int(month), int(day), int(year)
    print(f"{year:04}-{month:02}-{day:02}")

def check_format(date):
    try:
        month, day, year = date.split(" ")
        day = day.strip(",")
        month = (months.index(month) + 1)
        return day, month, year
    except:
        month, day, year = date.split("/")
        return day, month, year
    

main()