

def validate_numeric(func):
    ''' decorator function to validate if arguments are int/float'''
    def inner(a,b):
        if ((isinstance(a, float)
            or isinstance(a, int))
            and (isinstance(b, float)
            or isinstance(b, int))):
            return func(a,b)
        else:
            return f"The input arguments must be numeric"
    return inner

@validate_numeric
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

print(sum(1, 2))
print(sum(1, "2"))
print(sum(a=1, b="a"))
print(sum(a=1, b=3.4))
