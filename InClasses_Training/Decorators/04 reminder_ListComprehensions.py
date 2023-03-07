names = ["bibi bum", "bobo bam", "babu zap", "bob zip"]
cap_names = []


### for loop ####
for n in names:
    cap_names.append(n.title())
print (cap_names)
    
### list comprehension
cap_names = [ n.title() for n in names]
cap_name_no_z = [ n.title() for n in names if not "z" in n]
print (cap_names)
print (cap_name_no_z)