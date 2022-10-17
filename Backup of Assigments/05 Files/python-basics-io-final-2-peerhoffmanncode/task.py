from sys import exit
from glob import glob  # lib to handle file structure
from os import path, mkdir
from uuid import uuid4


def find_files(filepath: str, suffix: str) -> list:
    """Function to find all articles in a dictionary"""

    if path.exists(filepath):
        # using glob to find all files
        return glob(filepath + suffix)
    else:
        return None


def search_string_in_file(search_term, file_to_search_in) -> bool:
    """Function to find a give term in an article"""

    with open(file_to_search_in, "r") as file:
        # read all data, join to one string, make it lower case
        file_data = "".join(file.readlines()).lower()
        
    # find term in data
    if search_term.lower() in file_data:
        # if search_term is found, return True
        return True
    
    return False


def write_log(filepath, user_name, search_term, matches) -> bool:
    """Function to write a log file"""

    # create correct path to log directory
    path_list = filepath.split("/")
    filepath = "/".join(path_list[:-2]) + "/log/"
    # check if log directory exists
    if not path.exists(filepath.lower()):
        mkdir(filepath.lower())
    # check if user directory exists
    if not path.exists(filepath.lower() + user_name.lower()):
        mkdir(filepath.lower() + user_name.lower())
        
    # create unique_file_name using uuid4
    unique_file_name = (
        filepath.lower() + user_name.lower() + "/" + str(uuid4()) + ".txt"
    )
    
    # write actual log file
    with open(unique_file_name, "w") as log_file:
        print(f"Search term: {search_term}", file=log_file)
        print(f"Matches: {', '.join(matches)}.", file=log_file)


def main():
    """main program function"""

    # Constants for file handling
    FILE_SUFFIX = "*.txt"
    FILE_PATH = "src/data/articles/"

    # find all articles in the directory
    all_article: list = find_files(FILE_PATH, FILE_SUFFIX)
    if not all_article:
        print("could not find any articles to work on...")
        exit(-1)

    # get user name
    user_name = input("What is your name? ").lower()
    if not user_name:
        print("Please, provide a name.")
        exit(-1)
    print(f"Welcome {user_name.capitalize()}!")

    # start pgm loop
    while True:
        # get search term
        search_term = input("What word would you like to search for? ").lower()
        if not search_term:
            print("Please, provide a term of search.")
        else:
            print(f"Looking for [{search_term}] in {len(all_article)} articles ...")
            # find search_term in articles
            matching_articles = []
            for article in all_article:
                if search_string_in_file(search_term, article):
                    matching_articles.append(article)
            # print out the articles
            if matching_articles:
                print(f"** Found {len(matching_articles)} matching articles: **")
                for index, articles in enumerate(matching_articles):
                    articles = articles[len(FILE_PATH) : articles.find(FILE_SUFFIX[1:])]
                    matching_articles[index] = articles
                    print(f"[+]\t{articles}")
                # write LOG file!
                write_log(FILE_PATH, user_name, search_term, matching_articles)
            else:
                print("nothing was Found! No log will be created.")

        # ask user if he/she wants to search other stuff
        while True:
            search_again = input(
                "Would you like to search something else?(Y/N) "
            ).lower()
            if search_again == "y" or search_again == "yes":
                break
            else:
                exit(0)


if __name__ == "__main__":
    main()
