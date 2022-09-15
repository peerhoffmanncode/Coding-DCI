from datetime import datetime, date, timedelta

thisdate = datetime.now()

print(type(thisdate))

year = datetime.now().year
month = datetime.now().month
day = datetime.now().day
today = date(year, month, day)

### Task 1 ###
print("Task 1 started")
print()
print(f"today is: {today}, 15 days ago it was {today + timedelta(days=-15)}")

### Task 2 ###
print("Task 2 started")
print()
print(f"today is: {today}, in 7 days it will be {today + timedelta(days=7)}")

### Task 3 ###

print("Task 3 started")
print()
for i in range(1, 13):
    da_date = date(year=2022, month=i, day=25)
    print(
        f"Hello Friedrich, your rent of 300 € is due on {da_date.strftime('%A the %dth of %B, %Y')}"
    )
