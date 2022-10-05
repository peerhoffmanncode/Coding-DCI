fruit_colors = {
    "apple": "red",
    "berries": "blue"
}

# Get Method (Get with default value)
fruit_colors.get("Dose not exist!")


# Access the items ####

for k, v in fruit_colors.items():
    print (k,v)

for k in fruit_colors.keys():
    print(k)

for v in fruit_colors.values():
    print(v)
    

for a in enumerate(fruit_colors.values()):
    print(a)
    

# Using Enumeration
list_of_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]

for index, day in enumerate(list_of_days, start = 1):
    print(f"{day.capitalize()}, is the {index} day of the week")
    
    
    
### sort

books = [
    {"cost": 10, "name": 'Python 2'},
    {"cost": 1, "name": 'Best tourism sites in Napoli'},
    {"cost": 5, "name": 'Basket Weaving for Pros'},
    {"cost": 8, "name": 'Java for dummies'},
]
# print(sorted(books, key=lambda book: book['cost']))

# Sorting !
func = lambda book: book['name']
print("*** Sorted ascending ***")
print(sorted(books, key=func))
print("*** Sorted descending ***")
print(sorted(books, key=func, reverse=True))