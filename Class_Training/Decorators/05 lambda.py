## labda function for basic math

add = lambda a, b: a + b
sub = lambda a, b: a - b
div = lambda a, b: a / b
mul = lambda a, b: a * b

print(add(1, 2))
print(sub(1, 2))
print(div(1, 2))
print(mul(1, 2))


## lambda function for str

a_string = lambda name, prefix: f"{prefix.title()} {name.title()}."

print (a_string("bibo", "Da mighty emperor"))