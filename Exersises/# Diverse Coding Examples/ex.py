# Strings "a-z 0-9 !&"%$/($)"
# integer 0-9   10
# float X.Y     10.0


my_var = "my string"
print (my_var)

my_var = "my next \"with\" string"
print (my_var)

my_var = "my test and a hash tag \# "  # my comment
print (my_var)

my_var1 = "part 1 of the string________".find("string")    # << 14 INT
my_var2 = "part 2 of the string"
my_var4 = 10

my_var3 = str(my_var1) + " " + my_var2 + " " + str(my_var4)

#my_VAR_NEW = my_var1.upper()

print (my_var3)