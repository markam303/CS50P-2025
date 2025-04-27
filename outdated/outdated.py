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
try:
    month, day, year = date.split("/")
except ValueError:
    month, day, year = date.split(" ").strip(",")
month, day, year = int(month), int(day), int(year)
print(f"{year}-{month:02}-{day:02}")