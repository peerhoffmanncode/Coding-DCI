''' Calculation Program '''

import os

# clear terminal
os.system("clear")

def addition(n1, n2):
    ''' function to add n1 and n2 '''
    return n1 + n2

def subtract(n1, n2):
    ''' function to subtract n1 and n2 '''
    return n1 - n2

def divide(n1, n2):
    ''' function to divide n1 and n2 '''
    return n1 / n2

def multi(n1, n2):
    ''' function to multiply n1 and n2 '''
    return n1 * n2

def main():
    ''' main function '''
    
    while True:
        number1 = (input("please enter number one : "))
        if number1.isnumeric() is False: 
            print ("Please enter a number!")
        else:
            number1 = float(number1)
            break

    while True:
        number2 = (input("please enter number two : "))
        if number2.isnumeric() is False: 
            print ("Please enter a number!")
        else:
            number2 = float(number2)
            break

    options = ["1", "2", "3", "4", "+", "-", "/", "*"]    
    while True:
        choices = input("(1) to add, (2) to subtract, (3) to divide, (4) to multiply :")
        if choices in options:
            break
        else:
            print("Unknown operation!")

    if choices == "1" or choices == "+":
        result = addition(number1, number2)
        SYMBOL = "+"
    elif choices == "2" or choices == "-":
        result = subtract(number1, number2)
        SYMBOL = "-"
    elif choices == "3" or choices == "/":
        SYMBOL = "/"
        if number2 != 0:
            result = divide(number1, number2)
        else:
            print ("Devision by zero is not allowed !")
            result = "invalid!"
    elif choices == "4" or choices == "*":
        result = multi(number1, number2)
        SYMBOL = "*"

    print(f"Your result for {number1} {SYMBOL} {number2} is {result}")


# Start the program
if __name__ == "__main__":
    main()
                                