from datetime import datetime
import calendar

current_datetime = datetime.now()

### Task 1 ###
print("Task 1 started")
print()
print(current_datetime.year)

### Task 2 ###
some_date = datetime(2021, 7, 14)
print("Taks 2 started")
print()
print(some_date.weekday())

### Task 3 ###
year = 2021
print("Taks 3 started")
print()
print(f"{year} is a leap year = {calendar.isleap(year)}")

### Task 4 ###
date_as_string = "Feb 14 2021 8:30AM"
obj = datetime.strptime(date_as_string, "%b %d %Y %H:%MAM")
print("Taks 4 started")
print()
print(obj)
