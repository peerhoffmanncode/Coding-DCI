import datetime
import time
import os

os.system("clear")

birthday = 0
while (0 < birthday < 31) is False:
    birthday =   int(input("please enter the day of the event (DD)   : "))

birthmonth_list = ["01", "02", "03", "04", "05", "06", "07","08", "09", "1", "2", "3", "4", "5", "6", "7","8", "9", "10", "11", "12"]
birthmonth = ""
while (birthmonth in birthmonth_list) is False:
    birthmonth = input("please enter the month of the event (MM) : ")

birthyear= "0"
while (2022 <= int(birthyear)) is False:
    birthyear =  input("please enter the year of the event (YYYY): ")

event_day = str(birthday) + " " + str(birthmonth) + " " + birthyear
event_day = datetime.datetime.strptime(event_day, "%d %m %Y")
current_day = datetime.datetime.today()

delta_date = event_day - current_day

result_y = delta_date.days // 365
result_w = (delta_date.days - (result_y * 365)) // 7
result_d = (delta_date.days - (result_y * 365)) - (result_w * 7)
print(f"Your event is in {delta_date.days} days, that means your have {result_y} year(s), {result_w} week(s), {result_d} day(s) until.")
