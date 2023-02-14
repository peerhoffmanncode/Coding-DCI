class Animal:

    def __init__(self, name:str, sound: str) -> None:
        self.name = name
        self.sound = sound

    def speak(self) -> str:
        return f'The {self.name} says "{self.sound}"'
