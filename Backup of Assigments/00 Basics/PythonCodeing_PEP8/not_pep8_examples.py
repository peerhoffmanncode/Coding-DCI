''' My doc-string to begin with... '''
import sys, os, time

#################
### example 1 ###
#################
print("################################################################## EXAMPLE 1 ########################################")
RES=0                                               # what a nice variable! well, well...?
for i in range(1, 6,2):
    RES=(RES+i/2)
print(RES, "this is a awesome result")












#################
### example 2 ###
#################
print("################################################################## EXAMPLE 2 ########################################")

i = 0
while i < 5:
    i+=1
    if not i == 4:
        print("hello", i)
        











#################
### example 3 ###
#################
def my_little_function(argument1: str, argument2) -> str:
    '''This is a doc-string that explains the usage of this function.
    if this text is longer, you should keep it in readable short lines.
    My function will do ... Use argument1 to give the function a string ... Use argument2 to give the function an integer ... and so on...
    really well done!   
    '''
    my_list = ["item1", "item2",
        "item3", "item4", 
        "banana!" # i created a nice list, awesome and readable... !
    ]
    if my_list[2]=="item3":
        print     ("OH NICE! AN ITEM!",my_list[2])
    
print("################################################################## EXAMPLE 3 ########################################")

# call my_little function  
my_little_function(
    "hello", 42)  #-> here i call the function
