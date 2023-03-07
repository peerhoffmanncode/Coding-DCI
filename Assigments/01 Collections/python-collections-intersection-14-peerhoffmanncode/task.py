def intersection(list1: list, list2: list) -> list:
    working_set1 = set(list1)
    working_set2 = set(list2)
    return list(working_set1.intersection(working_set2))

list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
print(intersection(list_1, list_2))