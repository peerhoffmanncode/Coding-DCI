import math


def is_triangle(a: float, b: float, c: float) -> bool:
    print(pow(a, 2), pow(b, 2), pow(c, 2))
    if round(pow(a, 2) + pow(b, 2), 2) == round(pow(c, 2), 2):
        return True
    if round(pow(b, 2) + pow(c, 2), 2) == round(pow(a, 2), 2):
        return True
    if round(pow(c, 2) + pow(a, 2), 2) == round(pow(b, 2), 2):
        return True

    return False


a = float(input("gibt's du a: "))
b = float(input("gibt's du b: "))
c = float(input("gibt's du c: "))
# c = math.sqrt(pow(a,2)+pow(b,2))

if is_triangle(a, b, c):
    print("jo, is'n Triangle!")
else:
    print("Na! Nix Triangle!")
