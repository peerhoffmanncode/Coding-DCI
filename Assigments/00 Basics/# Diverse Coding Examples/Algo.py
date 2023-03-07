### Algo - LOOP

from difflib import diff_bytes


sum = 0
count = 0
# user_input = 0

max_rounds = input("enter value of rounds : ")

### LOOP
while count < int(max_rounds):
    
    user_input = int(input("Enter a number: "))
    
    sum = sum + user_input
    count = count + 1
    print("current value: " + str(sum) + " current round " + str(count))

### LOOP END
print("final state: " + str(sum) + " this is my result" )