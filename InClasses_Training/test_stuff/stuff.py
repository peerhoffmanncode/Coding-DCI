b = ["f", 1.1, {"c": 2}]

def something(a,c):
    global b
    b.append("something")

something(1,2)
