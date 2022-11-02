

def add (a: int,b: int) -> int:
    """
    This is a function that adds up two arguments: a + b
    >>> add(2,2)
    4

    Args:
        a (int): Number to add together
        b (int): Number to add together

    Returns:
        _type_: _description_
    """
    return a+b


if __name__ == '__main__':
    print(add(2,2) == 4)
    print(add(5,2) == 7)
    print(add(6,2) == 8)
