# code
# A Python program to demonstrate inheritance

class Person:

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)


class Emp(Person):

    def __init__(self, name, id):
        super().__init__(name, id)
        self.name_ = name

    def Print(self):
        return("Emp class called")


Emp_details = Emp("2Mayank", 103)

# calling parent class function
print("2",Emp_details.name, Emp_details.Print())
