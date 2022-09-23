''' basic math program :-) '''

def add(x: float, y: float):
    ''' addition function '''
    return x + y


def sub(x: float, y: float):
    ''' subtraction function '''
    return x - y


def mul(x: float, y: float):
    ''' multiplication function '''
    return x * y


def div_floor(x: float, y: float):
    ''' rounded division function '''
    if int(y) == 0:
        return False
    return int(round(x / y))       # floor div!


def div(x: float, y: float):
    ''' division function '''
    if int(y) == 0:
        return False
    return x / y       # floor div!


def powerof(x: float, y: float):
    ''' power of function '''
    return pow(x, y)       # floor div!

# declare variables for the maths
#a, b = 10, 5.5
a = float(input("Number 1: "))
b = float(input("Number 2: "))

# print out the returns of the functions (format string print out)
print(f"Value a: {a}, Value b: {b}")
print (f"Addition              : {add(a, b)}")
print (f"Subtraction           : {sub(a, b)}")
print (f"Multiplication        : {mul(a,b)}")
print (f"Rounded Division      : {div_floor(a,b)}")
print (f"Division              : {div(a,b):.1f}")
print (f"the power of {a}^{b} : {powerof(a,b):.1f}")