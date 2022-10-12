def mul(a, b):
    ''' multiply a and b '''
    return a * b

### Given ###
dict1 = {
  'a': 4,
  'b': 16,
  'c': 3
}

dict2 = {
  'a': 8,
  'b': 2,
  'c': 3
}

# why simple when you can make things complex for no reason :)
res = 0
for d1, d2 in zip(dict1, dict2):
    res += mul(dict1[d1], dict2[d2])
print (res)