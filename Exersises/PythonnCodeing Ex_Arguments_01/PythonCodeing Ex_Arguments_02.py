# The application in this file will read the command line options using argparse.
# This application should support positional arguments and be called like this: `./app3.py [FIRST_NAME] [LAST_NAME] [AGE]`
# If age is not specified, it should be assumed that it is 100. If the last name is not specified, it should be assumed that it is "Hanson". If the first name
# is not specified, should be assumed that it is "Larry".
# This application should also support the option `--fast`. It should print "fast mode enabled" if this is one of the options.
# The app should then output the text "Hello [FIRST_NAME] [LAST_NAME]! I see that you have had [AGE + 1] birthdays.".

import argparse
import os

os.system("clear")

parser = argparse.ArgumentParser(description="Arguments")

# -- fast argument
parser.add_argument("--fast", help="enable the fast mode", action="store_true")

# firstname argument
parser.add_argument(
    "first_name",
    type=str,
    metavar="[FIRST NAME]",
    default="Larry",
    help="Enter your first name",
    nargs="?",
)

# lastname argument
parser.add_argument(
    "last_name",
    type=str,
    metavar="[LAST NAME]",
    default="Hanson",
    help="Enter your last name",
    nargs="?",
)
# age argument
parser.add_argument(
    "age", type=int, metavar="[AGE]", default=100, help="Enter your age", nargs="?"
)

# pass all arguments into args
args = parser.parse_args()

#print result
print(
    f"Hello {args.first_name} {args.last_name}!"
    f"\nI see that you have had {args.age+1} birthdays."
)

# print if fast-mode is enabled
if args.fast is True:
    print("Hell yeah and you are on your fast mode !!!")
