class Human:
    def __init__(self, name):
        self._name = name

    @property  # init
    def name(self):
        print("hello!")
        pass

    @name.getter  # getter
    def name(self):
        return f"{self._name} getting this!"

    @name.setter  # setter
    def name(self, value):
        print(f"{value} setting this!")
        self._name = value.upper()

    @name.deleter  # deleter
    def name(self):
        del self._name


you = Human("")
you.name = "other name"


print(you)
