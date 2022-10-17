# Task - Filter lists
def digit_filter(data:list) -> list:
    ''' function to filter given data for digits
        remove item if invalid => isdigit = True!'''
    tmp = [] # define temporary list
    for item in data:
        found_digit = False
        for char in item:
            if char.isdigit():
                found_digit = True
                break
        if not found_digit:
            tmp.append(item) # include valid item!
    return tmp

# data given
l33t = ['Digital Car33r Institute',
        'DCI',
        'Digital',
        'Career',
        'Inst1tut3',
        # added new stuff tho check...
        '1337',
        '1ee7',
        'leet']

print(digit_filter(l33t))