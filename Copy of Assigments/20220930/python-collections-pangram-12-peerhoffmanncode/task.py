
# 1st approach using list
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

# 2st approach using set (fixed)
def is_pangram_set(panagram_string: str) -> bool:
    ''' function that adds each character of a string to a list.
        if list contains 26 characters [a-z] return true! 
    '''
    if not isinstance(panagram_string, str):
        return False # "wrong data input!"
    
    alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", 
                "j", "k", "l", "m", "n","o", "p", "q", "r", 
                "s", "t", "u", "v", "w", "x", "y", "z"}
    panagram_set = set(panagram_string.lower())

    return True if len(alphabet.intersection(panagram_set)) == 26 else False

# Testcases
print(is_pangram_set('Waltz, bad nymph, for quick jigs vex.'))
print(is_pangram_set('Glib jocks quiz nymph to vex dwarf.'))
print(is_pangram_set('Sphinx of black quartz, judge my vow.'))
print(is_pangram_set('How vexingly quick daft zebras jump!'))
print(is_pangram_set('The five boxing wizards jump quickly.'))
print(is_pangram_set('Jackdaws love my big sphinx of quartz.'))
print(is_pangram_set('Pack my box with five dozen liquor jugs.'))
#False test
print(is_pangram_set('abcdefghijklmnopqrstuvwxyFALSE!'))
