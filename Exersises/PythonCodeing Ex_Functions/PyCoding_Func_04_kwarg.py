
def test(**kwargs):
    print(kwargs, type(kwargs)) # holds a dict of all passed key word arguments

def test2(*args):
    print(args, type(args)) # holds a tuple of all passed arguments

test(name="TST", lname="bibo", num=10, bibo=True)
test2("TST", "lname=""bibo", 10, True)
