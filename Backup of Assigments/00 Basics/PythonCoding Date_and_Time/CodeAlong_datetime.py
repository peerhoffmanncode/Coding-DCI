import time
import datetime

# basic methods
print(datetime.datetime.today())
print(datetime.date.today())

var = "1981-06-11"
print(datetime.date.fromisoformat(var))

# create a datetime object
date1 = datetime.datetime(2022, 1, 26)
print(date1)

# strp to work with the input variable!
var = "June, 1, 1981"
obj = datetime.datetime.strptime(var, "%B, %d, %Y")
print(obj)

# strf to work with the object methods
output1 = obj.strftime("%Y-%m-%d %H:%M:%S")
output2 = obj.strftime("%Y %H")
print(output1, output2)

output3_Y = obj.year
output3_M = obj.month
output3_D = obj.day
output3_h = obj.hour
output3_m = obj.minute
output3_s = obj.second
output3_ms = obj.microsecond
print(
    output3_Y,
    output3_M,
    output3_D,
    output3_h,
    output3_m,
    output3_s,
    output3_ms,
    output3_s,
    output3_ms,
)


time_1 = datetime.datetime(day=11, month=6, year=1981)
time_2 = datetime.datetime(day=15, month=9, year=2022)
print(f"your are {time_2 - time_1} old, you old fart!")
print(
    "increase datetime obj by:",
    time_2 + datetime.timedelta(hours=5, minutes=30, seconds=30),
)

# convert to unix timestamp
unix_timestamp = datetime.datetime.timestamp(time_1)
normmaldate = datetime.datetime.fromtimestamp(unix_timestamp)
print(f"Unix Timestap                : {unix_timestamp}")
print(f"Back to Normal Date: Timestap: {normmaldate}")