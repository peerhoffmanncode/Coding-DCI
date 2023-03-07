n1 = 5
n2 = 5
n3 = 5
n4 = 7
n5 = 8
n6 = 9
n7 = 1
n8 = 1
n9 = 3
n0 = 4

# (456) 123-7890
# format string

# Version 1
print(f"({n1}{n2}{n3}) {n4}{n5}{n6}-{n7}{n8}{n9}{n0}")

# Version 2
print("({}{}{}) {}{}{}-{}{}{}{}".format(n4, n5, n6, n1, n2, n3, n7, n8, n9, n0))

# Version 3
print("({}{}{}) {}{}{}-{}{}{}{number0}".format(n4, n5, n6, n1, n2, n3, n7, n8, n9, number0 = n0))
print("({number0}{}{}) {number0}{}{}-{}{}{}{number0}".format(n4, n5, n6, n1, n2, n3, n7, n8, n9, number0 = n0))

