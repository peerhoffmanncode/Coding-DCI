## BASIC DATAYPES
# Str       - IMMUTABEL !!
var = "string"  # collection of chars
#print("line3", id(var), var)

var.upper()
#print("line7", id(var), var)
# print(var2)

# Int       - mutable
var = 10
#print(id(var), var)
var = var + 1
#print(id(var), var)

# Float
var = 10.0

# Complex
var = 1j+1

#print(type("STRING"))

## DATATYPES

# List
var = [5,10,20,1,2,4,99]
# print(var)
# var.sort()
# print(dir(var))

# Tuple
var1 = 10
var2 = 20
var = (var1, var1, var2, var2, var2)
#print(type(var))

# Dict
#           0   1   2   3    
#listvar = [10,20,"fausto",4000]
#listvar[0]

       # KEY   VALUE
var = {"0":"Hoffmann",
       1:[1,2,3],
       "Fausto":3985235.2340995834,
}

print(var["Fausto"])