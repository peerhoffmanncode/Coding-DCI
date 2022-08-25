# Functioninator 8000
## Task
# Create a function that takes a single word string and does the following:
# * Concatenates inator to the end if the word ends with a consonant otherwise, concatenate -inator instead.
# * Adds the word length of the original word to the end, supplied with '000'.

## Input / Output

def inatorInator(text):
    return text + "inator " + str(len((text))) + "000"



print(inatorInator("Shrink"))
print(inatorInator("Doom"))
print(inatorInator("EvilClone"))