import time, datetime

epoch = 0
current_time = time.time()

dann = datetime.datetime.strptime(time.ctime(epoch), "%a %b %d %H:%M:%S %Y")
heute = datetime.datetime.strptime(time.ctime(current_time), "%a %b %d %H:%M:%S %Y")

print(dann)
print(heute)

print(heute - dann)
