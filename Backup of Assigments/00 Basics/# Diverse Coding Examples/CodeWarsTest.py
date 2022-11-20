def is_square(n):
    import math
    
    # squareroot of n to get the base
    # check if the base mod 2 is 0
    
    if n < 0: return False # check for negative number
    if n == 0: return True # check for 0
        
    base = math.sqrt(n)
    root = int(base)
    dot = base - root
    print (base, root, dot)

    
    if dot > 0: 
        return False
    else:
        return True



print(is_square(25))