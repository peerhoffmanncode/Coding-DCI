#!/usr/bin/env python


def squared(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError
    return number**2


if __name__ == "__main__":
    squared(100)
