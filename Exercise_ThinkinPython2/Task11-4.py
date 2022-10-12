'''Use a dictionary to write a faster, simpler version of has_duplicates.'''

def has_duplicates(list_to_work: list) -> bool:
    
    temp_dict = {}
    for elem in list_to_work:
        if elem in temp_dict:
            return True
        temp_dict.setdefault(elem, 0)
    
    return False

my_list = ["dog", "cat", "cat", "parrot"]

print(has_duplicates(my_list))