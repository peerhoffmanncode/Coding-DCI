def double(string:str):
    #print(string)
    if len(string) < 1:
        return string

    return string[0]*2 + double(string[1:])

print(double('apple'))   # aappppllee
print(double('orange'))  # oorraannggee
print(double('pear'))    # ppeeaarr
print(double('abc'))     # aabbcc
print(double('zz'))      # zzzz
