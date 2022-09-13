import re

def remove_leading_zero(input_str:str) -> str:
    remove_leading = re.sub(r"^0+", "", input_str)
    remove_trailing = re.sub(r"0+$", "", remove_leading)
    return remove_trailing


lst = ["0023.07623070", "hello world", "01230"]

for i in lst:
    print(remove_leading_zero(i))