from animal import Animal


class Dog(Animal):
    def __init__(self):
        super().__init__(number_of_legs=4, number_of_eyes=2)

    def breathe(self):
        """
        Overritten function to modle behavior of a dog.
        """
        return_value = "Dogs love to breathe with their mouths open."
        print(return_value)
        return return_value

    def walk(self):
        return_value = "Dogs love to run."
        print(return_value)
        return return_value
