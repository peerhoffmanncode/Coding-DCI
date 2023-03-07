def coffee_machine(beans_in_kg, water_in_liters):
    print("You have ", beans_in_kg, "kgs. Water level: ", water_in_liters)
    # how many cups can we get with this input?  
    # 1kg - 120 cups
    total_cups = 120 * beans_in_kg
    # return beans_in_kg + water_in_liters
    return total_cups

# Forget the sciece --> liters to kg! density? 


# 1 euro per cup
target = 1000
# restaurant manager - has a target! 1000 euros per day
# "reduce" -  stock of coffee, etc.
# Formula! Correctness!! 
# target / total_cups
cups = coffee_machine(1, 4)
rounds_to_make_target_value = target / cups
print("You need to run this machine ", rounds_to_make_target_value)