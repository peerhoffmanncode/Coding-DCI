def count_characters(data) -> dict:
    ''' count each character in data
        return a dictionary'''
    if not isinstance(data, str):
        return "wrong data input!"
    
    result = {}
    for d in data:
        if d.lower() in result.keys():
            result[d] += 1
        else:
            result.update({d.lower(): 1})
    return result


## test cases
print(count_characters("Elephant"))
print(count_characters("awesome"))
print(count_characters(123))
        


