def count_characters(word):
  counts = {}
  for char in word.lower():
    counts.setdefault(char, 0)
    counts[char] = counts[char] + 1

  return counts

def main():
  print(count_characters('Elephant'))

if __name__ == '__main__':
  main()