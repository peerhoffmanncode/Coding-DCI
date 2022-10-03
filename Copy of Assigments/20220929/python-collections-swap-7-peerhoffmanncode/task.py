def swap(da_list: list, idx1: int, idx2: int) -> list:
    da_list[idx1], da_list[idx2] = da_list[idx2], da_list[idx1]
    return da_list

swap_list = [23, 65, 19, 90]

print("before", swap_list)
swap(swap_list, 1, 3)
print("after", swap_list)