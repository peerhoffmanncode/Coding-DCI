import sys

n = len(sys.argv)
print(f"Number of arguments: {n}")

print(f"Name of script: {sys.argv[0]}")

sum_of_given_number = 0
for i in range(1, n):
    sum_of_given_number += int(sys.argv[i])

print(f"Sum : {sum_of_given_number}")