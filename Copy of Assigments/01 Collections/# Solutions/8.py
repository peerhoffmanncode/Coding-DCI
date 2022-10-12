def top3(input_dict):
  sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1]))
  titles = sorted_dict.keys()
  values = sorted_dict.values()

  print('1. ' + titles[0] + ': ' + str(values[0]))
  print('2. ' + titles[1] + ': ' + str(values[1]))
  print('3. ' + titles[2] + ': ' + str(values[2]))

books = {
  'Harry Potter And The Sorcerer\'s Stone': 1241100000,
  'Harry Potter And The Chamber Of Secrets': 771300000,
  'Harry Potter And The Prisoner Of Azkaban': 65210000,
  'Harry Potter And The Goblet Of Fire': 645600000,
  'Harry Potter And The Order Of The Phoenix': 635600000,
  'Harry Potter And The Half Blood Prince': 661300000,
  'Harry Potter And The Deathly Hallows ': 652200000,
}

def main():
  top3(books)

if __name__ == '__main__':
  main()