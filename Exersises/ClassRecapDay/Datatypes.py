### Datatypes ###


# int - mutable
from datetime import date


x = 1
#print(type(x))


# float - mutable
x = 1.0

# complex - mutable
x = 1j+1

# str - immutabel
x = "hello world!"
x.capitalize()
print(x)
#print(type(x))

# List - mutable
var1 = "my variable"
x = ["h", "e", "l", "l" ,"o"]
#print("x:", x[0])

# Tuple - immutable
var1 = "my variable"
x = ("h", "h", "h", "e", "l", "l" ,"o")
x = x + ("new stuff",)
#print("x:", type(x), x)

# dictionary - mutable
#fruite store
###    KEY    VALUE
x = {"apple": 10,
     "banana": 6,
     "orange": 10,
     "pear": 100,}
print("x:", type(x), x["orange"])


