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
        break
    except ValueError:
        month, day, year = date.split(" ")
        day = day.strip(",")
        break
        
month, day, year = int(month), int(day), int(year)
print(f"{year}-{month:02}-{day:02}")