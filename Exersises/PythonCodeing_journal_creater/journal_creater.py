''' Little program to create a journal '''

import os
import time
import datetime
import colorama as c
import art      as art


# init colorama
c.init()

def write_to_file(filename: str, line_to_write: str, wa_mode):
    ''' function to write stuff to a file '''
    with open(filename, mode=wa_mode, encoding='utf-8') as my_log_file:
        my_log_file.write(line_to_write.strip()+"\n")


def read_to_file(filename: str) -> str:
    ''' function to read stuff of a file '''   
    with open(filename, mode="r", encoding='utf-8') as my_log_file:
        return my_log_file.read()


def input_data_from_user(question: str) -> str:
    ''' function to get input by user. Sanatizing will happen.'''
    input_line = input(question)
    return input_line


def printout_journal(full_journal):
    ''' print out the given journal variable '''
    print(c.Fore.RED)
    print(c.Back.WHITE)
    print("")
    print("-" * 80)
    print("--- " + (" " * 22) + "Current state of the journal" + (" " * 22) + " ---")
    print("-" * 80)
    print(c.Fore.GREEN)
    print(c.Back.RESET)
    print(full_journal)
    print(c.Style.RESET_ALL)


### Main PGM

# get the current date
CURRENT_DATE = str(datetime.datetime.now().strftime(("%m/%d/%Y, %H:%M:%S")))

# wipe screen
os.system("clear")

# get current path + filename
my_pwd = os.getcwd()
filename = my_pwd + "/log.txt"

# show the current state of the journal
printout_journal(read_to_file(filename))

user_msg = ""
while True:
    # get user input
    user_msg = input_data_from_user("Please enter new user Data (quit/end to exit) >>> : ")
    # check the input

    quit_list = ["quit", "end", "exit"]              # create a list of words to look for to exit the loop!           
    if user_msg.lower().strip() in quit_list:
        break                                       # drop out of the while loop (user wants to exit!)  
    elif user_msg != "":
        ## create the line that should be stored
        line_to_write = CURRENT_DATE + " - " + user_msg

        if os.getcwd().replace("\\","/").upper() in line_to_write.upper():
            pass
        else:
            write_to_file(filename, line_to_write, wa_mode = "a")

        # show the current state of the journal again
        printout_journal(read_to_file(filename))
    else:
        # not a valid input!
        print("please enter an information to store to the journal.")
