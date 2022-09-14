import os       # import os
import time     # import time

os.system("clear")  # clear terminal

print("Yeah, some funky download ...")  # print the heck out of things!
n=4
for i in range(0, 101, n):                      # start loop
    line = ("-" * ((100//n) - (i//n)))          # create ----- line 100 - "#" times
    bar = "#" * (i//n)                          # create ##### line "#" * i times
    
    fullbar = "|" +bar+line  + "| " + str(i) + "%"      # build progress bar
    print(fullbar + "\r", end="")                       # print progress bar
    time.sleep(0.1)                                     # sleep for 0,1 seconds

print("done!" + " " * 50)                               # print done