import re

def make_happy(input_str:str) -> str:
    faces = [r":", r";", r"8", r"x"]
    p = r"?=(\:|\;|8|x)\("  
    sub_p = r"(\:|\;|8|x))" 
    input_str = re.sub(p, sub_p, input_str)
    return input_str
    # for f in faces:
    #     p = f+r"\("  (\:|\;|\8|\x)
    #     sub_p = f+r")"
    #     input_str = re.sub(p, sub_p, input_str)
    # return input_str

print(make_happy("(My current mood: :(8(;(x("))
print(make_happy("I was hungry 8("))
print(make_happy("print('x('"))
print(make_happy("round(3.4)"))
