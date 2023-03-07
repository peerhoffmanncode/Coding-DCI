def sum_array(arr) -> int:
    if arr == None and len(arr) > 2: return 0
    return sum(arr) - max(arr) - min(arr)
    
    
    
print(sum_array([6, 2, 1, 8, 10]))