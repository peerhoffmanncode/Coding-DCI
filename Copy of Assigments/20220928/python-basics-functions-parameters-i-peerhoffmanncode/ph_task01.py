

def isEven(num: int) -> bool:
    ''' function to check if num is even '''
    return bool(num % 2)
    # if num % 2 == 0:
    #     return True
    # return False


def isOdd(num: int) -> bool:
    ''' function to check if num is odd '''
    return not bool(num % 2)
    # if num % 2 != 0:
    #     return True
    # return False


print(isOdd(1), isEven(1))
print(isOdd(657842), isEven(657842))
print(isOdd(0), isEven(0))