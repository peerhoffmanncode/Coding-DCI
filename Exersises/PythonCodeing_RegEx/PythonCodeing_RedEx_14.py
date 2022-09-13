import re

def remove_leading_zero(input_str:str) -> str:
    return re.sub(r"^0+", "", input_str)
    

lst = ["0023.07623070", "hello world", "01230"]

for i in lst:
    print(remove_leading_zero(i))