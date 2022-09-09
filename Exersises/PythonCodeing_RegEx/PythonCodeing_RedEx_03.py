import re


### Task 1 ###
print("\n ### Task 1 ###\n")
text = "Berlin is a world city of culture, politics, media and science."
pattern= r"\s"
result, _ = re.search(pattern, text).span()
print("The first white-space character is located at position:",result)

### Task 2 ###
print("\n ### Task 2 ###\n")
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
pattern= r"Frankfurt"
result = re.search(pattern, text)
print(result)

### Task 3 ###
print("\n ### Task 3 ###\n")
text = "Berlin is a city of culture."
pattern= r"\s"
subln = "-"
result = re.sub(pattern, subln,text)
print(result)

### Task 4 ###
print("\n ### Task 4 ###\n")
text = "Berlin is a city of culture."
pattern= r"in"
result = re.search(pattern, text)
print(result)

### Task 5 ###
print("\n ### Task 5 ###\n")
text = "Berlin is a city of culture."
pattern= r"^B\w+"
result = re.search(pattern, text)
print(result)

### Task 6 ###
print("\n ### Task 6 ###\n")
text = "The rain in Spain."
pattern= r"ai"
result = re.findall(pattern, text)
print(len(result))