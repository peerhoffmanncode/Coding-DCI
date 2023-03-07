def quicksort(list_to_sort: list, low: int = 0, high: int = -1) -> list:
    # initial case
    if high == -1:
        high = len(list_to_sort) - 1

    # if lowest number is smaller than highest, keep sorting
    if low < high:
        # partition (dived and conquer)
        devided_list_pivot = partition_while(list_to_sort, low, high)
        # crucial to check if pivot is max left
        if devided_list_pivot != 0:
            quicksort(list_to_sort, low, devided_list_pivot - 1)
            quicksort(list_to_sort, devided_list_pivot + 1, high)

    # return final result (base case)
    return list_to_sort


def partition_while(list_to_devide: list, low: int, high: int) -> int:
    pivot = list_to_devide[low]
    i, j = low, high

    while True:  # i < j:
        while i <= j and list_to_devide[i] <= pivot:
            i += 1

        while i <= j and list_to_devide[j] >= pivot:
            j -= 1

        if i < j:
            list_to_devide[i], list_to_devide[j] = list_to_devide[j], list_to_devide[i]
        else:
            break

    list_to_devide[low], list_to_devide[j] = (
        list_to_devide[j],
        list_to_devide[low],
    )
    return j


def partition_for(list_to_devide: list, low: int, high: int) -> int:
    # define value to compare the division
    pivot = list_to_devide[high]

    # loop to find position of pivot
    for moving_high in range(low, high):
        if list_to_devide[moving_high] < pivot:
            # change list in place -> will be reflected in quicksort func
            list_to_devide[low], list_to_devide[moving_high] = (
                list_to_devide[moving_high],
                list_to_devide[low],
            )
            # add one to moving low
            low += 1

    # change list in place -> will be reflected in quicksort func
    list_to_devide[low], list_to_devide[high] = (
        list_to_devide[high],
        list_to_devide[low],
    )

    # return new pivot num
    return low
