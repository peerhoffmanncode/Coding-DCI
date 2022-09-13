import re

def is_mathematical(input_str:str) -> bool:
    p = r"\d+\s*(\+|\-|\*|\/|%)\s*\d+"
    r = re.search(p, input_str.strip())

    if r is None:
        return False
    return True

lst = ["5 + 2", "9 * 1", "hello world", "123", "5 + foo", "234982734 / 238498374"]

for i in lst:
    print(is_mathematical(i))