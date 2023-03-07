#######################
### no decorator ! ####
#######################
def divide(a, b):
    return a / b

print (divide(4,3))
print (divide(5,2))

###############################
### with decorator !  no @ ####
###############################
def check_divisor(func):
    def inner(a, b):
        if b == 0:
            return "null division!"
        return func(a,b)
    return inner

def divide2(a, b):
    return a / b


divide_obj = check_divisor(divide2)
print(divide_obj(4,2))
print(divide_obj(4,0))
print(divide_obj(4,-1))


################################
### with decorator ! WITH @ ####
################################

@check_divisor
def divide3(a, b):
    return a / b

print(divide3(4,2))
print(divide3(4,0))
print(divide3(4,-1))
