
## closurs without argument

def outer():
    print("1 - hi, i am form the outer one")
    def inner():
        print("1 - hi i am from the inner function")
    return inner

instance = outer()
instance()


## closurs with argument

def outer_with_arg(name):
    print (f"2 - hi, {name} i am form the outer one")
    def inner():
        return (f"2 - hi {name} i am from the inner function")
    return inner

print(outer_with_arg("bibo")())


