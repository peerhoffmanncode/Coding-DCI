# data
from time import perf_counter
from quicksort import quicksort
from quicksort2 import quick_sort

import random


def bubble_sort(array: list) -> list:
    lenght = len(array)
    while lenght:
        for i in range(lenght - 1):
            print(array[i] , array[i + 1])
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        lenght = lenght - 1
    return array


array: list = [5,4,3,2,1,0]

# #print("Before bubble sorting: ", array)
# a = perf_counter()
# array = bubble_sort(array)
# a = perf_counter() - a
# #print("After bubble sorting: ", array)
# print("Bubble sort Time:", a)


array: list = [random.randint(0, 100) for num in range(100000)]
#array: list = [9,8,7,6,5,4,3,2]

print("Before quick sorting: ", array)
a = perf_counter()
array = quick_sort(array, 0, len(array)-1)
a = perf_counter() - a
print("After quick sorting: ", array)
print("Quick sort Time:", a)
