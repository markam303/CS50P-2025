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


while True:
    date = input("Date: ")
    try:
        month, day, year = date.split("/")
        break
    except ValueError:
        month, day, year = date.split(" ")
        if month in months:
            day = day.strip(",")
            month == months.index(month)
            break
        else:
            pass

        
month, day, year = int(month), int(day), int(year)
print(f"{year}-{month:02}-{day:02}")