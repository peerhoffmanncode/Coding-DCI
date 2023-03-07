
def test(**kwargs):
    print(kwargs, type(kwargs)) # holds a dict of all passed key word arguments

def test2(*args):
    print(args, type(args)) # holds a tuple of all passed arguments

test(name="TST", lname="bibo", num=10, bibo=True)
test2("TST", "lname=""bibo", 10, True)


my_funny_list = ["z","a", "c", "e", "g", "b", "d", "f"]
my_funny_list.sort()
print(my_funny_list)
print(my_funny_list.pop())
my_funny_list.clear()
print(my_funny_list)

next_list = [[4,5,6], [7,8], [9,10], [11], [1,2,3], [15,14,13], [12]]
next_list.sort()
print(next_list)
print(next_list.pop())
next_list.clear()
print(next_list)

another_list = [[4,5,6], [7,8], [9,10], [11], [1,2,3], [15,14,13], [12], [100,10]]
another_list.insert(4, ["MyFunnyInsert", "AndAnotherOne]"])
print(another_list)
print(another_list.pop())
another_list.clear()
print(another_list)

crazy_lizzt = []
for i in range(10):
    crazy_lizzt.append({"freaking number":i})
print(crazy_lizzt)
crazy_lizzt.reverse()
print(crazy_lizzt)
crazy_lizzt.clear()
print(crazy_lizzt)