#### Functions #####

def myfunction(num1=0,num2=0,multiply=1.5,name=""):
    print(num1*multiply)
    print(num2*multiply)
    print(multiply)

# first call
#myfunction(name="peer", num1=1, num2=2, multiply=20)

# second call
#myfunction(name="fausto", num1=1, num2=2)

# def newfunction(*positional_args):
#     print(positional_args)
#     print(positional_args[6][2])
    
# newfunction(["hello", "world", "funny bunny!"],"Shaban","Fausto", "peer",78635, "something",344.34234)


def newfunction(kwargs):
    print(kwargs)
    print(kwargs["something"])
    
newfunction(name="Fausto", age=120, love="napoli", city = "hamburg", pro = "genius", )