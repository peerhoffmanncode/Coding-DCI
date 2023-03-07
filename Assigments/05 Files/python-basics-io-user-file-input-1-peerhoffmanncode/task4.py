#### Task 4 ###

with open("src/data/task4.txt") as file:
    even = []
    for num, line in enumerate(file):
        if num % 2:
            even.append(line)
        else:
            print(line, end="")
    for line in even:
        print(line, end="")
