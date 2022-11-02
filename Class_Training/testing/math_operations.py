# unit test


def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def div(a: int, b: int) -> float:
    if b != 0:
        return a / b
    else:
        return False


def mul(a: int, b: int) -> float:
    return a * b


def mod(a: int, b: int) -> float:
    return a % b
