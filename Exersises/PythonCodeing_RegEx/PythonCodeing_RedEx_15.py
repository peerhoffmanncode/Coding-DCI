import re

def is_mathematical(input_str:str) -> bool:
    ''' function the checks a string for a correct equasion '''

    # build regex pattern
    p = r"\d+\s*(\+|\-|\*|\/|%)\s*\d+"
    # validate input string by pattern
    r = re.search(p, input_str.strip())

    # check if re.search found a valid equasion
    if r is None:
        return False # no match
    return True      # match


# run test with list of a testset
lst = ["5 + 2", "9 * 1", "hello world", "123", "5 + foo", "234982734 / 238498374"]

for i in lst:
    print(is_mathematical(i))