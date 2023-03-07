### Task 6 ###

import os  # import os
import time  # import time


def progressbar(width: int) -> None:
    """function to create a progressbar
    argument width must be a positive integer
    width: 1 - 100"""
    if width < 1:
        width = 1

    for i in range(0, 101):
        # create - line
        line = "-" * ((width) - int(i * (width / 100)))
        # create # line
        bar = "#" * int(i * (width / 100))

        # build progress bar string
        fullbar = f"|{bar}{line}| {i:3}%"
        # print progress bar
        print(fullbar + "\r", end="")
        # sleep for 0,1 seconds
        time.sleep(0.1)
    # print("done!" + " " * (width+2))                               # print done


# clear terminal
os.system("clear")
print("Yeah, some funky download ...")

progressbar(22)
