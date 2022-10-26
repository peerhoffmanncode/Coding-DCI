"""
Identify what is common?
"Base case" or "Base class"

Attributes / fields
===================
- first_name
- last_name
- gender (3)
legs
identification
date_of_birth
shoe_size

Methods
=======
- talk()
- run()
- cry()
- drink() -- special Adult? college student
- study() -- after the ages of 4

etc.

"""


class Person:
    def __init__(self, first_name: str, last_name: str, gender: str, legs: int = 2):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.legs = legs

    def talk(self) -> str:
        return "Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative approaches to corporate strategy foster collaborative thinking to further the overall value proposition. Organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment."

    def run(self, destination: str, origin: str) -> str:
        return f"Hey, I am {self.first_name}, I am running towards {destination} away from {origin}"

    def cry(self, date) -> str:
        if date == "today":
            return "We shall cry today"
        elif date == "monday":
            return "TGIm"  # TGIF
        elif self.legs < 2:
            return "Ouch, it is going to be hard!"
        else:
            return "Not enough tears today"

    # design a full name function
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


if __name__ == "__main__":
    p1 = Person("Fausto", "Doe", "Other")
    p2 = Person("Emily", "Doe", "Female", 1)
    p3 = Person("Reza", "Doe", "Male")
    print(p1.run("Bristol", "Napoli"))

    print(p1.cry("today"))
    print(p1.full_name())
