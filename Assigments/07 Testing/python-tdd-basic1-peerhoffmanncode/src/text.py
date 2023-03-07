# function will convert string parameter to upper case
def to_upper(string):
    """function to upper case a string
    if type is not string, raise a TypeError!
    """
    if not isinstance(string, str):
        raise TypeError
    return string.upper()


# function will check return true if all items on
# the parameter list are upper case
def to_word_list_isupper(str_list):
    """function to upper case strings in a list
    if type is not string, raise a TypeError!
    """
    if not isinstance(str_list, list):
        raise TypeError
    for word in str_list:
        if not isinstance(word, str):
            raise TypeError
        if word.islower():
            return False
    return True
