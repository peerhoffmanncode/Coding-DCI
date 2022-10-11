### Fibonnaci / etc ...

import sys
sys.setrecursionlimit(2000)     # set the limit to receive depth

print()
### factorial ####

def factorial(n):
    #base case
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("####### recursive factorial function #######")
for i in range(11):
    print(f"{factorial(i):10}, i -> {i}")
    
print()
    
#### Sum ####

# def get_sum(sum_list, size, sum):
#     if size == 0:
#             return sum
    
#     # Function Call Observe sum+array[size-1]
#     # to maintain sum of elements
#     return get_sum(sum_list, size - 1,
#             sum + sum_list[size - 1])
    
# print(get_sum(x, len(x), 0))

print("####### recursive summing function #######")

x = [0,1,2,3,4,5,6,7,8,9,10]

def get_sum(sum_list: list):
    ''' recursive function to get sum of elements from a list '''
    # base case
    if len(sum_list) < 1:
        return 0 # int(sum_list[0])
    # add element [0] + element [1] -> store to element [1]
    # sum_list[1] = sum_list[0] + sum_list[1]
    # pop element [0]
    first = sum_list.pop(0)    
    # return current scope to next recursive call
    print (f"element to add {first}, remaining list {sum_list}")
    return first + get_sum(sum_list)

print(f"given list = {x}")
print(f"result will be = [{get_sum(x)}]")
print()