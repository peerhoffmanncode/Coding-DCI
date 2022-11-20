import datetime
import time
import os
import calendar

os.system("clear")

birthday = 0
while (0 < birthday < 31) is False:
    birthday =   int(input("please enter the day of your birth (DD)   : "))

birthmonth_list = ["01", "02", "03", "04", "05", "06", "07","08", "09", "1", "2", "3", "4", "5", "6", "7","8", "9", "10", "11", "12"]
birthmonth = ""
while (birthmonth in birthmonth_list) is False:
    birthmonth = input("please enter the month of your birth (MM) : ")

birthyear= "0"
while (1900 < int(birthyear) < 2022) is False:
    birthyear =  input("please enter the year of your birth (YYYY): ")

your_birthday = str(birthday) + " " + str(birthmonth) + " " + birthyear
your_birthday = datetime.datetime.strptime(your_birthday, "%d %m %Y")
current_day = datetime.datetime.today()

delta_date = current_day - your_birthday

result_y = delta_date.days // 365
result_w = (delta_date.days - (result_y * 365)) // 7
result_d = (delta_date.days - (result_y * 365)) - (result_w * 7)
print(f"You are {delta_date.days} days old, that means your were born {result_y} year(s), {result_w} week(s), {result_d} day(s) ago.")
