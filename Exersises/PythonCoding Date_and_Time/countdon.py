import time
import os

os.system("clear")

n = int(input("Give a number to count down to : "))

store_current_time = time.time()
for i in range(n, 0, -1):
    print (f"countdown: {i}...", end="\r", flush= True)
    time.sleep(1)
    
print("DONE !               ")
print("Countdown started at:", time.ctime(store_current_time))
print("Countdown ended at  :", time.ctime(time.time()))