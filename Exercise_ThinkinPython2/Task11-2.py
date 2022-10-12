'''Read the documentation of the dictionary method setdefault and use it to write a
more concise version of invert_dict.'''

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, [])
        inverse[val].append(key)
    return inverse


d = {"a": 1,
    "p": 1,
    "r": 2,
    "t": 1,
    "o": 1}

print(invert_dict(d))