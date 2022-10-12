list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

def intersection(list_1, list_2):
  return list(set(list_1).intersection(list_2))

def main():
  print(intersection(list_1, list_2))

if __name__ == '__main__':
  main()