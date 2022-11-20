# CAPS LOCK DAY is over!

## Task
# October 22nd is CAPS LOCK DAY. Apart from that day, every sentence should be lowercase, so write a function to normalize a sentence.

# Create a function that takes a string. If the string is all uppercase characters, convert it to lowercase and add an exclamation mark at the end. Each string is a normalized sentence and should start with an uppercase character.

## Input/Output

# normalize("CAPS LOCK DAY IS OVER")                -->   "Caps lock day is over!"  
# normalize("Today is not caps lock day.")          -->   "Today is not caps lock day."  
# normalize("Let us stay calm, no need to panic.")  -->   "Let us stay calm, no need to panic." 

import datetime

def normalize(User_String):
    """ Function to normalize a user string
        If the date is 22 october, do nothing!
        return normalized User_String on any other day
        """
    # get current date
    today = datetime.datetime.today().strftime("%d-%m")

    if today == "22-10":
        # exit if 22-oct
        return User_String
    
    if User_String == User_String.upper():
        # add ! if UPPER !
            User_String = User_String + "!"
    return User_String.lower().capitalize()


print(normalize("CAPS LOCK DAY IS OVER"))
print(normalize("Today is not caps lock day."))
print(normalize("Let us stay calm, no need to panic."))