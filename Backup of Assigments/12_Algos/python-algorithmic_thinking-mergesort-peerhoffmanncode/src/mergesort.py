# TODO implement mergesort
def mergesort(my_array: list, left=0, right=-1) -> list:

    if right == -1:
        right = len(my_array)-1

    if left < right:
        middle = left + (right - left) // 2

        # mergesort both halves
        mergesort(my_array, left, middle)
        mergesort(my_array, middle + 1, right)

        # merge the halves
        merge(my_array, left, middle, right)

    return my_array


def merge(my_array, left, middle, right) -> list:
    n1 = middle - left +1
    n2 = right - middle

    # Copy data to temp arrays L[] and R[]
    left_list = my_array[left: left + n1]
    right_list = my_array[middle+1: middle + n2+1]

    # Merge the temp lists back
    # Initial index i, j, k
    i = j = 0
    k = left

    while (i < n1) and (j < n2):
        if left_list[i] <= right_list[j]:
            my_array[k] = left_list[i]
            i += 1
        else:
            my_array[k] = right_list[j]
            j += 1
        k += 1

    # Copy the remaining elements of
    # Left, if there are any
    while i < n1:
        my_array[k] = left_list[i]
        i += 1
        k += 1

    # Copy the remaining elements of
    # Right, if there are any
    while j < n2 and k < len(my_array):
        my_array[k] = right_list[j]
        j += 1
        k += 1
