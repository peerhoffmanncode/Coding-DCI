from abc import ABC, abstractmethod
from task_0_singleton import singleton


class FlightClass(ABC):
    """Abstract class for flight class types"""

    @staticmethod
    @abstractmethod
    def perks():
        """abstract method to be implemented"""
        pass


@singleton
class FirstClass(FlightClass):
    """class for FirstClass flight"""

    @staticmethod
    def perks():
        perks = (
            "\tPerks:\n\t\tExtra Leg Room\n\t\tComfortable Seats\n\t\tFree Beverages"
        )
        return perks


@singleton
class BusinessClass(FlightClass):
    """class for BusinessClass flight"""

    @staticmethod
    def perks():
        perks = "\tPerks:\n\t\tExtra Leg Room\n\t\tComfortable Seats"
        return perks


@singleton
class EconomyClass(FlightClass):
    """class for EconomyClass flight"""

    @staticmethod
    def perks():
        perks = "\tPerks:\n\t\tNo perks :D"
        return perks
