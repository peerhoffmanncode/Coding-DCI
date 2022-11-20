import re  # import the regular expression library

text_to_searched_in = "some text mail@web.de some text"  # target text

# find something at the beginning
pattern1 = r"^[a-z]{4}"                           # the actual regular expression
begin = re.search(pattern1, text_to_searched_in)  # using the pattern to search the target text
print(begin)                                      # printing out the match

# find something at the beginning
pattern2 = r"([a-z]+$)"                           # the actual regular expression
ending = re.search(pattern2, text_to_searched_in) # using the pattern to search the target text
print(ending)                                     # printing out the match





#x = re.findall(pattern, text_to_be_searched)
#x = re.match(pattern, text_to_be_searched)
#x = re.finditer(pattern, text_to_be_searched)
