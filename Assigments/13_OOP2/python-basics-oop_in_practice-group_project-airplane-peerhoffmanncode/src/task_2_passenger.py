from abc import ABC, abstractmethod


class Person(ABC):
    """abstract class for person types"""

    def __init__(self, wired_number: str, name: str) -> None:
        self.wired_number = wired_number
        self.name = name

    @abstractmethod
    def __str__(self) -> str:
        """to be implemented"""


class Pilot(Person):
    """Pilot class"""

    def __str__(self) -> str:
        return f"{self.name} ({self.wired_number}) is the pilot."


class Crew(Person):
    """Crew class"""

    def __str__(self) -> str:
        return f"{self.name} ({self.wired_number}) a crew member."


class Passenger(Person):
    """Passenger class"""

    def __str__(self) -> str:
        return f"{self.name} ({self.wired_number}) is a passenger."
