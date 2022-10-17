def chunk(the_dict: dict, chunks: int):
    ''' functionn to chuck up a given dictonary.'''

    # validation
    if chunks < 1: 
        chunks = 1

    # var definition
    reps = 0
    result = []
    tmp_dict = {}
    # loop over dict
    for key, value in the_dict.items():
        tmp_dict.update({key: value})
        reps += 1
        if reps >= chunks:
            result.append(tmp_dict)
            tmp_dict = {}
            reps = 0

    # in case of unsuitable chuck, append rest!
    if tmp_dict:
        result.append(tmp_dict)
    return result

# Data
data = {
  'key1': 1,
  'key2': 2,
  'key3': 3,
  'key4': 4,
  'key5': 5,
  'key6': 6,
}

# call teh test
print(chunk(data, 2))