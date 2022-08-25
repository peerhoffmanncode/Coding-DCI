# # replace() in python
# ## Overview:
# The replace() method replaces each substring of a string that matches the given string. 
# ## Task
# Write a program that replaces the standalone "dog" in the following sentence with "cat".
# Use f-string when printing the output.
# ## Input/Output
# ```
# "A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."  -->  "Output: A dogmatic cat buys dogecoin to become rich and buy hotdogs every day."
# ```

def find_and_replace(input_string: str, search_string: str, replace_string: str) -> str:
    """ Function to find and replace the given string in the given input string
        only find standalone words! """
    return input_string.replace(" " + search_string + " ", " " + replace_string + " ")


print("")
print(find_and_replace("A dogmatic dog buys dogecoin to become rich and buy hotdogs every day.", "dog", "cat"))
print("")
