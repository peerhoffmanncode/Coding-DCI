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

results = [] 
for key in dict1.keys():
  result = dict1[key] * dict2[key]
  results.append(result)

print(sum(results))