#### LOOPS ####

### while loops

counter = 0
while True:
    print ("Number: ", counter)
    name = input("your name : ")
    
    if name == "Peer":
        break
    if name == "":
        continue # go back to line 6
    counter += 1
    if counter >= 5:
        break
    
    print("hi i am in the loop ... ")

print(">>>This is the end of the loop!")