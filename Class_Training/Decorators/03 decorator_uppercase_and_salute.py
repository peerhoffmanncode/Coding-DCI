# ##### Part 1 ####
def uppercase(func):
    def inner(name):
        return func(name).upper()
    return inner

@uppercase
def greet(name):
    return f"hi there {name}"

print(greet("peer"))


#### Part 2 ####

def make_title(func):
    def inner(*args):
        return func(args[0]).title()
    return inner

def add_mr(func):
    def inner(name):
        return f"Mr/Ms. {name}"
    return inner       

@make_title
@add_mr
def greetings(name):
    return name

print(greetings("fausto doe"))
