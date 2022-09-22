import datetime
import calendar
import os

def date_difference(date_to_come: datetime.datetime, current_date_to: datetime.datetime) -> dict:
    
    delta_date = date_to_come - current_date_to     # calculate difference between current and previous
    all_days = delta_date.days                      # get days
    
    if all_days > 0:
        c_year = current_date_to.year                # current year -> 2022
        c_month = current_date_to.month              # current month -> 9 
    else:
        all_days = abs(all_days)                     # get days
        c_year = date_to_come.year                   # current year -> 2022
        c_month = date_to_come.month                 # current month -> 9 
    
    substract_year = 365                            # normal year = 365 if not a leap year

    result_y = result_m = result_w = result_d = 0   # counter var
    leap_year = 0
    while True:
        if all_days >= 365:
            # count years !
            if calendar.isleap(c_year):
                substract_year = 366
                leap_year += 1
            else:
                substract_year = 365
                
            all_days = all_days - substract_year
            result_y += 1
            c_year += 1
        
        if 28 <= all_days < 365:
            # count remaining month !
            if c_month ==1 or c_month ==3 or c_month ==5 or c_month ==7 or c_month ==8 or c_month ==10 or c_month ==12:
                # month of 31 days
                substract_month = 31
            elif c_month ==2:
                # check leap for feb!
                if calendar.isleap(c_year):
                    substract_month = 29
                else:
                    substract_month = 28
            else:
                # month of 30 days
                substract_month = 30
    
            all_days = all_days - substract_month
            result_m += 1
            c_month += 1
            if c_month > 12: c_month = 1
            
        if 7 <= all_days < 28:
            # count remaining weeks
            all_days = all_days - 7
            result_w += 1
        
        if all_days < 7:
            # count remaining days
            result_d = all_days -1
            break
    
    return {"year": result_y,
                   "month": result_m,
                   "week": result_w,
                   "day": result_d,      
            }
    
#### MAIN CODE ####

os.system("clear")      # clear screen

# input your DAY
input_day = 0
while (0 < input_day < 31) is False:
    input_day =   int(input("please enter the day of the event (DD)   : "))

# input your MONTH
month_list = ["1", "2", "3", "4", "5", "6", "7","8", "9", "01", "02", "03", "04", "05", "06", "07","08", "09", "10", "11", "12"]
input_month =""
while (input_month in month_list) is False:
    input_month =input("please enter the month of the event (MM) : ")

# input your YEAR
input_year =  input("please enter the year of the event (YYYY): ")

# create the date objects
other_date = datetime.datetime.strptime((str(input_day) + " " + str(input_month) + " " + input_year), "%d %m %Y")
current_date = datetime.datetime.today()

# call the mighty date_difference function
output_dict = date_difference(other_date, current_date)

# print some awesome results ...
print(f"Your event is in {output_dict['year']} year(s), {output_dict['month']} month(s), {output_dict['week']} week(s), {output_dict['day']} day(s) until.")
