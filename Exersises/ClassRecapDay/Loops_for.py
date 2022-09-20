#### LOOPS ####
import time

### FOR loops

start = 5
end = 10
step = 1
my_list_to_for_loop = list(range(start, end, step))

my_list_to_for_loop = {0:"Nadia", 
                       1:"Wojciech", 
                       "something":"Peer", 
                       3:"Reza",
                       4:"Peer"
                       }
print(my_list_to_for_loop)

list1 = ["Peer", "Nadia", "Reza", "Someone"]
list2 = [list1[0], "Nadia", list1[0]]


for i1, i2 in zip(list1, list2):
    if i1 == i2:
        print ("found", i1, i2)
    
