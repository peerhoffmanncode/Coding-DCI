# Task - Matrix mean
def calc_mean(numbers):
    ''' function to calculate wired matrix mean stuff ...
        probabbly wrong ... but who knows ...'''

    x = []
    for idx, n in enumerate(numbers):
        x.append(f"x{idx} = {sum(n) // len(n)}")

    y = []
    summ = 0
    for idx in range(len(numbers[0])):
        for n in numbers:
            summ += n[idx]
        y.append(f"y{idx} = {summ // len(numbers[0])}")
    return x + y

numbers = [[5, 6, 3],
           [8, 3, 1],
           [9, 10, 4],
           [8, 4, 2]]

print(calc_mean(numbers))