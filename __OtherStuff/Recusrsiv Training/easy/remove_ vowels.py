def remove_vowels(string:str):
    #print(string)
    if len(string) < 1:
        return string
    if string[0].lower() in "aeiou":
        return remove_vowels(string[1:])
    else:
        return string[0] + remove_vowels(string[1:])

print(remove_vowels('apple'))     # ppl
print(remove_vowels('orange'))    # rng
print(remove_vowels('pear'))      # pr
print(remove_vowels('pineapple')) # pnppl
print(remove_vowels('durian'))    # drn
print(remove_vowels('banana'))    # bnn
