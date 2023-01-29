def permutations(lst, length):
    if length == 0:
        return [[]]

    permuts = []
    for i, item in enumerate(lst):
        remaining_items = lst[:i] + lst[i+1:]
        for perm in permutations(remaining_items, length-1):
            permuts.append([item] + perm)
    return permuts

print(permutations([1,2,3,4], 2))
