import time

# print >> flush = False

countdown = 5
for i in range(countdown, 0, -1):
    print (i, "...", end="", flush=False)
    time.sleep(1)                           # This will wait wired 5 seconds and then print all output at once!
print("done, go!")


# print >> flush = True
countdown = 5
for i in range(countdown, 0, -1):
    print (i, "...", end="", flush=True)
    time.sleep(1)                           # This will print every second !
print("done, go!")