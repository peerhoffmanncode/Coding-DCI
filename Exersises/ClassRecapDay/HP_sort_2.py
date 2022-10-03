books = {
  'Harry Potter And The Sorcerer\'s Stone': 1241100000,
  'Harry Potter And The Chamber Of Secrets': 771300000,
  'Harry Potter And The Prisoner Of Azkaban': 65210000,
  'Harry Potter And The Goblet Of Fire': 645600000,
  'Harry Potter And The Order Of The Phoenix': 635600000,
  'Harry Potter And The Half Blood Prince': 661300000,
  'Harry Potter And The Deathly Hallows ': 652200000,
}
# Sort and print dictionary
#set counter
nc= 1
## sort and print the first 4
for key_b in sorted(books, key = books.get, reverse = True):
    if nc <4:
        print(f"{nc} {key_b}:  {books[key_b]}" )
    nc +=1