import datetime
import os
import random

random.seed()

def equalchoice(line_to_write_to_file: str):
    now = str(datetime.datetime.now())
    
    if os.path.exists('choice.txt') == False:
        report = open('choice.txt','w')
        report.write(line_to_write_to_file + now)
        report.close()
    else:
        report = open('choice.txt','a')
        report.write("\n" + line_to_write_to_file + now)
        report.close()

movies = {
    1: "1.mp4",
    2: "2.mp4",
    3: "3.mp4",
    4: "4.mp4",
    5: "5.mp4",
    6: "6.mp4",
    7: "7.mp4",
    8: "8.mp4",
    9: "9.mp4",
    10: "10.mp4",
    11: "11.mp4",
    12: "12.mp4",
    13: "13.mp4",
    14: "14.mp4",
    15: "15.mp4",
    16: "16.mp4",
    17: "17.mp4",
}


x   = random.randint(1,17)
if x < 17:
    os.system(movies[x])
    equalchoice("NOT 17th movie was randomly chosen. ")
else:
    os.system(movies[x])
    equalchoice("17th movie was randomly chosen.     ")