import datetime as dt

# Calculates the age between the given date and the current date in years
def age(date):
    return ((dt.datetime.now()-date).days)//365

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
print(f"You are {age(dt.datetime(year,month,day))} years old!")
