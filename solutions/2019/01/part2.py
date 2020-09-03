total = 0

def calc_fuel(fuel):
    result = int(fuel) // 3 - 2
    if result <= 0:
        return 0
    
    return result + calc_fuel(result)
    
with open('./input', 'r') as f:
    inputs = f.read().strip().split('\n')
    
for fuel in inputs:
    total += calc_fuel(fuel)

print(total)
