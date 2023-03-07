numbers = [3, 24, 50, 79, 88, 150, 345]


def twoSum(numbers, target):
    for idx1, n1 in enumerate(numbers):
        for idx2 in range(idx1, len(numbers)):
            if n1 + numbers[idx2] == target and idx1 != idx2:
                print(n1, numbers[idx2], idx1, idx2)
                return [idx1 + 1, idx2 + 1]


print(twoSum(numbers, 200))
