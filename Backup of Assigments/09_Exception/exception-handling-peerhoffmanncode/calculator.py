class MathematicalError(Exception):
    """General mathematical error exception class."""

    pass


class Calculator:
    """calcualtor class"""

    def __init__(self, user_input):
        """constructor"""
        # define instance variables
        self.n1, self.op, self.n2 = self.parse_input(user_input)

    def parse_input(self, user_input):
        # breakpoint()
        elements = user_input.strip().split(" ")
        if len(elements) != 3:
            raise MathematicalError("Input does not consist of three elements")
        if elements[1] not in "+-*/":
            raise MathematicalError('Invalid operator. Can only use "+" or "-"')
        # if not elements[0].isdigit() or not elements[2].isdigit():
        #     raise MathematicalError("The first and third input value must be numbers")
        try:
            n1 = float(elements[0])
            op = elements[1]
            n2 = float(elements[2])
        except ValueError:
            raise MathematicalError("The first and third input value must be numbers")
        else:
            return n1, op, n2

    def calculate(self):
        """calculate the number of n1 & n2"""
        if self.op == "+":
            return self.n1 + self.n2
        if self.op == "-":
            return self.n1 - self.n2
        if self.op == "*":
            return self.n1 * self.n2
        if self.op == "/":
            if self.n2 == 0:
                raise MathematicalError("Division by zero!")
            return self.n1 / self.n2


if __name__ == "__main__":
    while True:
        user_input = input(">>> ")
        if user_input == "quit":
            break
        calculator = Calculator(user_input)

        result = calculator.calculate()
        print(result)
