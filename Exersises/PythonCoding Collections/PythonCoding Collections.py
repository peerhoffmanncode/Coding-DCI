def greeting(gender: str, firstname: str, lastname: str) -> tuple:

    if gender == 'male':
        return (f"Good Morning Mr. {firstname}", f"{firstname} {lastname}")
    else:
        return (f"Good Morning Ms. {firstname}", f"{firstname} {lastname}")



### Python Tuple
# define tuples
my_tuple1 = ("Name1", "Name2", "Name3", "Name4")
my_tuple2 = "Name5", "Name6"
# concatinate tuples
my_tuple3 = my_tuple1 + my_tuple2
# print result
print("my tuple 1", my_tuple1)
print("my tuple 2", my_tuple2)
print("my tuple 3", my_tuple3)
print("my tuple 3 - count: ", my_tuple3.count("Name1"))
print("my tuple 3 - count: ", my_tuple3.index("Name3"))
print(greeting("male", "Peer", "Hoffmann"))
print(greeting("female", "Some", "Girl"))