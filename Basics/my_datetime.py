import datetime

today = datetime.date.today()
print("FULL DATE ", today)
print("CURRENT YEAR ", today.year)
print("CURRENT MONTH ", today.month)
print("CURRENT DAY ", today.day)

date_and_time = datetime.datetime.now()
print(date_and_time)

# Create an specific date
specific_date = datetime.date(2026, 12, 13)
print(specific_date)
