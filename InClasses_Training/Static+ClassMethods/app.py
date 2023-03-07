class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hi, i am {self.name}, and i am {self.age} old!"

    def normal_method(self):
        pass

    @staticmethod
    def make_all_upper(name):
        return name.upper()

    @classmethod
    def cl_method(cls, name, age):
    '''
        >>> add(2,2)
        4
    '''


        if age > 90:
            age = 90
        return cls(cls.make_all_upper(name), age)


if __name__ == "__main__":

    my_ins = MyClass("peer", 15)
    my_ins.normal_method()
    a = my_ins.make_all_upper("peer")
    b = MyClass.make_all_upper("emily")
    c = MyClass.cl_method("michel", 120)
    print(c)
    d = my_ins.cl_method("nadia", 30)
    print(d, c)
