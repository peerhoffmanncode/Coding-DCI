# condition to check
# while condition is true > LOOP !
# >> CONDITIONAL END !!
counter = 0

while True:            # setting the condition of the LOOP (>> TRUE)

    name = input("we are at line 8 ! - > enter name: ") # name = ""           # define VAR name

    counter += 1
    print("loop for: ", counter, "name is:", name)
    if name == "Fausto":                    # <- is name = Fausto  >> true ????
        print("finally you entered a name! YEAH!")  # print something
        break                               # stop the loop > and continue at line 16 !
    elif name == "Shaban":                  # <- is name = Shaban  >> true ????
        print("finally you entered a name! YEAH!")  # print something nice
        break                               # stop the loop > and continue at line 16

    ## JUMP BACK TO LINE 8 !

print ("end of loop", name)