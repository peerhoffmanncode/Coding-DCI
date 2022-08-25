# find in Python
## Task - Finding Nemo
# You need to find the word "Nemo" in a given string and return its position in that string, like this:
# ```
# I found Nemo at [index]!
# ```
# If you can't find Nemo, return:
# ```
# I can't find Nemo :("
## Examples:

# "I am finding Nemo !"  -->    "I found Nemo at 13!"  
# "Nemo is me"           -->    "I found Nemo at 0!"  
# "I Nemo am"            -->    "I found Nemo at 2!"  
# "Hello World"          -->    "I can't find Nemo :("

def find_any_string(main_string: str, search_string: str) -> str:
    """ Function to find a matching string in the main string 
        returns the position in that string
    """
    indexpos = main_string.find(search_string)
    if indexpos == -1:
        return "I can't find Nemo :("
    else:
        return f"I found Nemo at [{indexpos}]!"
    
print(find_any_string("I am finding Nemo !", "Nemo"))
print(find_any_string("Nemo is me", "Nemo"))
print(find_any_string("I Nemo am", "Nemo"))
print(find_any_string("Hello World", "Nemo"))