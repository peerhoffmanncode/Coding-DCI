def combination(lst, length):
    if length == 0:
        return [[]]

    permuts = []
    for i, item in enumerate(lst):
        remaining_items =  lst[i+1:]
        for perm in combination(remaining_items, length-1):
            permuts.append([item] + perm)
    return permuts

print(combination([1,2,3,4], 2))
