
# class Animal:
#     def __init__(self, species, can_walk):
#         self.species = species
#         self.can_walk = can_walk    

#     def walk(self):
#         if self.can_walk:
#             return f"{self.species} can walk!"
#         return f"{self.species} cannot walk!"


# # inherit!
# class Human(Animal):

#     def __init__(self, species, can_walk, name):
#         super().__init__(species, can_walk)     
#         self.name = name 


#     # override walk() method
#     def walk(self):
#         return "Walks on land"  

# # create an instance of Animal
# animal = Animal('monkey', True)
# # print(animal.walk())

# animal2 = Animal('snails', False)
# # print(animal2.walk())


# # create an instance of Human
# # matteo = Human('homo sapiens', True, 'Matteo Messina Denaro')
# # print(matteo.walk())


# class A:
#     name = "fausto"

#     def walk(self):
#         print("Loves to walk!")


# class B:
#     name = "Victor"
#     last_name = "Shaban"


# class C:
#     middle_name = "XYZ"

# # resolves names
# class Multiple(B, A, C):
#     pass    

# instance = Multiple()
# print(instance.name)
# print(instance.last_name)
# print(instance.middle_name)
# instance.walk()



class Animal:
    def __init__(self, name) -> None:
        self.name = name

# create an instance of an Animal?
# How do I create an instance of an Anima?
animal = Animal("dog")        


class SearchForm(forms.Form):
    search_term = forms.CharField()
# How do I create an instance of a SearchForm?
animal = SearchForm()
