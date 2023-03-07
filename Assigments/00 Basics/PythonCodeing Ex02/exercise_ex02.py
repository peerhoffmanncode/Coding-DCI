from random import random
import math


import random
# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


a = random.randint(0, 100)
b = random.randint(1, 100)
lst = [a,b]

print ("Random vales are a:", a)
print ("Random vales are a:", b)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

print("find max val ", max(lst))
print("find min val ", min(lst))
print("calc abs val ", abs(a - 1000 - b))
print("calc power of ", pow(a, b))
print("calc ceiling ", math.ceil(a/b))
print("calc floor val ", math.floor(a/b))
print("calc max of bool ", max(True, False))
print("calc abs compex ", abs(a - (b+3j)))
print("calc abs compex ", round(abs(a - (b+3j)),12))