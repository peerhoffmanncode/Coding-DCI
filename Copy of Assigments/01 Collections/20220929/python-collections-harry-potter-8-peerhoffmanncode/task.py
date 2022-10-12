def find_bestseller(dictonary: dict) -> list:
    # sort the list for the values! x [1] to select values, not keys!
    #sort_orders = sorted(dictonary.items(), key=lambda collumn: collumn[1], reverse=True)
    sort_orders = sorted(dictonary.items(), key=lambda collumn: collumn[1], reverse=True)
    return sort_orders


books = {
  'Harry Potter And The Sorcerer\'s Stone': 1_241_100_000,
  'Harry Potter And The Chamber Of Secrets': 771300000,
  'Harry Potter And The Prisoner Of Azkaban': 65210000,
  'Harry Potter And The Goblet Of Fire': 645600000,
  'Harry Potter And The Order Of The Phoenix': 635600000,
  'Harry Potter And The Half Blood Prince': 661300000,
  'Harry Potter And The Deathly Hallows ': 652200000,
}

bestseller = find_bestseller(books)
for index, book in enumerate(bestseller):
    bookname, sales = book
    print(f"{index+1:02}. {bookname:<42}:{sales:11}")