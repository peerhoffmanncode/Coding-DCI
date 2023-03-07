### Task 5 ###
# Countdown
import time

for i in range(5, 0, -1):
    print(f"{i}... counting down", end="\r")
    time.sleep(1)
print("Go!                  ")
