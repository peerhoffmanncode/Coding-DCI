
secret = ""                                                     # define a variable to use for the input() function
while len(secret) < 8:                                          # create a infinite loop until a user enters the word with len > 8
    secret = input("Your (mind. 8 char) secret man ? :")        # prompt for user input, store in var: secret
                                                                # << END OF LOOP
name = input("Dude, da name? : ")                               # prompt for user input, store in var: name
year = input("okay some birth year you got? : ")                # prompt for user input, store in var: year

constr = secret+name                                            # combine var: secret and var: name and store in var: constr
fullstr = constr[::-1] + year                                   # store full output line in var: fullstr, but reverse the var constr[from: to: step], here step is -1 for reverse!!!

print(fullstr)                                                  # print out var: fullstr to user