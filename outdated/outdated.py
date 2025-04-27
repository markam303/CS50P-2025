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
month, day, year = date.split("/")
month, day, year = int(month), int(day), int(year)
print(f"{year}-{month:02}-{day:02}")