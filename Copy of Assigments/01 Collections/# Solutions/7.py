swap_list = [23, 65, 19, 90]

def swap(swap_list, index_1, index_2):
  swap_list[index_1], swap_list[index_2] = swap_list[index_2], swap_list[index_1]
  return swap_list

def main():
  print(swap(swap_list, 1, 3))

if __name__ == '__main__':
  main()