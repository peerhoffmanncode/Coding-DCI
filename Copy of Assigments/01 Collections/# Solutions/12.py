from string import ascii_lowercase as alphabet

def pangram(input):
  return set(alphabet) - set(input.lower()) == set([])

def main():
  print(pangram('Waltz, bad nymph, for quick jigs vex.'))
  print(pangram('Not all characters.'))

if __name__ == '__main__':
  main()