total = 0

def calc_fuel(fuel):
    global total
    result = int(fuel) // 3 - 2
    if result <= 0:
        return
    
    total += result
    calc_fuel(result)
    

with open('./input', 'r') as f:
    inputs = f.read().split('\n')
    
for fuel in inputs:
    if fuel == '':
        continue
    
    calc_fuel(fuel)

print(total)
