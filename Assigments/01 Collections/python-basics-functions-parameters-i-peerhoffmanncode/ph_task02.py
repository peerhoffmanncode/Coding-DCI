def isEven(num: int) -> bool:
    ''' function to check if num is even '''
    if num % 2 == 0:
        return True
    return False


def isOdd(num: int) -> bool:
    ''' function to check if num is odd '''
    if num % 2 != 0:
        return True
    return False


def getParity(num: int, parity: str ):
    ''' function to check if parity is ok '''
    if parity.lower() == "even" or parity.lower() == "odd":
        return isEven(num), isOdd(num)
    else:
        return "Parity indicated is unknown"

print(getParity(1, "odd"))
print(getParity(657842, "even"))
print(getParity(0, "even"))
print(getParity(-2, "number"))