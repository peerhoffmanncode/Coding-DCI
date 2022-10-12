l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']

def digit_filter(original):
  new = []
  for string in original:
    if any(char for char in string if char.isdigit()):
      continue
    else:
      new.append(string)
  return new

def main():
  print(digit_filter(l33t))

if __name__ == '__main__':
  main()