
## No Flush set

from itertools import count

countdown = 9
For i in range(countdown, 0, -1):
    print (i,"...", end ="", flush=False)