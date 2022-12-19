''' Dictornary to use with a template HTML file using Jinja2 eg.'''


context = {
  'navigation': [
    'Home',
    'Explore',
    'Notofication',
    'Bookmarks',
    'Lists',
    'Profiles',
    'More',
  ]
}

User = {
  'Name': 'Digital Career Institute'
  'id': "@DC_Institute1"
  'Message': "Your digital Career Starts Here. \nFind the jobs that work for you and get the skills to do them"
  'Joined': DateObjectFrom_DB
  'Following': following_as_int_from_db
  'Followers': follower_as_int_from_db
}

Tweets = [
    {"Name": Name_from_db,
     "id": id_from_db,
     "tweet": coresponding_tweet_from_db},
    {"Name": Name_from_db,
     "id": id_from_db,
     "tweet": coresponding_tweet_from_db},
    {"Name": Name_from_db,
     "id": id_from_db,
     "tweet": coresponding_tweet_from_db},
    ...
]