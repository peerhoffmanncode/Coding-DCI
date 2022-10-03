# Task - Combine lists into a dict

color_names = ['red', 'green', 'blue']
color_hex = ['#FF0000','#00FF00', '#0000FF']
comb_dict = {}

for a,b in zip(color_names,color_hex):
    comb_dict[a] = b
    
print(comb_dict)