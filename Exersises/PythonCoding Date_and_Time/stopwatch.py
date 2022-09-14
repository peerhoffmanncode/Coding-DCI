import time
import os

os.system("clear")

current_time = time.time()

while True:
    try:
        print(f"Stopwatch: {round(time.time() - current_time, 1)} seconds passed...       ", 
              end = "\r", flush = True)
        time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"Stopwatch: {round(time.time() - current_time, 1)} seconds DONE!!!         ", 
              end = "\r")
        break
    
print("")
print("\n")