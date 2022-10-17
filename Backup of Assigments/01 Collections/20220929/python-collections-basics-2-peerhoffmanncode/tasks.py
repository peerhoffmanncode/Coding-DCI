### Task 1 ###

person = {"name": "Bart Simpson",
          "address": "742 Evergreen Terrace"}

print(f"{person['name']}, {person['address']}")
### Task 2 ###

bart = {"name": "Bart Simpson"}
homer = {"name": "Homer Simpson"}
address = {"adress": "742 Evergreen Terrace"}

bart.update(address)
homer.update(address)

print(bart["adress"])
print(homer["adress"])


### Task 3 ###

ages = {"Peter": 36,
        "Robin": 29,
        "Michael": 33}

for n in ages:
    print(f"{n} is {ages[n]} years old")
    
    
### Task 4 ###

animals = {"Alligator": 7,
           "Tiger": 8,
           "Parrot": 9,
           "Hamster": 11,
           "Dolphin": 12,
}
tmp = {}
for a in animals:
    if a[-1] != "r":
        tmp[a] = animals[a]
print(tmp)