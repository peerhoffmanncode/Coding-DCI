# Task 1

person = {
  'name': 'Bart Simpson',
  'address': '742 Evergreen Terrace'
}

print(person['name'] + ',' + person['address'])

# Task 2

bart = {'name': 'Bart Simpson'}
homer = {'name': 'Homer Simpson'}

address = {'address': '742 Evergreen Terrace'}

bart.update(address)
homer.update(address)

print(bart['address'])

# Task 3

ages = {
  'Peter': 36,
  'Robin': 29,
  'Michael': 33
}

for name, age in ages.items():
  print(name + ' is ' + str(age) + ' years old')

# Task 4

animals = {
  'Alligator': 1,
  'Tiger': 6,
  'Parrot': 2,
  'Hamster': 5,
  'Dolphin': 8
}

for name, count in animals.items():
  if name.endswith('r'):
    animals.pop(name)

print(animals)