def fix_name_shemes(dictionary):
    ''' function that fixes the name schema !'''
    tmp_dict = {} 
    for key, value in dictionary.items():
        new_key = key.replace(' ', '_').lower()
        tmp_dict.update({new_key:value})
        
    # return back to global scope dict!
    dictionary = tmp_dict
    return dictionary # only to print it ;-)


## Test cases

natural_case1 = {
  'Company name': 'Digital Career Institute',
  'Street': 'Vulkanstraße',
  'House Number': 1,
  'City': 'Berlin'
}

natural_case2 = {
  'Movie name': 'James Bond 007: Skyfall',
  'Director': 'Sam Mendes',
  'Production Year': 2012,
  'Duration in minutes': 143,
  'Production countries': ['US', 'UK']
}

print(fix_name_shemes(natural_case1))
print(fix_name_shemes(natural_case2))