#!/usr/bin/env python

from mergesort import mergesort


def main():
    a = [0, 3, 7, 2, 8, 4, 6, 9, 1, 4]
    b = mergesort(a)
    # We check if the result is correct
    c = [0, 1, 2, 3, 4, 4, 6, 7, 8, 9]
    if len(b) != len(c):
        print("Failed - length is incorrect!")
        print(b)
        print(c)
        return
    for i in range(0, len(c) - 1):
        if b[i] != c[i]:
            print("Failed - order is incorrect!")
            print(b)
            print(c)
            return
    print(b)
    print(c)
    print("Congratulations! No error detected.")


if __name__ == "__main__":
    main()
