

class Person:
    
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return (f"i am a person {self.name}")
    
    def greeting(self):
        return f"good morning, my name is {self.name}"
    

a = Person("peer")
b = Person("shaban")
c = Person("habibi")

print(a.greeting())
