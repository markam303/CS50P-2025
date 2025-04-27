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

date = input("Date: ")
while True:
    try:
        month, day, year = date.split("/")
        month, day, year = int(month), int(day), int(year)
        break
    except ValueError:
        try:
            month, day, year = date.split(" ")
            day = day.strip(",")
            month == months.index(month)
            break
        except ValueError:
            pass
        

print(f"{year}-{month:02}-{day:02}")