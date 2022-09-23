def full_name(*args): # "tuple"
    ''' function to concatenate a tuple of args and return them
        >> using a for loop !'''
    fullname = ""
    for name in args:
        fullname += name + " "
    return fullname.rstrip()

def join_full_name(*args): # "tuple"
    ''' function to concatenate a tuple of args and return them
        >> using the join function!'''
    return " ".join(args)

# using full_name here
print(full_name("Charly", "Bobo", "the third", "the master of the known universe", "heroic user of the plunger"))
print(full_name("Charly", "Bobo"))
print(full_name("Charly"))

# using join_full_name here
print(join_full_name("Charly", "Bobo", "the third", "the master of the known universe", "heroic user of the plunger"))
print(join_full_name("Charly", "Bobo"))
print(join_full_name("Charly"))