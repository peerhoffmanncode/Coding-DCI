import calendar

print(calendar.month(1981, 6))
for i in range(1981, 2080):
    if calendar.isleap(i):
        print(i, calendar.isleap(i))
