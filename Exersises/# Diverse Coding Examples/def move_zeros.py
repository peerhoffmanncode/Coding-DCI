def move_zeros(lst):
    
    #if lst == []: return lst
    for i in lst:
        if i == "0" or i == 0:
            lst.remove(i)
            list.append(i)  
    return lst

list = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]

print(list)
print(move_zeros(list))