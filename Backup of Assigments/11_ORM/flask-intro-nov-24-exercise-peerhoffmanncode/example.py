class Person:
    def __init__(self, id, name, location) -> None:
        self.id = id
        self.name = name
        self.location = location


mirjam = Person(1, "Mirijam", "Berlin")
fausto = Person(2, "Fausto", "Hamburg")


# Design have to make some choices
# Algorithms
# - create instance of the class
# - then call the save() method of that instance

# Methods to write
# save() write and commit to db (SQL INSERT INTO tbl)
# delete() delete from db (SQL DELETE FORM tbl)
# update() update a record (SQL UPDATE tbl SET)

# - @staticmethods -
# find() find a record (SQL SELECT FROM tbl)
