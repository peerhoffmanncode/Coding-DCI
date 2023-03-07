from dog import Dog


class GermanShepherd(Dog):
    def walk(self):
        """
        Overritten function to modle behavior of a dog.
        """
        return_value = "German Shepherds show their beautiful fur while running."
        print(return_value)
        return return_value
