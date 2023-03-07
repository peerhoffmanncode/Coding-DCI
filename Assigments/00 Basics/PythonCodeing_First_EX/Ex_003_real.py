# length() in Python
## Overview:
# The len() method is used to get the length of a string. The length is equal to the number of Unicode code units in a string.

## Task
# Write a program that detects if a string has an even/odd number of characters and prints "even" or "odd" accordingly.


## Input --> Output
your_phrase = ""
while your_phrase != "end":
    print("")
    your_phrase = input("say something nice [end = quit/exit]: ")
    print("")
    if len(your_phrase) % 2 == 0:
        print("[" + your_phrase + "] is an even string")
    else:
        print("[" + your_phrase + "] is an odd string")
        
    print (f"{len(your_phrase): 10}")