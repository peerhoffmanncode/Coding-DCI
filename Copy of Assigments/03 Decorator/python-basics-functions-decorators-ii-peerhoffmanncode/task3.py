
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
    return inner


def cache(memory_dict):
    ''' decorator factory function'''
    def decorator(func):
        ''' decorator function to store calcualtion in a memory cache'''
        def inner(*args, **kwargs):
            if args:
                tuple_var = args
            if kwargs:
                tuple_var = kwargs['a'], kwargs['b']
                
            if memory_dict.get(func):
                if memory_dict[func].get(tuple_var):
                    result = memory_dict[func].get(tuple_var)
                    print("Using the cache : ", end = "")
                else:
                    result = func(*args, **kwargs)
                    memory_dict[func].update({tuple_var:result})
                    print("Calculating     : ", end = "")
            else:
                result = func(*args, **kwargs)
                memory_dict[func] = {tuple_var:result}
                print("Calculating     : ", end = "")
            return result
        return inner
    return decorator


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



memory_dict = {}
@debug        #possible to include the debug here!
@cache(memory_dict)
@validate_numeric
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b



### possible optimization if 1,2 and 2,1 are treated as the same!
print(sum(1, 2))
print(sum(1, 2))
print(sum(3, 2))
print(sum(3, 2))
print(sum(2, 1))
print(sum(1, 2))
print(sum(a=10,b=20))
print(sum(10,20))
