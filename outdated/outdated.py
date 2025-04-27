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
            month, day, year = int(month), int(day), int(year)
            if check_date(day, month):
                break
        except ValueError:
            pass

            

    print(f"{year:04}-{month:02}-{day:02}")

def check_format(date):
    try:
        month, day, year = date.split(" ")
        if not int(day):
            return 1
        day = day.strip(",")
        month = (months.index(month) + 1)
        return day, month, year
    except:
        month, day, year = date.split("/")
        return day, month, year

def check_date(day, month):
    return 1 <= month <= 12 and 1 <= day <= 31
        
    

main()