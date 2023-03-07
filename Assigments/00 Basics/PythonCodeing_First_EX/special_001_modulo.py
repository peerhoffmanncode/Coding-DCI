

user_input = ""                                     # define a variable to use for the input() function
while user_input != "end":                          # create a infinite loop until a user enters the word "end"
    user_input = input ("give me some :")           # prompt for user input, store in var: user_input
                    
    if len(user_input) % 2 == 0:                    # if statement! check if a len() of a given input is even or odd using the % (modulo) operator
        print ("this is even!")                     # print it is even
    else:                                           # else statement! if not even, do the following
        print ("nope, not even!")                   # print it is not even / it is odd!
        
# end of pgm   