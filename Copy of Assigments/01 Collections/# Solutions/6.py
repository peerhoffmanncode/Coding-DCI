def mean(input):
  column_mean = [sum(number) / len(number) for number in zip(*input)]
  return str(sum(column_mean) / len(column_mean))

def main():
  print(mean([[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]))

if __name__ == '__main__':
  main()