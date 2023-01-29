def pascal(n:int):
    if n <= 0:
        return [1]

    line = [1]
    previous_line = pascal(n-1)
    for i in range(len(previous_line)-1):
        line.append(previous_line[i] + previous_line[i+1])
    line += [1]
    return line

for i in range(10):
    print(pascal(i))
