'''Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary.'''

with open("./words.txt", "r") as file:
    data = file.readlines()

all_words = {}
for lines in data:
    for word in lines.split(" "):
        all_words[word.rstrip("\n")] = 0
        
if "Write" in all_words:
    print("nice, found 'Write'")
else:
    print("ahh, no 'Write'")
    
if "Dumbo" in all_words:
    print("nice, found 'Dumbo'")
else:
    print("ahh, no 'Dumbo'")