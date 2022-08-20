'''This program should take user input() and based on the choice
the user made change the course of the story.'''

import os
from sys import platform
from  colorama import Fore, Back, Style

def read_database(filename):
    '''Open database and load the data in file'''
    database_dict = {}
    with open(filename) as f:
        
        for line in f:
            print(line)
            if line == "\n":
                pass
            elif line[:1] == "#" or line[:1] == "'":
                pass
            else:
                (key, val) = line.split(";")
                database_dict[key] = val
    return database_dict

def show_text_line(msg, fcolor, bcolor):
    '''little function to print text with color
       might be replaced in order for a GUI'''
    print(fcolor + bcolor + msg + Style.RESET_ALL)
    
def clearscreen():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')

def main(filename):
    '''Main game loop function'''
    
    # create DB Dict key:str :value:str
    database_dict = {} 
    # load game database
    database_dict = read_database(filename)
    
    #set level of question deepness to ground!
    game_deepness_level = 0                             
    # no chose was taken yet!       
    choice = ""
    
    # while loop begin
    while True:
        # clear screen for every question
        clearscreen()
        
         # Welcomeline
        show_text_line("Welcome to this text based adventure", Fore.LIGHTRED_EX, Back.RESET)
        show_text_line("------------------------------------", Fore.RESET, Back.RESET)
        show_text_line("", Fore.RESET, Back.RESET)
     
        found_entries = False       # every loop the exit flag is set to FALSE!
        game_deepness_level += 1    # every loop the deepness is increased by 1
        
        max_options = 0
        for game_stage, question in database_dict.items():      # read data from game dictionary
            if len(game_stage) == game_deepness_level:          # is db game_stage == deepness_level
                if choice == "":                                # first ever round?
                    # is item a question?
                    if "_" in game_stage:                       
                        show_text_line(f"" + question.strip("\n"), Fore.LIGHTGREEN_EX, Back.RESET)
                        show_text_line("", Fore.RESET, Back.RESET)
                        found_entries = True                        
                    # is item an option
                    else:                                       
                        show_text_line(f"choose [{game_stage}] : " + question.strip("\n"), Fore.RESET, Back.RESET)
                        found_entries = True
                        max_options += 1
                elif choice == game_stage[:game_deepness_level-1]:  # proper round!
                    # is item a question?
                    if "_" in game_stage:
                        show_text_line(f"" + question.strip("\n"), Fore.LIGHTGREEN_EX, Back.RESET)
                        show_text_line("", Fore.RESET, Back.RESET)
                        found_entries = True
                    # is item an option
                    else:
                        show_text_line(f"choose [{(game_stage[game_deepness_level-1:game_deepness_level]).upper()}] : " + question.strip("\n"), Fore.RESET, Back.RESET)
                        found_entries = True
                        max_options += 1
                        
            # options are not valid yet?
            elif len(game_stage) > game_deepness_level:
                break
         
        if found_entries is False:                              # couldn't we find any new question!
            show_text_line("end of the game...", Fore.RESET, Back.RESET) 
            show_text_line("", Fore.RESET, Back.RESET)
            break
        
        if max_options < 1:
            show_text_line("you reached the end of the game...", Fore.RESET, Back.RESET)
            show_text_line("", Fore.RESET, Back.RESET)
            break
        else:
            show_text_line("", Fore.RESET, Back.RESET)
            next_step = input("what do you want to do ? [Select a [Number],  [R]eturn, [Q]uit]: ").strip()
            if next_step[:1].isnumeric() and (int(next_step[:1]) <= max_options):
                choice = choice + next_step[:1]
            elif next_step[:1].lower() == "r" and len(choice) >= 1:
                choice = choice[:len(choice)-1]
                game_deepness_level -= 2
            elif next_step[:1].lower() == "q":
                show_text_line("you quited the game ...", Fore.RESET, Back.RESET)
                show_text_line("", Fore.RESET, Back.RESET)
                break
            else:
                game_deepness_level -= 1



###########################################################
### Start the game loop
###########################################################

if __name__ == '__main__':
    FILENAME = "game.db"
    
    main(FILENAME)