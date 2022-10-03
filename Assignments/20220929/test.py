list1 = ["red", "blue", "green"]
list2 = ["X123", "Y456", "Y789"]

# dict
dict_test = {}
for i in range(len(list1)):
    dict_test[list1[i]] = list2[i]
print(dict_test)