
######################################
### Task 1
######################################

three_mul = 'fizz'
five_mul = 'buzz'
num1 = 3
num2 = 5
max_num = 100
   
for i in range(1, max_num):
    
    # % or modulo division gives you the remainder 
    if i % num1 == 0 and i % num2 == 0:
        print(i, three_mul + five_mul)   
    elif i % num1 == 0:
        print(i, three_mul)
    elif i % num2 == 0:
        print(i, five_mul)
    else:
        print(i)

       
######################################
### Task 2
######################################

n = 5
number = 1
sum = 0
while number < n + 1:
    sum = sum + number
    number = number + 1
print("Sum =", sum)


######################################
### Task 3
######################################

n = 5
sum = 0
for num in range(n+1):
    sum += num
print("Sum =", sum)


######################################
### Task 4
######################################

# 4.1
for x in range(3):
    print(x)
#4.2 
for j in range(0, 5):
    print("This is loop number" + str(j))
#4.3
x = 10    
while x > 0:
    print(x)
    x -= 1
#4.4
countdown = 5
while countdown != 0:
    print(f"{countdown}")
    countdown -= 1
else:
    print("Start!")

    
######################################
### Task 5
######################################

x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x == y or x == z or y == z:
    result = 0
else:
    result = x + y + z

print("Calculated sum is ", result)


######################################
### Task 6
######################################
    
x = int(input("First number: "))
y = int(input("Second number: "))

result = x + y

if result >= 15 and result <= 20:
    result = 20
print("Calculated sum is ", result)


######################################
### Task 7
######################################

a = input("First value: ")  # bug
b = input("Second value: ") # bug

print("Before swapping: a =", a, " ,b = ", b) # bug

#b, a = a, b

tmp = a
a = b
b = tmp # <- missing ! bug

print("After swapping: a =", a, " ,b = ", b) # bug


######################################
### Task 8
######################################

x = float(input("First number: "))
y = float(input("Second number: "))
z = float(input("Third number: "))

print("The maximum value is ", max(x, y ,z))
print("The minimum value is ", min(x, y ,z))


######################################
## Task 9
######################################

x = input("Type your value: ")

if x == "0":
    x = False
elif x == "1":
    x = True
else:
    pass

print("Your entered value is now ", x)


######################################
### Task 10
######################################

x = int(input("First number: "))
y = int(input("Second number: "))

if x % y == 0:
    print("First number is divisible by second number, result =", x / y)
elif y % x == 0:
    print("Second number is divisible by first number, result =", y / x)
else:
    print("Numbers are non-divisible!")