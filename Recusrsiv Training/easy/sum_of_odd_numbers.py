def sum_of_odd_numbers(lst: list):
    if lst == []:
        return 0

    num = lst[0]

    if num % 2 == 0:
        return sum_of_odd_numbers(lst[1:]) - num
    else:
        return num + sum_of_odd_numbers(lst[1:])

print(sum_of_odd_numbers([1,2,3,4]))   # -2
print(sum_of_odd_numbers([1,2,3,4,5])) # 3
print(sum_of_odd_numbers([1,3,5]))     # 9
print(sum_of_odd_numbers([2,4,6]))     # -12
print(sum_of_odd_numbers([99,10,10]))  # 79
