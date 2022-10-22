import re

text = """Psycopg converts Python variables to SQL values using their types: 
the Python type determines the function used to convert the object into a string representation suitable for PostgreSQL.
Many standard Python types 1bas.icx2@aold.cu.com are already adapted to the correct SQL representation. Passing parameters to an SQL statement happens
in functions such as cursor.execute() by using %s placeholders bumbes@bubu.zsh in the SQL statement, and passing a sequence of values as 
he second argument of the donald.trump@bibo.bum function. For example the Python function call:"""

pattern = r'([\w\.]+)@([\w\.]+)(\.[A-Za-z0-9]+)'

res1 = re.finditer(pattern, text)
res2 = re.findall(pattern, text)
res3 = re.search(pattern, text)
res4 = re.match(pattern, text)
res5 = re.fullmatch(pattern, text)
res6 = re.split(pattern, text)
res7 = re.sub(pattern, 'HOOOORRRRAAY!', text)
res8 = re.escape(pattern)

for i in res1:
    print ("finditer: ", i.start(), i.end(), i.group())
    print(i.group(0), i.group(1), i.group(2), i.group(3))
        
print()
print ("findall: ", res2)
print()
print ("search: ", res3)
print ()
print ("match :", res4)
print()
print ("fullmatch :", res5)
print()
print ("split :", res6)
print()
print ("sub :", res7)
print()
print ("escape :", res8)