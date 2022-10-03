

def is_pangram(panagram_string: str) -> bool:
    ''' function that adds each character of a string to a list.
        if list contains 26 characters [a-z] return true! 
    '''
    if not isinstance(panagram_string, str):
        return "wrong data input!"
    
    result = []
    for d in panagram_string:
        if not d.isalpha():
            continue
        elif d.lower() not in result:
            result.append(d)
    if len(result) >= 26:
        return True
    return False

#test


print(is_pangram('Waltz, bad nymph, for quick jigs vex.'))
print(is_pangram('Glib jocks quiz nymph to vex dwarf.'))
print(is_pangram('Sphinx of black quartz, judge my vow.'))
print(is_pangram('How vexingly quick daft zebras jump!'))
print(is_pangram('The five boxing wizards jump quickly.'))
print(is_pangram('Jackdaws love my big sphinx of quartz.'))
print(is_pangram('Pack my box with five dozen liquor jugs.'))
#False test
print(is_pangram('abcdefghijklmnopqrstuvwxyFALSE!'))
