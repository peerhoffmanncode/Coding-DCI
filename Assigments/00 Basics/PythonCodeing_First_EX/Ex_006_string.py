# substring in Python

## Overview:
# The python string[start: end: step] method returns a part of the string.
# We pass start index and end index number position where both start and end index is exclusive.

## Task
### "Without own words"
#Please write a program that prints out "Hello Gregor". The challenge is that you are not allowed to create own chars & strings. You are only allowed to use elements of a given string provided in the solution.py file.

### Output
"""
"Hello Gregor"
"""

# give text to play with
given_string = """One morning, when Gregor Samsa woke from troubled dreams, 
he found himself transformed in his bed into a horrible vermin.
 He lay on his armour-like back, and if he lifted his head a 
little he could see his brown belly, slightly domed and divided by 
arches into stiff sections. The bedding was hardly able to cover 
it and seemed ready to slide off any moment. His many legs, pitifully 
thin compared with the size of the rest of him, waved about helplessly 
as he looked."""


def return_char(input_str, to_look_for):
    """
    Return the character at the given index.
    """
    return input_str[input_str.index(to_look_for):input_str.index(to_look_for)+len(to_look_for)]

part1 = return_char(given_string, "Gregor")
part2 = return_char(given_string, "H") \
        + return_char(given_string, "e") \
        + return_char(given_string, "l") \
        + return_char(given_string, "l") \
        + return_char(given_string, "o")

print(part1, part2)
