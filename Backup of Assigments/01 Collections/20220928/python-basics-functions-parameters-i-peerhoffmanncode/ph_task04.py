

def sumAll(*numbers):
    ''' function to sum all numbers in multi dimensional lists '''
    sumof = 0
    if isinstance(*numbers) != list:
        return "ERROR! Wrong data type!"
    
    for main_list in numbers:
        try:
            flatten_list = [element for sublist in main_list for element in sublist]
            sumof += sum(flatten_list)
        except TypeError:
            sumof += sum(main_list)
    return sumof
        
test7 = 5
test0 = [0, 2, 4, 5]    
test1 = [[0, 2, 4, 5]]
test2 = [
    [0, 2, 4, 5],
    [6],
    [0, 2, 4, 5, 1, 4, 3, 2]
]
print(sumAll(test0))
print(sumAll(test1))
print(sumAll(test2))
print(sumAll(test7))