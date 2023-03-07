############### Task 1 ################

print("")
print("Task1")
print("")
for i in range(0,3):
    mynumber = int(input("Enter number:"))
    if mynumber % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
        

############### Task 2 ################

print("")
print("Task2")
print("")
range_start = range_end = range_step = 1

range_args = int(input("Enter number of arguments in range() function:"))
if range_args > 0:
    range_start = int(input("Enter starting number: "))
    range_end = range_start + 1
if range_args > 1:   
    range_end = int(input("Enter stopping number: "))
if range_args > 2:    
    range_step = int(input("Enter step: "))

if range_start > range_end:
    if range_step > 0:
        range_step = range_step * -1
 
for i in range(range_start,range_end+1,range_step):
    print (i)
    

############### Task 3 ################
 
print("")
print("Task3")
print("")
user_number = int(input("Enter a number: "))
for i in range(user_number+1, 1, -1):
    if user_number % i == 0:
        print (i)


############### Task 4 ################

print("")
print("Task4")
print("")
user_number = int(input("Enter a number: "))

is_a_prime = True
if user_number > 1:
    for i in range(2, user_number):
        if (user_number % i) == 0:
            is_a_prime = False
            break
        
if is_a_prime == True and user_number > 1:
    print(user_number, "is a prime number!")
else:
    print(user_number, "is NOT a prime number! Could be divided by", i)
        

############### Task 5 ################

print("")
print("Task5")
print("")
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz!")
    elif i % 3 == 0: 
        print("Fizz!")
    elif i % 5 == 0: 
        print("Buzz!")
    else:
        print(i)


############### Task 6 ################

print("")
print("Task6")
print("")
for i in range(1000, 2001):
    if i % 7 == 0 and i % 5 != 0: 
        print (i)
