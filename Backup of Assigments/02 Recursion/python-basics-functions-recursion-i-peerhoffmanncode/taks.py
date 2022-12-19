#### Task 1 ####
print()
print("#### Task 1 ####")

def countdown(number: int) -> int:
    if number == 0:
       print("0")
    else:
        print(number)
        countdown(number-1)

countdown(5)




#### Task 2 ####
print()
print("#### Task 2 ####")

def factorial(number: int) -> int:
    if number == 0:
        return 1
    return number * factorial(number -1)
    
print(factorial(0))
print(factorial(1))
print(factorial(10))


#### Task 3 ####
print()
print("#### Task 3 ####")

def harmonic_sum(number: float) -> float:
    if number == 0:
        return 0
    return ((1/number) + harmonic_sum(number -1))

print(harmonic_sum(7))
print(harmonic_sum(4))
