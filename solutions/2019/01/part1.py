with open('./input', 'r') as f:
    inputs = f.read().split('\n')
    
result = 0
for fuel in inputs:
    if fuel == '':
        continue
    
    result += int(fuel) // 3 - 2

print(result)
