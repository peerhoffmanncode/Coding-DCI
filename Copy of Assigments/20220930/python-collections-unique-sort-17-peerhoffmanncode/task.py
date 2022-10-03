def unique_char_sort(a_list: list) -> list:
    ''' function to sort a list by the number of unique characters in the strings.'''
    
    # create temp dictionary to find unique characters per item
    tmp_dic = {}
    for elem in a_list:
        tmp_str = ""
        for char in elem:
            if elem.count(char) == 1:
                tmp_str += char
        tmp_dic[elem] = len(tmp_str)
        
    # sort temp dictionary by value
    sorted_dic = sorted(tmp_dic.items(), key=lambda collumn: collumn[1], reverse=False)
    
    # create output list
    final_list = []
    for key, vale in sorted_dic:
        final_list.append(key)
        
    return final_list


# test cases
strings = ['Digital',
           'Career',
           'Institute',
           'another_wired_testcase' # added tis to be sure!
           'Lecture',
           'Exercise',
           ]

print("Unsorted input:", strings)
print("Sorted output :", unique_char_sort(strings))
