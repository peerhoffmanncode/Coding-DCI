def partition(list, low, high):

    # right most element in list
    pivot = list[high]

    # pointer to a greater element
    i = low - 1

    # loop through all list items comparing them to the pivot
    for j in range(low, high):
        if list[j] <= pivot:
            # if the element is smaller than the pivot, we swap it with the greater element
            i = i + 1 #
            list[i], list[j] = list[j], list[i]

    # swap the pivot with a greater element (specified by i)
    list[i + 1], list[high] = list[high], list[i + 1]

    # return the position from where the partition or division is done
    return i + 1

def quick_sort(list, low, high):
    if low < high:
        # find pivot element
        # which fulfills these conditions:
        # element smaller than pivot are the left
        # elements greater than the pivot are on the right
        pi = partition(list, low, high)

        # recurse on the left side of the list
        quick_sort(list, low, pi - 1)

        # recurse on the right side of the list
        quick_sort(list, pi + 1, high)
    return list
