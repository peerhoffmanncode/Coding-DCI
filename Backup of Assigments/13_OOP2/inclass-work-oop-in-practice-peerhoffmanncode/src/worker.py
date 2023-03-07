from abc import ABC, abstractmethod
from tool import Laptop


# Complete the class Worker
class Worker(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        print(f"\n\n{self.name} starts working:")

    @abstractmethod
    def take_break(self, minutes):
        print(f"\n\n{self.name} takes {minutes} minutes break:")


# Complete this class, so that it would work properly. Implement the missing methods
class Programmer(Worker):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def __str__(self):
        return f"{self.name} codes with {self.language}"

    def work(self):
        print("The programmer is coding")

    def take_break(self, minutes):
        print("The programmer is takeing a break")


# Complete the class Janitor.
# Janitor is a subclass of the class Worker
# work(): Janitor fixes pipes with "tool"
# take_break(): Janitor listens to music
class Janitor(Worker):
    def __init__(self, name, tool):
        super().__init__(name)
        self.tool = tool

    def __str__(self):
        return f"{self.name} uses {self.tool}"

    def work(self):
        print(f"Janitor fixes pipes with {self.tool}")

    def take_break(self, minutes):
        print(f"Janitor is listening to music for {minutes} minutes")
