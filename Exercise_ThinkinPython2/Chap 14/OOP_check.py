class TestClass:
    """my fancy doc str"""

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        print(f"Name der classe: {type(self).__name__}")
        print(f"Name der classe: {type(self).__qualname__}")
        print(f"Name der classe: {type(self).mro()}")
        print(f"Name der classe: {type(self).__doc__}")
        return f"__str__ ich bin eine class mit der variable name={self.name}"

    def __repr__(self):
        return f"__repr__ ich bin eine class mit der variable {self.name}"

    # SETTER
    def set_name(self, new_name):
        print(f"changing name from {self.name} to {new_name}")
        self.name = new_name

    # GETTER
    def get_name(self):
        return f"mein Name ist {self.name}"


test = TestClass("Bibo")

print(test)
print(test.get_name())
test.set_name("Bumbes")
print(test.get_name())
