
def debug(func):
    ''' decorator function to print out debug information '''
    def inner(*args, **kwargs):
        print("**********")
        if args:
            print(f"Positional arguments: {args[0]},{args[1]}")
        else:
            print("There are no positional arguments")
        if kwargs:
            print(f"keyword arguments: a={kwargs['a']},b={kwargs['b']}")
        else:
            print("There are no keyword arguments")
        return f"Result: {func(*args, **kwargs)}"
        # return func(*args, **kwargs)
    return inner


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

@debug
@validate_numeric
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

print(sum(1, 2))
print(sum(a=1, b=2))
print(sum(1, "a"))
