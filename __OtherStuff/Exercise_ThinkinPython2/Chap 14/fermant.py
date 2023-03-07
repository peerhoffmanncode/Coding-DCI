# Fermant => pow(a,n) + pow(b,n) = pow(c,n)
import random


def check_fermant(a: int, b: int, c: int, n: int) -> bool:

    if (n > 2) and (pow(a, n) + pow(b, n) == pow(c, n)):
        print(
            f"a:{a},b:{b},c:{c},n:{n}, Fermant was wrong !, {a}^{n}+{b}^{n} = {pow(a,n) + pow(b,n)}, and so is {c}^{n} = {pow(c,n)}"
        )
        return True
    elif (n > 2) and (pow(a, n) + pow(b, n) != pow(c, n)):
        print(
            f"a:{a},b:{b},c:{c},n:{n}, no that doesn't work!, {a}^{n}+{b}^{n} = {pow(a,n) + pow(b,n)}, but {c}^{n} = {pow(c,n)}"
        )
        return False
    else:
        print(f"wrong input")
        return False


check = False
while check == False:
    a = random.randint(0, 20)
    b = random.randint(0, 20)
    c = random.randint(0, 20)
    n = random.randint(3, 20)

    check = check_fermant(a, b, c, n)
