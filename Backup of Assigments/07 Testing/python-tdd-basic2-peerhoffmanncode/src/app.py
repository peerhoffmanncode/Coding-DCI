from random import randrange

# function will return random number between start and end parameter where end is included
def rnd(start, end):
    return randrange(start, end + 1)


# function should return the greatest number in a list
def max_num_in_list(the_list: list) -> int:
    return max(the_list)
