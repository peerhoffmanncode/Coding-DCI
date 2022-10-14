''' Progrmm to read data from a file'''

f = open('numbers.txt', 'w')
# open a file and read the data

for i in range(1, 1_000_001):
    lines = f.write(f"{i}\n")
f.close()

# f = open('numbers.txt', 'r')
#     lines = f.readlines()
# f.close()