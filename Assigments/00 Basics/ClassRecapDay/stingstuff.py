transformer = ['a', 'u', 't', 'o', 'b', 'o', 't', 's']
print ("".join(transformer))


lists = [ ["John",[ {"name": "Mary"} ], "Amy"], [ 32, 43,{'age': 100}, 51] ]
#Print the value of Mary
#Print the age of 100.

print(lists[0][1][0]["name"])
print(lists[1][2]["age"])

lists[::-2]

print(lists)

lists.reverse()
print(lists)

words = ['cat', 'aadvark', 'elephant', 'squirrel', 'hippo']
newlist = sorted(words, reverse = False)
print(newlist)



words = ['cat', 'aadvark', 'elephant', 'squirrel', 'hippo']
words[1:10] = ["lion"]
print(words)
#words[1:3] = ["lion", "tiger"]
#print(words)