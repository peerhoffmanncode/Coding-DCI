# Functioninator 8000
## Task
# Create a function that takes a single word string and does the following:
# * Concatenates inator to the end if the word ends with a consonant otherwise, concatenate -inator instead.
# * Adds the word length of the original word to the end, supplied with '000'.

## Input / Output

def inatorInator(text:str):
    """
    Function to check if a given words last char is a consonant.
    If so add inator, else -inator
    return with len of the given word and add "000" to the line
    """
    if (   text[-1].lower() == "a"
        or text[-1].lower() == "e"
        or text[-1].lower() == "i"
        or text[-1].lower() == "o"
        or text[-1].lower() == "u"):
        inator = "-inator "
    else:
        inator = "inator "
    return text + inator  + str(len((text))) + "000"


# Test some words and print them out
print(inatorInator("Shrink"))
print(inatorInator("Doom"))
print(inatorInator("EvilClone"))
