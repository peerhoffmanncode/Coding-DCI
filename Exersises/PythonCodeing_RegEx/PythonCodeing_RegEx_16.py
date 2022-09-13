import re

def make_happy(input_str:str) -> str:
    ''' function that makes a sad string happy '''
    
    # list of eyes
    eyes = [r":", r";", r"8", r"x"]

    # for loop over eyes
    for e in eyes:
        # build regex pattern
        p = e + r"\("
        # build regex substitution string
        sub_p = e + r")"
        # find sad faces and make'em happy
        input_str = re.sub(p, sub_p, input_str)
    
    # return the happy string
    return input_str

# run very sad tests and hope to be happy 
print(make_happy("(My current mood: :(8(;(x("))
print(make_happy("I was hungry 8("))
print(make_happy("print('x('"))
print(make_happy("round(3.4)"))
