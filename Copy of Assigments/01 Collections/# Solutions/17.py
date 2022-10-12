strings = ['Digital', 'Career', 'Institute', 'Lecture', 'Exercise']

def unique_char_count(string):
  return len(list(set(string)))

def unique_char_sort(strings):
  strings.sort(key = unique_char_count)
  return strings

def main():
  print(unique_char_sort(strings))

if __name__ == '__main__':
  main()