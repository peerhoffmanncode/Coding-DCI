from add import add
from subtraction import subtraction


def main():
    """
    main function that inits the program.

    *** Doctest ***
    >>> add(1,1)
    2

    >>> subtraction(5,3)
    2
    """

    user_input = input("Which math do you like to do (1 add, 2 subtraction) : ")

    if user_input in ["1", 1]:
        a = int(input("Number 1 to add: "))
        b = int(input("Number 2 to add: "))
        print(f"Result {add(a,b)}")

    elif user_input in ["2", 2]:
        a = int(input("Number 1 to add: "))
        b = int(input("Number 2 to add: "))
        print(f"Result {subtraction(a,b)}")

    else:
        print("i do not know wht you like to do!")


if __name__ == "__main__":
    main()