## Example 001
my_first_variable = "this is a damn cool text!"
my_second_varialble = " ... and damn what a nice second text to add! Yay..."
print (len(my_first_variable))
print (my_first_variable + my_second_varialble)
print (my_first_variable + my_second_varialble.upper())


## Tasks

# 001
city = "London"
print (city)

# 002
city = "Berlin"
population = 3645000
print (city + " " + str(population))

# 003
city = "london".capitalize()
population = population = 3645000
print (city, city.isalpha())
print (population)

# 004
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
print("capital: " + str(text.index("capital")))

# 005
text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
mynewlist = text.split()
print (mynewlist)

# 006
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
text = text.replace("capital", "capital of Germany")
print (text)