# Strings "a-z 0-9 !&"%$/($)"
# integer 0-9   10
# float X.Y     10.0

# Define a variable
my_var = "my string"
print (my_var)

# Define a variable with escaping the "" with the \ char
my_var = "my next \"with\" string"
print (my_var)


# combining strings 

my_var1 = "part 1 of the string________".find("string")             # << return 14 as INT !!! my_var1 will be a INT var!
my_var2 = "part 2 of the string"                                    # will be a string var
my_var4 = 10                                                        # will be a int var

my_var3 = str(my_var1) + " " + my_var2 + " _ " + str(my_var4)       # combine! but use str() to make int as a str !


# selecting a part of a string

to_char = 2                                                         # define a int var to use as position
my_new_string = "abcdefgh"                                          # define a string as data to use
               # 01235678

print (my_new_string[0    :to_char+1])                              # print out art of a string [from_ :to_] - to is the first char to exclude!
                #    from  to                                       # use +1 to include the char you like to see!