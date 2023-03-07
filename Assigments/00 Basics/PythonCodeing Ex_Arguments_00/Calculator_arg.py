''' Calculation Program '''

import sys
print (sys.argv)

if len(sys.argv) != 4 or sys.argv[1].isnumeric() is False or sys.argv[3].isnumeric() is False:
    print("pleasee enter two numbers and a mathematical symbol [+, -, /, x]!")
    print("eg: 5 + 5")
    print("")
    sys.exit()
    
number1 = float(sys.argv[1])
number2 = float(sys.argv[3])

options = ["+", "-", "/", "x"]
if sys.argv[2] in options:
    choices = sys.argv[2]
else:
    print("pleasee enter two numbers and a mathematical symbol!")
    print("eg: 5 + 5")
    print("")
    sys.exit()

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
    elif choices == "4" or choices == "x":
        result = multi(number1, number2)
        SYMBOL = "x"

    print(f"Your result for {number1} {SYMBOL} {number2} is {result}")


# Start the program
if __name__ == "__main__":
    main()
                                