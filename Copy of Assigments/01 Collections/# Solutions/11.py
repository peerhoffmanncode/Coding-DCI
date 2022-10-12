participants = ['Brian', 'Britney', 'Ben']
scores = {
  'brian': 25,
  'britney': 80,
  'ben': 50
}

def get_score(name):
  if not name in participants:
    print('{} did not participate'.format(name))
    return
  
  score = scores[name.lower()]
  print('{} scored {} points'.format(name, score))

def main():
  get_score('Britney')
  get_score('Paul')

if __name__ == '__main__':
  main()