### Date conversion program ###

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
            break
        except ValueError:
            pass

            
    month, day, year = int(month), int(day), int(year)
    print(f"{year}-{month:02}-{day:02}")

def check_format(date):
    if date in months:
        month, day, year = date.split(" ")
        day = day.strip(",")
        month = months.index(month)
        return day, month, year
    else:
        month, day, year = date.split("/")
        return day, month, year
    

main()