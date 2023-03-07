# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

import math
import random


#### Task 1
# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))
# num3 = int(input("Num3: "))

# if num1 == num2 == num3:
#     print ("The triple sum is:", (num1+num2+num3)*3)
# else:
#     print ("The sum is:", num1+num2+num3)



#### Task 2
# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))

# if num1 > num2:
#     print ("The result of calculation is: ", (num1-num2)*2)
# else:
#     print ("The result of calculation is: ", abs(num1-num2))



#### Task 3
# num1 = int(input("Num1: "))y
# if num1 % 2 != 0:
#     print(num1, "is an odd number!")
# else:
#     print(num1, "is an even number!")



# #### Task 4
# r = float(input("Input the radius of the circle : "))
# pi = math.pi
# print("The area of the circle with radius", r, "  is:", (pi*(r*r)))



# ### Task 5
# random_number = random.randint(1,10) # 5
# usernum = 0
# while usernum != random_number:
#     usernum = int(input("Guess a number between 1 and 10 until you get it right : "))
# print ("Well guessed!")



#### Task 6
#### Formel C/5 = F-32/9
# temp = int(input("to enter a temperature "))
# flag = str(input("to enter a shortcut for given scale (C for Celsius, F for Fahrenheit)"))

# if flag == "C" or flag == "c":
#     print (f"The temperature in Fahrenheit is {9*(temp/5)+32} degrees")
# else:
#     print (f"The temperature in Celsius is {5*((temp-32)/9)} degrees")   



#### Task 7
# size = 5
# for i in range(1,size+1): print("*" * i)
# for i in range(size-1,0,-1): print("*" * i)



#### Task 8

# import time
# start = time.time()

count= 0
num1 = 0
num2 = 1
fib =  0
print("Index of Fibonacci :", count, "Result: ", fib)

for count in range(0,10+1):
    fib = num1 + num2
    if count > 1:
        num1 = num2
        num2 = fib
    print("Index of Fibonacci :", count, "Result: ", fib)
    
#print("done! It took :", round(time.time()-start))
