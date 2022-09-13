import re

def remove_leading_zero(input_str:str) -> str:
    ''' function that removes leading&trailing zero characters'''
    
    # remove leading zero characters
    remove_leading = re.sub(r"^0+", "", input_str)
    # remove trailing zero characters
    remove_trailing = re.sub(r"0+$", "", remove_leading)
    # return final result
    return remove_trailing

# run test with list of a testset
lst = ["0023.07623070", "hello world", "01230"]

for i in lst:
    print(remove_leading_zero(i))