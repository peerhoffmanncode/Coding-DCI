### OOP !!
class Person:
    def __init__(self, name, age, augenanzahl) -> None:
        self.name = name
        self.age = age
        self.augenanzahl = augenanzahl

    def __str__(self):
        return f"ich bin {self.name} und bin {self.age} Jahre alt..."

    def laufen(self):
        return "ich laufe", self.name

    def sprechen(self):
        return "ich spreche"

    @classmethod
    def make_child(cls, cm_name, cm_age, cm_augen):  # CLS => CLASS

        return cls(cm_name, cm_age, cm_augen)

    @staticmethod
    def exists(size, schuhe):
        print("subba funzt!", size, schuhe)


# static methode ohne object!
Person.exists("L", "Puma")

# object erstellt !
rico = Person("Rico", 12, 12)

# object methode!
rico.sprechen()

# static methode, aber von object aufgerufen! kein Unterschied zu Person.exists!!!
rico.exists("M", "ADIDAS")

sophie = Person.make_child("sophie", 4, 2)
print("sophie:", sophie.name, sophie.age, sophie.augenanzahl)
print(sophie)

OBJECT | CLASS
rico = Person("rico", 23, 14)
peer = Person("peer", 41, 7)
