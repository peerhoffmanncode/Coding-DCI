'''This program should take user input() and based on the choice
the user made change the course of the story.'''

import os
import sys
import time
from sys import platform
from colorama import Fore, Back, Style
from art import tprint

def read_database(filename):
    '''Open database and load the data in file'''
    database_dict = {}
    with open(filename) as db_file:

        for line in db_file:
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
    '''check the OS and clear the terminal screen'''
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')

def intro_animation():
    '''startup animation'''
    clearscreen()
    tprint("Amazing text adventure by Peer", "tombstone")
    show_text_line(("-" * 99) + " 20 August 2022 -", Fore.RESET, Back.RESET)
    show_text_line("as if i would need to load the Database", Fore.LIGHTRED_EX, Back.RESET)
    for i in range(6):
        print(".", end="", flush=True)
        time.sleep(0.35)

def quit_the_game():
    show_text_line("bye bye! ...", Fore.RESET, Back.RESET)
    time.sleep(2)
    clearscreen()
    sys.exit()


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
        return_flag = False         # was the RETURN to last question option scripted ?
        game_deepness_level += 1    # every loop the deepness is increased by 1

        max_options = 0
        for game_stage, question in database_dict.items():          # read data from game dictionary
            if len(game_stage) == game_deepness_level:              # is db game_stage == deepness_level
                if choice == "":                                    # first ever round?
                    # is Return scripted?
                    if "r" in game_stage.lower():
                        return_flag = True
                    # is item a question?
                    if "_" in game_stage:
                        show_text_line(question.strip("\n"), Fore.LIGHTGREEN_EX, Back.RESET)
                        show_text_line("", Fore.RESET, Back.RESET)
                        found_entries = True
                    # is item an option
                    else:                                       
                        show_text_line(f"choose [{game_stage}] : " 
                                       + question.strip("\n"), Fore.RESET, Back.RESET)
                        found_entries = True
                        max_options += 1
                elif choice == game_stage[:game_deepness_level-1]:  # proper round!
                    # is Return scripted?
                    
                    if "r" in game_stage.lower():
                        return_flag = True
                        
                    # is item a question?
                    if "_" in game_stage:
                        show_text_line(question.strip("\n"), Fore.LIGHTGREEN_EX, Back.RESET)
                        show_text_line("", Fore.RESET, Back.RESET)
                        found_entries = True
                    # is item an option
                    else:
                        show_text_line(f"choose [{(game_stage[game_deepness_level-1:game_deepness_level]).upper()}] : " 
                                       + question.strip("\n"), Fore.RESET, Back.RESET)
                        found_entries = True
                        max_options += 1

            # options are to advanced yet?
            elif len(game_stage) > game_deepness_level:         # mybe get rid of this check?
                break

        if found_entries is False:                              # can't find any new question! End of game.
            show_text_line("you reached the end of the game...", Fore.RESET, Back.RESET)
            show_text_line("", Fore.RESET, Back.RESET)
            break

        if max_options < 1:                                     # no options to chose from! End of game.
            show_text_line("you reached the end of the game...", Fore.RESET, Back.RESET)
            show_text_line("", Fore.RESET, Back.RESET)
            break
        else:
            show_text_line("", Fore.RESET, Back.RESET)
            next_step = input("what do you want to do ? [Select a [Number], [R]eturn, [Q]uit]: ").strip()

            if next_step[:1].isnumeric() and (int(next_step[:1]) <= max_options):
                if max_options == 1 and return_flag:
                    game_deepness_level -= 1
                else:
                    choice = choice + next_step[:1]
            elif next_step[:1].lower() == "r" and len(choice) >= 1:
                choice = choice[:len(choice)-1]
                game_deepness_level -= 2
            elif next_step[:1].lower() == "q":
                show_text_line("you quited the game ...", Fore.RESET, Back.RESET)
                quit_the_game()
            else:
                game_deepness_level -= 1

#//--------------------------//#
#   Start the main game loop   #
#//--------------------------//#

if __name__ == '__main__':

    intro_animation()

    FILENAME = "game.db"
    if os.path.exists(FILENAME):
        while True:
            main(FILENAME)
            quit_game = input("Do you like to play again ? [n/y] : ")
            if quit_game[:1].lower() != "y":
                quit_the_game()

    else:
        show_text_line("[Error] >> Could not find game.db !!! ", Fore.RED, Back.WHITE)
        show_text_line("Program is looking for game.db in [" +os.getcwd()+ "]", Fore.RESET, Back.RESET)
        show_text_line("", Fore.RESET, Back.RESET)
        sys.exit()
