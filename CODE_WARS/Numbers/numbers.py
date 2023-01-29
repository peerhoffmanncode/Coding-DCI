def get_pins(observed):
    p = [['0', '8'],
         ['1', '2', '4'],
         ['2', '1', '3', '5'],
         ['3', '2', '6'],
         ['4', '1', '5', '7'],
         ['5', '2', '6', '8', '4'],
         ['6', '3', '9', '5'],
         ['7', '4', '8',],
         ['8', '5', '0', '7', '9'],
         ['9', '6', '8'],
         ]
    result = ""
    for n in observed:
        for i in range(10):
            if i == int(n):
                subset = sorted(p[i])
                result = result + "".join(subset)
                
    return list(result)
                    
                
                
#('8', ['5','7','8','9','0']),

print((get_pins('8')))