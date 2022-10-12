#### Task 1 ##########################
print()
print()
print("#### Task 1 ##########################")
print()

add15 = lambda x: x + 15

print(add15(1))
print(add15(-2))


#### Task 2 ##########################
print()
print()
print("#### Task 2 ##########################")
print()

isOdd = lambda x: not bool(x % 2)
isEven = lambda x: bool(x % 2)
getParity = lambda x, parity: True if not bool(x % 2) and parity == "even" else False

print(isOdd(2), isEven(2))
print(isOdd(1), isEven(1))
print(getParity(2, "odd"), getParity(2, "even"))
print(getParity(1, "odd"), getParity(1, "even"))


#### Task 3 ##########################
print()
print()
print("#### Task 3 ##########################")
print()

starts_with_p = lambda x: x.lower().startswith("p")

print(starts_with_p("Python"))
print(starts_with_p("JavaScript"))
print(starts_with_p("pirate"))


#### Task 4 ##########################
print()
print()
print("#### Task 4 ##########################")
print()

numbers = [2, 4, 5, 7, 9, 14]
factor = 2
print(list(map(lambda x: x * factor, numbers)))
